{{etc['template_header']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 03_01
# generate salmon index of transcriptome genome
salmon index -t {{etc['transcriptome_fa']}} -i {{etc['quantifier_idx']}}\
 --type {{etc['idx_type']}} --threads {{etc['threads_salmon']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
