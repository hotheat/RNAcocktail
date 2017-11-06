#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 04_01
# differential expression analysis of quantifications computed using Salmon-SMEM
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py diff --threads 5\
 --sample A1,A2 B1,B2\
 --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
 --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
  --ref_gtf /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/example_small/Homo_sapiens.GRCh37.75.gtf\
   --quant_files /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work/salmon_smem/A1/quant.sf,/hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work/salmon_smem/A2/quant.sf /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work/salmon_smem/B1/quant.sf,/hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work/salmon_smem/B2/quant.sf


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME