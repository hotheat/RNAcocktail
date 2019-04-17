{{etc['template_header']}}


# 04_01
# differential expression analysis of quantifications computed using Salmon-SMEM
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py diff --threads {{etc['threads']}}\
  --start {{etc['start']}}\
  --sample {{etc['sample']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --quant_files {{etc['quant_files']}}\
   --R {{etc['R']}}\


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME