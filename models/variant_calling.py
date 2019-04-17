from models.model import JinjaTemplate
from models.model import AddBam
from tools.utils import *


class CallVariantRNA(AddBam):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.call_variant_para = self.parameters

    def var_call(self, var_call_path):
        bam_ls = self.add_bam()
        recon_module = JinjaTemplate(self.call_variant_para, self.templates[9])
        mkdir(var_call_path[0])
        for num, value in enumerate(self.samples):
            self.call_variant_para['alignment_bam_single'] = bam_ls[num]
            self.call_variant_para['single_sample'] = value
            recon_module.write_sample_shell(var_call_path, value)
