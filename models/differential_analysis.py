from models.model import JinjaTemplate
from models.model import InfoTemplate
from tools.utils import *


class DifferentAnalysis(InfoTemplate):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.comput_trans_para = self.parameters
        self.inputs = {
            'STEP04_01_differential_exp_quantifications_Salmon-SMEM.sh': ["/salmon_smem", "quant.sf"],
            'STEP04_02_differential_reference_transcriptome.sh': ['/hisat2', 'alignments.sorted.bam'],
            'STEP04_03_differential_stringtie_computed_transcriptome.sh': ['/stringtie', 'transcripts.gtf'],
        }

    def replace_str(self, comma_sp, *args):
        for i, v in enumerate(comma_sp):
            for j, k in enumerate(v):
                done_format_str = self.comput_trans_para['work_dir'] + args[0][0] + '/%s' % k + '/%s' % args[0][1]
                v[j] = done_format_str
        return comma_sp

    def restore_str(self, comma_sp, *args):
        tmp_ls = []
        raw_ls = self.replace_str(comma_sp, *args)
        for i, v in enumerate(raw_ls):
            tmp_str = ','.join(v)
            tmp_ls.append(tmp_str)
        restored_str = ' '.join(tmp_ls)
        return restored_str

    def format_diff_analysis(self, *args):
        sample_name = self.comput_trans_para['sample']
        space_sp = sample_name.split(' ')
        comma_sp = [i.split(',') for i in space_sp]
        restored_str = self.restore_str(comma_sp, *args)
        return restored_str

    def add_restored_str(self, diff, name):
        if not self.comput_trans_para.get(name):
            restored_str = self.format_diff_analysis(self.inputs.get(diff[1]))
            self.comput_trans_para[name] = restored_str

    def total_diff_ana(self, diff, name, temp_i):
        diff_ana = JinjaTemplate(self.comput_trans_para, self.templates[temp_i])
        mkdir(diff[0])
        self.add_restored_str(diff, name)
        diff_ana.write_shell(diff)

    def salmon(self, salmon_diff):
        self.total_diff_ana(salmon_diff, 'quant_files', 5)

    def ref_transcpm(self, ref_transcpm_diff):
        self.total_diff_ana(ref_transcpm_diff, 'alignments', 6)

    def comput_transcpm(self, *transcpt):
        comput_transcpm_diff, ref_transcpm_diff = transcpt[0][0], transcpt[0][1]
        cpt_tra_ana = JinjaTemplate(self.comput_trans_para, self.templates[7])
        mkdir(comput_transcpm_diff[0])
        # self.ref_transcpm() 会使 self.comput_trans_para 拥有 key 值 ['alignments']
        if not self.comput_trans_para.get('alignments') or \
                not self.comput_trans_para.get('transcript_gtfs'):
            self.add_restored_str(comput_transcpm_diff, 'transcript_gtfs')
            self.add_restored_str(ref_transcpm_diff, 'alignments')
        # 可以用装饰器判断 alignments 是否符合格式要求
        cpt_tra_ana.write_shell(comput_transcpm_diff)
