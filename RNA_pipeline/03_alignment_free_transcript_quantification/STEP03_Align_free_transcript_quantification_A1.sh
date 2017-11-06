#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 03_02
# alignment-free transcript quantification
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py quantify --quantifier_idx /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/example/Homo_sapiens.GRCh37.75.cdna.21.Salmon.fmd\
 --threads 4\
 --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
 --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
   --1 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/A1_1.fq.gz\
    --2 /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/A1_2.fq.gz\
     --U ""\
       --libtype A\
        --sample A1\
         --unzip \
          --salmon salmon\
           --salmon_smem_opts ''

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME