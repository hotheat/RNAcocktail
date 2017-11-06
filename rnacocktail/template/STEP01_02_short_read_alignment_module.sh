#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

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
       --sample {{etc['sample']}}\
        --hisat2_opts {{etc['hisat2_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
