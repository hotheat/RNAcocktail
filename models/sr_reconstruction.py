from models.model import JinjaTemplate
from models.model import AddBam
from tools.utils import *


class ShortReadReconstruct(AddBam):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.sr_recon_para = self.parameters

    def sr_construct(self, reconstruct):
        bam_ls = self.add_bam()
        recon_module = JinjaTemplate(self.sr_recon_para, self.templates[2])
        mkdir(reconstruct[0])
        for num, value in enumerate(self.samples):
            self.sr_recon_para['alignment_bam_single'] = bam_ls[num]
            self.sr_recon_para['single_sample'] = value
            recon_module.write_sample_shell(reconstruct, value)


