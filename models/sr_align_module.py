from models.model import JinjaTemplate
from models.model import InfoTemplate
from models.model import SequenceType
from tools.utils import *


class ShortReadAlign(InfoTemplate):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.sr_align_para = self.parameters

    def index_shell(self, sr_align_index):
        align_index_module = JinjaTemplate(self.sr_align_para, self.templates[0])
        mkdir(sr_align_index[0])
        align_index_module.write_shell(sr_align_index)

    def align_shell(self, sr_align):
        align_module = JinjaTemplate(self.sr_align_para, self.templates[1])
        st = SequenceType(self.sr_align_para)
        mkdir(sr_align[0])

        for num, value in enumerate(self.samples):
            self.sr_align_para = st.choose_seq(num)
            self.sr_align_para['single_sample'] = value
            align_module.write_sample_shell(sr_align, value)
