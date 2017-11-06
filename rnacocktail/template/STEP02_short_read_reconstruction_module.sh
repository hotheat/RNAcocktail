#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 02
# Short read transcriptome reconstruction

run_rnacocktail.py reconstruct --alignment_bam {{etc['alignment_bam']}}\
  --start {{etc['start']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --threads {{etc['threads']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --sample {{etc['sample']}}\
    --stringtie {{etc['stringtie']}}\
     --stringtie_opts {{etc['stringtie_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME