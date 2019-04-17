import json
from jinja2 import Environment, FileSystemLoader
from tools.utils import *
import re

S = 'ref_genome_fa'


class ToJson(object):
    def __init__(self, path):
        self.path = path

    @property
    def json_file(self):
        s = load_file(self.path)
        return json.loads(s)

    def joined_dictionary(self):
        united = {}
        for k, v in self.json_file.items():
            united.update(v)
        return united


class InitializeArguments(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.add_large_genome()
        self.add_indexes()
        self.add_outdir()
        self.add_step()

    def add_index(self, indexes):
        result = self.parameters.get(indexes[1])
        if result == "''" or result is None:
            fasta_path = self.parameters.get(indexes[0])
            path_drop_fa = os.path.splitext(fasta_path)[0]
            if path_drop_fa != "''":
                self.parameters[indexes[1]] = '.'.join((path_drop_fa, '.'.join(indexes[2:])))

    def add_large_genome(self):
        # 添加 large_index
        if 'large_genome' not in self.parameters or re.match('false', self.parameters['large_genome'],
                                                             flags=re.IGNORECASE):
            self.parameters['large_genome'] = 'false'.title()
        else:
            self.parameters['large_idx'] = '--large-index'
            self.parameters['large_genome'] = 'true'.title()

    def add_indexes(self):
        ref_genome_indexes = ['ref_genome_fa', 'align_idx', 'HISAT2']
        salmon_idx_type = self.parameters.get('idx_type', 'salmon_index')
        transcript_indexes = ['transcriptome_fa', 'quantifier_idx', 'Salmon', salmon_idx_type]
        ref_dict_indexes = ['ref_genome_fa', 'ref_genome_dict', 'dict']
        for i in (ref_genome_indexes, transcript_indexes, ref_dict_indexes):
            self.add_index(i)
            if i[1] != 'ref_genome_dict':
                # 在初始化时完成 index 目录的创建
                index_dir = self.parameters[i[1]]
                if index_dir != "''":
                    mkdir(os.path.dirname(index_dir))

    def add_outdir(self):
        out_dir = self.parameters.get('out_dir')
        work_dir = self.parameters.get('work_dir')
        if work_dir.endswith('/'): work_dir = work_dir[:-1]
        if out_dir == "''" or out_dir is None:
            out_dir = '/'.join((work_dir.rsplit('/', 1)[0], 'out'))
            self.parameters['out_dir'] = out_dir
        log('Workdir is {}'.format(work_dir))
        log('Outdir is {}'.format(out_dir))

    def add_step(self):
        arg = get_arg()
        for i, v in arg.items():
            self.parameters[i] = arg[i]


class InfoTemplate(object):
    def __init__(self, initial_parameters):
        self.parameters = initial_parameters
        self.templates = self.sorted_templates()
        self.samples = self.sample_list()
        self.samples_number = len(self.samples)

    def sorted_templates(self):
        template = self.parameters.get('template_path')
        templates = os.listdir(template)
        return sorted(templates)

    def sample_list(self):
        sample_str = self.parameters.get('sample')
        samples = sample_str.replace(',', ' ').split(' ')
        return samples


class JinjaTemplate(object):
    def __init__(self, initial_parameters, module_sh):
        self.etc = initial_parameters
        self.module_sh = module_sh

    def template(self, **kwargs):
        """
        本函数接受一个路径和一系列参数
        读取模板并渲染返回
        """
        t = env.get_template(self.module_sh)
        return t.render(**kwargs)

    # 开始渲染
    def module(self):
        global env
        # 得到用于加载模板的目录
        path = self.etc['template_path'] + '/'
        # 创建一个加载器, jinja2 会从这个目录中加载模板
        loader = FileSystemLoader(path)
        # 用加载器创建一个环境, 有了它才能读取模板文件
        env = Environment(loader=loader)
        cmd = self.template(etc=self.etc)
        return cmd

    def write_file(self, to_file):
        with open(to_file, 'w') as f:
            f.write(self.cmd)

    def write_shell(self, target):
        target_path, target_sh = target[0], target[1]
        self.cmd = self.module()
        target_file_path = os.path.join(target_path, target_sh)
        self.write_file(target_file_path)

    def write_sample_shell(self, target, value):
        recon_sh = target[1].replace('{}', value)
        new_s_align = (target[0], recon_sh)
        self.write_shell(new_s_align)


class SequenceType(object):
    def __init__(self, initial_parameters):
        self.parameters = initial_parameters

    def extrat_pair_reads(self, seq_name):
        read_1_ls = []
        read_2_ls = []
        for i in seq_name:
            if i != '':
                read_1_ls.append(i.split(',')[0])
                read_2_ls.append(i.split(',')[1])
        return [read_1_ls, read_2_ls]

    def type_seq(self, seq_name):
        seq_name = load_file(seq_name).split('\n')
        for i in seq_name:
            if ',' in i and len(i.split(',')) >= 2:
                if (".fq" in i) or (".fastq" in i) or (".qf" in i):
                    return "pair_reads", self.extrat_pair_reads(seq_name)
            elif 'DRR' in i or 'SRR' in i or 'ERR' in i:
                return 'sra', seq_name
            elif '_inter.fq' in i:
                return 'interleaved', seq_name
            elif ',' not in i and ('.fq' in i or '.fastq' in i):
                return 'single_reads', seq_name

    def choose_seq(self, num):
        etc = self.parameters
        seq_name = etc['seq_pwd']
        seq_type, seq = self.type_seq(seq_name)
        if seq_type == 'pair_reads':
            seq_1_fq = ','.join(seq[0]).split(',')
            seq_2_fq = ','.join(seq[1]).split(',')
            etc['1'] = seq_1_fq[num]
            etc['2'] = seq_2_fq[num]
        else:
            seq_fq = ','.join(seq).split(',')
            type_fq_dict = {
                'single_reads': 'U',
                'sra': 'sra',
                'interleaved': 'I',
            }
            t = type_fq_dict.get(seq_type, None)
            etc[t] = seq_fq[num]
        return etc


class AddBam(InfoTemplate):
    def __init__(self, parameters):
        super().__init__(parameters)

    def has_bam(self):
        bam_file = self.parameters.get('alignment_bam', None)
        if bool(bam_file) is True:
            bam_list = bam_file.split(',')
            if len(bam_list) != self.samples_number:
                raise RaiseException('Failed! Number of bam files don\'t equal samples!')
            else:
                self.parameters['alignment_bam'] = bam_list
            return bam_list
        return False

    def add_bam(self):
        has_bam_value = self.has_bam()
        new_bam_ls = []
        if not has_bam_value:
            for i in self.samples:
                etc = self.parameters
                bam_name = etc['out_dir'] + '/hisat2' + '/%s' % i + '/alignments.sorted.bam'
                new_bam_ls.append(bam_name)
            bam_ls = new_bam_ls
        else:
            bam_ls = has_bam_value
        return bam_ls
