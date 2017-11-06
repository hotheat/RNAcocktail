#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME
# 03_01
# generate salmon index of transcriptome genome
salmon index -t {{etc['transcriptome_fa']}} -i {{etc['quantifier_idx']}}\
 --type {{etc['idx_type']}} --threads {{etc['threads_salmon']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
