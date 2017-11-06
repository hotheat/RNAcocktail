#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 02
# Short read transcriptome reconstruction

run_rnacocktail.py reconstruct --alignment_bam /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out/hisat2/A2/alignments.sorted.bam\
 --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
 --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
 --threads 5\
  --ref_gtf /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/example_small/Homo_sapiens.GRCh37.75.gtf\
   --sample A2\
    --stringtie stringtie\
     --stringtie_opts ''

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME