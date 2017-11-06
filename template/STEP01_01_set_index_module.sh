#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/:/ifs4/BC_NGS/USER/liuwq/Zhaoyong/share_software/Java/jre1.8.0_73/bin/:"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

CURTIME=`date +"%Y-%m-%d %H:%M:%S"` 
echo 'Start at' $CURTIME
# 01_01
# generate index of genome
hisat2-build {{etc['ref_genome_fa']}} {{etc['align_idx']}}  -p {{etc['threads']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME
