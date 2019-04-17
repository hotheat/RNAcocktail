{{etc['template_header']}}


# 04_02
# reads aligned using HISAT2 on reference transcriptome (DESeq2)
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py diff --threads {{etc['threads']}}\
 --start {{etc['start']}}\
 --sample {{etc['sample']}}\
 --outdir {{etc['out_dir']}}\
 --workdir {{etc['work_dir']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --alignments {{etc['alignments']}}\
   --R {{etc['R']}}\


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME