from models.sr_align_module import ShortReadAlign
from models.sr_reconstruction import ShortReadReconstruct
from models.alignment_free_quantification import AlignFreeQuantification
from models.differential_analysis import DifferentAnalysis
from models.denovo_assembly import DenovoAssembly
from models.variant_calling import CallVariantRNA


class Route():
    def __init__(self, initial_parameters):
        self.sr_alignment = ShortReadAlign(initial_parameters)
        self.sr_reconstruction = ShortReadReconstruct(initial_parameters)
        self.align_free_quant = AlignFreeQuantification(initial_parameters)
        self.diff = DifferentAnalysis(initial_parameters)
        self.de_as = DenovoAssembly(initial_parameters)
        self.var_ca = CallVariantRNA(initial_parameters)

    def sr_align_index(self, target_file):
        sr_a_i = target_file.get('sr_align_index')
        self.sr_alignment.index_shell(sr_a_i)

    def sr_align(self, target_file):
        sr_a = target_file.get('sr_align')
        self.sr_alignment.align_shell(sr_a)

    def sr_reconstruct(self, target_file):
        sr_r = target_file.get('sr_reconstruct')
        self.sr_reconstruction.sr_construct(sr_r)

    def free_quant_index(self, target_file):
        fr_q_i = target_file.get('align_free_quant')
        self.align_free_quant.index_shell(fr_q_i)

    def free_quant_align(self, target_file):
        fr_q_a = target_file.get('free_quant_align')
        self.align_free_quant.align_shell(fr_q_a)

    def diff_analy_salmon(self, target_file):
        di_ana_s = target_file.get('diff_analy_salmon')
        self.diff.salmon(di_ana_s)

    def diff_analy_ref_transcpm(self, target_file):
        di_ana_s = target_file.get('diff_analy_ref_transcpm')
        self.diff.ref_transcpm(di_ana_s)

    def diff_analy_cmpt_transcpm(self, target_file):
        di_ana_s = target_file.get('diff_analy_cmpt_transcpm')
        self.diff.comput_transcpm(di_ana_s)

    def denovo_assem(self, target_file):
        d_a = target_file.get('denovo_assembly')
        self.de_as.assembly(d_a)

    def variant_calling(self, target_file):
        var_ca = target_file.get('variant_calling')
        self.var_ca.var_call(var_ca)
