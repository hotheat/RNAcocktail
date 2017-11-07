# coding:utf-8
from jinja2 import Environment, FileSystemLoader
import json
import os
import time



def log(*args, **kwargs):
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def load_file(path):
    with open(path, 'r') as f:
        read_file = f.read()
    return read_file


def write_file(to_file, cmd):
    with open(to_file, 'w') as f:
        f.write(cmd)


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        log('Succeed to make dictionary {}.'.format(path))
        os.makedirs(path)
        return True
    else:
        log('{} has been existed.'.format(path))
        return False


def update_dict(dict1, dict2):
    dict = dict1.copy()
    dict.update(dict2)
    return dict


def update_dicts(data):
    united_dict = {}
    for k, v in data.items():
        tmp_dict = update_dict(united_dict, v)
        united_dict = tmp_dict
    return united_dict


def extrat_pair_reads(seq_name):
    read_1_ls = []
    read_2_ls = []
    for i in seq_name:
        if i != '':
            read_1_ls.append(i.split(',')[0])
            read_2_ls.append(i.split(',')[1])
    return [read_1_ls, read_2_ls]


def type_seq(seq_name):
    # log('type seq', seq_name)
    seq_name = load_file(seq_name).split('\n')
    # log('seq_ name2', seq_name)
    for i in seq_name:
        if ',' in i and len(i.split(',')) >= 2:
            if ".fq" in i and ".fq" in i:
                return "pair_reads", extrat_pair_reads(seq_name)
        elif 'DRR' in i or 'SRR' in i or 'ERR' in i:
            return 'sra', seq_name
        elif '_inter.fq' in i:
            return 'interleaved', seq_name
        elif ',' not in i and '.fq' in i:
            return 'single_reads', seq_name


def choose_seq(etc, num):
    seq_name = etc['seq_pwd']
    # log('seq name', seq_name)
    seq_type, seq = type_seq(seq_name)
    if seq_type == 'pair_reads':
        seq_1_fq = ','.join(seq[0]).split(',')
        seq_2_fq = ','.join(seq[1]).split(',')
        etc['1'] = seq_1_fq[num]
        etc['2'] = seq_2_fq[num]
    else:
        seq_fq = ','.join(seq).split(',')
        # log('seq_type', seq_type)
        if seq_type == 'single_reads':
            etc['U'] = seq_fq[num]
        elif seq_type == 'sra':
            etc['sra'] = seq_fq[num]
        elif seq_type == 'interleaved':
            etc['I'] = seq_fq[num]
    return etc


def choose_file(etc):
    if etc.get('1') and 'fq.gz' in etc['1']:
        etc['file_format'] = 'fastq.gz'
    if etc.get('U') and 'fq.gz' in etc['U']:
        etc['file_format'] = 'fastq.gz'
    return etc


def sample_info(etc):
    sample_str = etc['sample']
    sample_str = sample_str.replace(',', ' ')
    # log('sample string', sample_str)
    sample_ls = sample_str.split(' ')
    return sample_ls


def has_bam(united_dict):
    bam_file = united_dict.get('alignment_bam')
    if bool(bam_file) == True:
        bam_list = bam_file.split(',')
        if len(bam_list) != sample_num:
            # log('number bam list', len(bam_list), sample_num)
            log('Failed! Number of bam files don\'t equal samples!')
            sys.exit()
        else:
            united_dict['alignment_bam'] = bam_list
        return bam_list
    return False


def add_bam(etc):
    has_bam_value = has_bam(etc)
    new_bam_ls = []
    if not has_bam_value:
        for i in sample_ls:
            bam_name = etc['out_dir'] + '/hisat2' + '/%s' % i + '/alignments.sorted.bam'
            new_bam_ls.append(bam_name)
        bam_ls = new_bam_ls
    else:
        bam_ls = has_bam_value
    return bam_ls


def replace_str(raw_ls, str_format, software_dic):
    for i, v in enumerate(raw_ls):
        for j, k in enumerate(v):
            done_format_str = united_dict['work_dir'] + software_dic + '/%s' % k + '/%s' % str_format
            v[j] = done_format_str
    return raw_ls


def restore_str(raw_ls, str_format, software_dic):
    tmp_ls = []
    raw_ls = replace_str(raw_ls, str_format, software_dic)
    # log("raw list", raw_ls)
    for i, v in enumerate(raw_ls):
        tmp_str = ','.join(v)
        tmp_ls.append(tmp_str)
    restored_str = ' '.join(tmp_ls)
    # log("restored string", restored_str)
    return restored_str


def format_diff_analysis(united_dict, str_format, software_dic):
    sample_name = united_dict['sample']
    space_sp = sample_name.split(' ')
    comma_sp = [i.split(',') for i in space_sp]
    restored_str = restore_str(comma_sp, str_format, software_dic)
    return restored_str


def diff_ana_salmon(diff_mode, united_dict, diff_analy_ls, mkpath):
    diff_ana_salmon_argv = united_dict.copy()
    if not diff_ana_salmon_argv.get('quant_files'):
        restored_str = format_diff_analysis(united_dict, diff_analy_ls[0][2], diff_analy_ls[0][1])
        diff_ana_salmon_argv['quant_files'] = restored_str
    diff_ana_salmon_sh = diff_analy_ls[0][0]
    write_generated_sh(diff_mode, diff_ana_salmon_sh, diff_ana_salmon_argv, mkpath)


def diff_ana_ref_transcpm(diff_mode, united_dict, diff_analy_ls, mkpath):
    diff_ana_ref_transcpm_argv = united_dict.copy()
    if not diff_ana_ref_transcpm_argv.get('alignments'):
        restored_str = format_diff_analysis(united_dict, diff_analy_ls[1][2], diff_analy_ls[1][1])
        diff_ana_ref_transcpm_argv['alignments'] = restored_str
        # log('restored_str', restored_str)
    diff_ana_salmon_sh = diff_analy_ls[1][0]
    # log('reference_dict_alignment', diff_ana_ref_transcpm_argv['alignments'] )
    write_generated_sh(diff_mode, diff_ana_salmon_sh, diff_ana_ref_transcpm_argv, mkpath)
    return diff_ana_ref_transcpm_argv


def diff_ana_cpted_transcpm(diff_mode, united_dict, diff_analy_ls, mkpath):
    diff_ana_cpted_transcpm_argv = united_dict.copy()
    if not united_dict.get('alignments') and \
            not united_dict.get('transcript_gtfs'):
        restored_str_gtf = format_diff_analysis(united_dict, diff_analy_ls[2][2], diff_analy_ls[2][1])
        diff_ana_cpted_transcpm_argv['transcript_gtfs'] = restored_str_gtf
        restored_str_bam = format_diff_analysis(united_dict, diff_analy_ls[1][2], diff_analy_ls[1][1])
        diff_ana_cpted_transcpm_argv['alignments'] = restored_str_bam
    diff_ana_salmon_sh = diff_analy_ls[2][0]
    write_generated_sh(diff_mode, diff_ana_salmon_sh, diff_ana_cpted_transcpm_argv, mkpath)


# 开始渲染
def module(etc, module_sh):
    global env
    # 得到用于加载模板的目录
    path = etc['template_path'] + '/'
    # 创建一个加载器, jinja2 会从这个目录中加载模板
    loader = FileSystemLoader(path)
    # 用加载器创建一个环境, 有了它才能读取模板文件
    env = Environment(loader=loader)
    cmd = template(module_sh, etc=etc)
    return cmd


def template(filename, **kwargs):
    """
    本函数接受一个路径和一系列参数
    读取模板并渲染返回
    """
    # log('filename', filename)
    t = env.get_template(filename)
    return t.render(**kwargs)


def write_generated_sh(module_sh, generated_sh, etc, mkpath):
    # log('etc', etc['threads'])
    cmd = module(etc, module_sh)
    # #log('mkpath', generated_sh)
    to_file_path = os.path.join(mkpath, generated_sh)
    write_file(to_file_path, cmd)


def short_read_alignment(set_index_module, align_module, united_dict, mkpath):
    set_index_sh = 'STEP01_01_Set_index.sh'
    sr_align_argv = united_dict.copy()
    index_dir = sr_align_argv['align_idx']
    mkdir(os.path.dirname(index_dir))
    # log('set index module', set_index_module)
    write_generated_sh(set_index_module, set_index_sh, sr_align_argv, mkpath)
    for i, v in enumerate(sample_ls):
        alignment_args = choose_seq(sr_align_argv, i)
        align_sh = 'STEP01_Align_short_read_%s.sh' % v
        alignment_args['sample'] = v
        write_generated_sh(align_module, align_sh, alignment_args, mkpath)
    return sr_align_argv


def short_read_transcriptome_reconstruction(sr_reconstruc_module, united_dict, mkpath):
    sr_restr_argv = united_dict.copy()
    bam_ls = add_bam(sr_restr_argv)
    for i, v in enumerate(sample_ls):
        sr_restr_argv['alignment_bam'] = bam_ls[i]
        sr_restr_argv['sample'] = v
        reconstc_sh = 'STEP02_short_read_reconstruction_%s.sh' % v
        write_generated_sh(sr_reconstruc_module, reconstc_sh, sr_restr_argv, mkpath)


def alignment_free_quantification(salmon_index_module, quantify_module, united_dict, mkpath):
    set_index_sh = 'STEP03_Salmon_index.sh'
    al_free_quan_args = united_dict.copy()
    # log('set index module', set_index_module)
    write_generated_sh(salmon_index_module, set_index_sh, al_free_quan_args, mkpath)
    for i, v in enumerate(sample_ls):
        al_free_quan_args = choose_seq(al_free_quan_args, i)
        free_quan_sh = 'STEP03_Align_free_transcript_quantification_%s.sh' % v
        al_free_quan_args['sample'] = v
        write_generated_sh(quantify_module, free_quan_sh, al_free_quan_args, mkpath)


def differential_analysis(diff_mode, united_dict, diff_analy_ls, mkpath):
    # log('diff mode', diff_mode)
    if diff_mode == all_templates[5]:
        diff_ana_salmon(diff_mode, united_dict, diff_analy_ls, mkpath)
        return
    if diff_mode == all_templates[6]:
        # log(diff_mode)
        diff_ana_ref_transcpm(diff_mode, united_dict, diff_analy_ls, mkpath)
        return
    if diff_mode == all_templates[7]:
        diff_ana_cpted_transcpm(diff_mode, united_dict, diff_analy_ls, mkpath)


def denovo_assembly(denovo_mode, united_dict, mkpath):
    denovo_asmbl_argv = united_dict.copy()
    for i, v in enumerate(sample_ls):
        denovo_asmbl_argv = choose_seq(denovo_asmbl_argv, i)
        denovo_asmbl_argv = choose_file(denovo_asmbl_argv)
        de_asmbl_sh = 'STEP05_denovo_assembly_%s.sh' % v
        denovo_asmbl_argv['sample'] = v
        write_generated_sh(denovo_mode, de_asmbl_sh, denovo_asmbl_argv, mkpath)


def variant_calling(var_call_mode, united_dict, mkpath):
    var_call_argv = united_dict.copy()
    bam_ls = add_bam(var_call_argv)
    for i, v in enumerate(sample_ls):
        var_call_argv['alignment_bam'] = bam_ls[i]
        var_call_argv['sample'] = v
        var_call_sh = 'STEP06_variant_calling_%s.sh' % v
        write_generated_sh(var_call_mode, var_call_sh, var_call_argv, mkpath)


if __name__ == '__main__':
    # 读取 json 配置文件，并合并所有字典
    data = json.loads(load_file('./configure/configure_file.json'))
    united_dict = update_dicts(data)
    template_dic = united_dict['template_path']
    # 取出/template 路径下所有的模板

    all_templates = os.listdir(template_dic)
    all_templates.sort()

    # 获得样本基本信息
    sample_ls = sample_info(united_dict)
    sample_num = len(sample_ls)

    # 定义 short read alignment 脚本存放的目录，并调用函数，生成脚本
    mkpath_sr_align = "./RNA_pipeline/01_short_read_alignment/"
    mkdir(mkpath_sr_align)
    short_read_alignment(all_templates[0], all_templates[1], united_dict, mkpath_sr_align)

    # 定义 short read transcriptome reconstruction 脚本存放的目录，调用函数，生成脚本
    mkpath_sr_restr = "./RNA_pipeline/02_short_read_reconstruction/"
    mkdir(mkpath_sr_restr)
    short_read_transcriptome_reconstruction(all_templates[2], united_dict, mkpath_sr_restr)

    # 定义 alignment free quantification 脚本存放的目录，调用函数，生成脚本
    mkpath_tr_quant = "./RNA_pipeline/03_alignment_free_transcript_quantification/"
    mkdir(mkpath_tr_quant)
    alignment_free_quantification(all_templates[3], all_templates[4], united_dict, mkpath_tr_quant)

    # 定义 differential analysis 脚本存放目录，调用函数，生成脚本
    mkpath_diff_ana = "./RNA_pipeline/04_differential_analysis/"
    mkdir(mkpath_diff_ana)
    salmon_smem_sh = 'STEP04_01_differential_exp_quantifications_Salmon-SMEM.sh'
    diff_ana_ref_trans = 'STEP04_02_differential_reference_transcriptome.sh'
    diff_ana_cpted_trans = 'STEP04_03_differential_stringtie_computed_transcriptome.sh'
    diff_analy_ls = [
        [salmon_smem_sh, "/salmon_smem", "quant.sf"],
        [diff_ana_ref_trans, '/hisat2', 'alignments.sorted.bam'],
        [diff_ana_cpted_trans, '/stringtie', 'transcripts.gtf']
    ]
    # log("etc bam", etc['alignment_bam'])
    differential_analysis(all_templates[5], united_dict, diff_analy_ls, mkpath_diff_ana)
    differential_analysis(all_templates[6], united_dict, diff_analy_ls, mkpath_diff_ana)
    # log('template02', all_templates[6])
    differential_analysis(all_templates[7], united_dict, diff_analy_ls, mkpath_diff_ana)

    # 定义 denovo assembly 脚本存放目录，调用函数，生成脚本
    mkpath_denovo_asmb = "./RNA_pipeline/05_denovo_assembly/"
    mkdir(mkpath_denovo_asmb)
    denovo_assembly(all_templates[8], united_dict, mkpath_denovo_asmb)

    # 定义 variant calling 脚本存放目录，调用函数，生成脚本
    mkpath_variant_calling = "./RNA_pipeline/06_variant_calling/"
    mkdir(mkpath_variant_calling)
    variant_calling(all_templates[9], united_dict, mkpath_variant_calling)
