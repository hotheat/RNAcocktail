#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 03_01
# generate salmon index of transcriptome genome
salmon index -t /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/example_small/Homo_sapiens.GRCh37.75.cdna.all.fa -i /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/example/Homo_sapiens.GRCh37.75.cdna.21.Salmon.fmd\
 --type fmd --threads 4

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME