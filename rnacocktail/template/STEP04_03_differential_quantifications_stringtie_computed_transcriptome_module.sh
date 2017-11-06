#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 04_03
# reads aligned using HISAT2 on StringTie computed transcriptome (DESeq2)
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py diff --threads {{etc['threads']}}\
  --start {{etc['start']}}\
  --sample {{etc['sample']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --ref_gtf {{etc['ref_gtf']}}\
   --alignments {{etc['alignments']}}\
    --transcripts_gtfs {{etc['transcript_gtfs']}}\
     --featureCounts {{etc['featureCounts']}}\
      --featureCounts_opts {{etc['featureCounts_opts']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME