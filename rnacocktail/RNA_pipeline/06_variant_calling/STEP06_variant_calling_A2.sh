#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 06
# Variant calling
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

samtools faidx /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/example_small/Homo_sapiens.GRCh37.75.dna.chromosome.21.fa

java -jar /hwfssz1/ST_OCEAN/USER/guojiao1/guojiao/software/picard-tools-2.2.2/picard.jar CreateSequenceDictionary R=/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/example_small/Homo_sapiens.GRCh37.75.dna.chromosome.21.fa O=/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/example_small/Homo_sapiens.GRCh37.75.cdna.all.dict

run_rnacocktail.py variant \
 --sample A2\
 --threads 5\
  --picard /hwfssz1/ST_OCEAN/USER/guojiao1/guojiao/software/picard-tools-2.2.2/picard.jar\
   --gatk /hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/opt/gatk-3.5/GenomeAnalysisTK.jar\
    --outdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out\
     --workdir /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/work\
      --alignment /hwfssz1/ST_OCEAN/USER/guojiao1/Project/RNAcocktail_test/out/hisat2/A2/alignments.sorted.bam\
       --ref_genome /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/test/example_small/Homo_sapiens.GRCh37.75.dna.chromosome.21.fa\
        --knownsites /hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/shell_scripts/Ex1_alignment_of_paired_short_reads/work_dir/example/variants_21.vcf\
        --java_opts "-Xms40g -Xmx40g"\
	--IndelRealignment \
          --CleanSam 

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME