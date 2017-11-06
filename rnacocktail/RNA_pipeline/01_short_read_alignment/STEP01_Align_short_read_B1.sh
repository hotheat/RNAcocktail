#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

# 01_02
# alignment of RNA data by index

run_rnacocktail.py align --align_idx /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/example/Homo_sapiens.GRCh37.75.dna.chromosome.21.HISAT2\
 --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
 --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
 --threads 5\
  --ref_gtf /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/example_small/Homo_sapiens.GRCh37.75.gtf\
   --1 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/B1_1.fq.gz\
    --2 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/B1_2.fq.gz\
     --U ""\
      --sra ""\
       --sample B1\
        --hisat2_opts ''

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME