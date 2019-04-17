{{etc['template_header']}}


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
      --featureCounts_opts {{etc['featureCounts_opts']}}\
      --R {{etc['R']}}\


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME