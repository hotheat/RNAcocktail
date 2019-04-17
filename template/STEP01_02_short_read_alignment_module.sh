{{etc['template_header']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

# 01_02
# alignment of RNA data by index

run_rnacocktail.py align --align_idx {{etc['align_idx']}}\
 --start {{etc['start']}}\
 --outdir {{etc['out_dir']}}\
 --workdir {{etc['work_dir']}}\
 --threads {{etc['threads']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --1 {{etc['1']}}\
    --2 {{etc['2']}}\
     --U {{etc['U']}}\
      --sra {{etc['sra']}}\
       --sample {{etc['single_sample']}}\
        --hisat2_opts {{etc['hisat2_opts']}}\
          --large_genome {{etc['large_genome']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
