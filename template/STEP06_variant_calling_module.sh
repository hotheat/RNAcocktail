{{etc['template_header']}}


# 06
# Variant calling
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

samtools faidx {{etc['ref_genome_fa']}}

java -jar {{etc['picard']}} CreateSequenceDictionary R={{etc['ref_genome_fa']}} O={{etc['ref_genome_dict']}}

run_rnacocktail.py variant \
 --start {{etc['start']}}\
 --sample {{etc['single_sample']}}\
 --threads {{etc['threads_variant']}}\
  --picard {{etc['picard']}}\
   --gatk {{etc['gatk']}}\
    --outdir {{etc['out_dir']}}\
     --workdir {{etc['work_dir']}}\
      --alignment {{etc['alignment_bam_single']}}\
       --ref_genome {{etc['ref_genome_fa']}}\
        --knownsites {{etc['knownsites']}}\
        --java_opts {{etc['java_opts']}}\
	--IndelRealignment {{etc['IndelRealignment']}}\
          --CleanSam {{etc['CleanSam']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME