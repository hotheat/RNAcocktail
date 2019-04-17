from routes.routes import *
from models.model import *
from tools.utils import *

out_shell_dir = './RNA_pipeline'

target_file = {
    'sr_align_index': ['{}/01_short_read_alignment/'.format(out_shell_dir),
                       'STEP01_01_Set_index.sh'],

    'sr_align': ['{}/01_short_read_alignment/'.format(out_shell_dir),
                 'STEP01_02_Align_short_read_{}.sh'],

    'sr_reconstruct': ['{}/02_short_read_reconstruction/'.format(out_shell_dir),
                       'STEP02_short_read_reconstruction_{}.sh'],

    'align_free_quant': ['{}/03_alignment_free_transcript_quantification/'.format(out_shell_dir),
                         'STEP03_01_Align_free_transcript_quantification_index.sh'],

    'free_quant_align': ['{}/03_alignment_free_transcript_quantification/'.format(out_shell_dir),
                         'STEP03_02_Align_free_transcript_quantification_{}.sh'],

    'diff_analy_salmon': ['{}/04_differential_analysis/'.format(out_shell_dir),
                          'STEP04_01_differential_exp_quantifications_Salmon-SMEM.sh'],

    'diff_analy_ref_transcpm': ['{}/04_differential_analysis/'.format(out_shell_dir),
                                'STEP04_02_differential_reference_transcriptome.sh'],

    'diff_analy_cmpt_transcpm': [
        ['{}/04_differential_analysis/'.format(out_shell_dir),
         'STEP04_03_differential_stringtie_computed_transcriptome.sh'
         ],
        ['{}/04_differential_analysis/'.format(out_shell_dir),
         'STEP04_02_differential_reference_transcriptome.sh',
         ]
    ],

    'denovo_assembly': [
        '{}/05_denovo_assembly/'.format(out_shell_dir),
        'STEP05_denovo_assembly_{}.sh'
    ],

    'variant_calling': [
        '{}/06_variant_calling/'.format(out_shell_dir),
        'STEP06_variant_calling_{}.sh'
    ]

}


def initialization():
    _ = get_arg()
    general_para = './configure/general_parameters.json'
    advance_para = './configure/advanced_parameters.json'
    gene_json = ToJson(general_para)
    advan_json = ToJson(advance_para)
    gene = gene_json.joined_dictionary()
    advan = advan_json.joined_dictionary()
    gene.update(advan)
    parameters = gene
    template_initial = InitializeArguments(parameters)
    return template_initial


def main():
    initialize = initialization()
    initial_parameters = initialize.parameters
    route = Route(initial_parameters)
    route.sr_align_index(target_file)
    route.sr_align(target_file)
    route.sr_reconstruct(target_file)
    route.free_quant_index(target_file)
    route.free_quant_align(target_file)
    route.diff_analy_salmon(target_file)
    route.diff_analy_ref_transcpm(target_file)
    route.diff_analy_cmpt_transcpm(target_file)
    route.denovo_assem(target_file)
    route.variant_calling(target_file)
    log('Work Completed!')


if __name__ == '__main__':
    main()
