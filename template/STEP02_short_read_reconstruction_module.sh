{{etc['template_header']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 02
# Short read transcriptome reconstruction

run_rnacocktail.py reconstruct --alignment_bam {{etc['alignment_bam_single']}}\
  --start {{etc['start']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --threads {{etc['threads']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --sample {{etc['single_sample']}}\
    --stringtie {{etc['stringtie']}}\
     --stringtie_opts {{etc['stringtie_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME