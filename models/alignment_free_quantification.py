from models.model import JinjaTemplate
from models.model import InfoTemplate
from models.model import SequenceType
from tools.utils import *


class AlignFreeQuantification(InfoTemplate):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.align_free_quant = self.parameters

    def index_shell(self, free_align_index):
        free_align_module = JinjaTemplate(self.align_free_quant, self.templates[3])
        mkdir(free_align_index[0])
        free_align_module.write_shell(free_align_index)

    def align_shell(self, free_align):
        free_al_module = JinjaTemplate(self.align_free_quant, self.templates[4])
        st = SequenceType(self.align_free_quant)
        mkdir(free_align[0])
        for num, value in enumerate(self.samples):
            self.align_free_quant = st.choose_seq(num)
            self.align_free_quant['single_sample'] = value
            free_al_module.write_sample_shell(free_align, value)
