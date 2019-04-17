from models.model import JinjaTemplate
from models.model import InfoTemplate
from models.model import SequenceType
from tools.utils import *


class DenovoAssembly(InfoTemplate):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.deno_assem_para = self.parameters

    def add_file_format(self):
        etc = self.deno_assem_para
        if etc.get('1') and 'fq.gz' in etc['1']:
            etc['file_format'] = 'fastq.gz'
        if etc.get('U') and 'fq.gz' in etc['U']:
            etc['file_format'] = 'fastq.gz'
        self.deno_assem_para = etc

    def assembly(self, de_am):
        assem_module = JinjaTemplate(self.deno_assem_para, self.templates[8])
        st = SequenceType(self.deno_assem_para)
        mkdir(de_am[0])
        for num, value in enumerate(self.samples):
            self.deno_assem_para = st.choose_seq(num)
            self.add_file_format()
            self.deno_assem_para['sample'] = value
            assem_module.write_sample_shell(de_am, value)
