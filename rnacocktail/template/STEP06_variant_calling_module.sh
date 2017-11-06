#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 06
# Variant calling
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

samtools faidx {{etc['ref_genome_fa']}}

java -jar {{etc['picard']}} CreateSequenceDictionary R={{etc['ref_genome_fa']}} O={{etc['ref_genome_dict']}}

run_rnacocktail.py variant \
 --start {{etc['start']}}\
 --sample {{etc['sample']}}\
 --threads {{etc['threads_variant']}}\
  --picard {{etc['picard']}}\
   --gatk {{etc['gatk']}}\
    --outdir {{etc['out_dir']}}\
     --workdir {{etc['work_dir']}}\
      --alignment {{etc['alignment_bam']}}\
       --ref_genome {{etc['ref_genome_fa']}}\
        --knownsites {{etc['knownsites']}}\
        --java_opts {{etc['java_opts']}}\
	--IndelRealignment {{etc['IndelRealignment']}}\
          --CleanSam {{etc['CleanSam']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME