#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

# 05
# Denovo assembly

run_rnacocktail.py denovo --threads {{etc['threads']}}\
  --start {{etc['start']}}\
  --sample {{etc['sample']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --1 {{etc['1']}}\
   --2 {{etc['2']}}\
    --U {{etc['U']}}\
     --I {{etc['I']}}\
      --sra {{etc['sra']}}\
      --assmebly_hash {{etc['assembly_hash']}}\
       --file_format {{etc['file_format']}}\
        --read_type {{etc['read_type']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME

