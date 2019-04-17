{{etc['template_header']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"` 
echo 'Start at' $CURTIME
# 01_01
# generate index of genome
hisat2-build {{etc['ref_genome_fa']}} {{etc['align_idx']}}  -p {{etc['threads']}} {{etc['large_idx']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
