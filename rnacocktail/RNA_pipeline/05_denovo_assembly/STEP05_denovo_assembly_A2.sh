#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

# 05
# Denovo assembly

run_rnacocktail.py denovo --threads 5\
 --sample A2\
 --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
 --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
  --1 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/A2_1.fq.gz\
   --2 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/A2_2.fq.gz\
    --U ""\
     --I ""\
      --assmebly_hash 25\
       --file_format fastq.gz\
        --read_type short

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
