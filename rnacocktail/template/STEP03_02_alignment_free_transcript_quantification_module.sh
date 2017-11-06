#!/bin/bash
export PATH="/usr/sbin:/sbin:/usr/bin:/bin:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/bin/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1/scripts/:/hwfssz1/ST_OCEAN/USER/guojiao1/app/miniconda/envs/r-test/bin/"
export PYTHONPATH="/hwfssz1/ST_OCEAN/USER/guojiao1/app/rnacocktail-0.2.1:"
export LD_LIBRARY_PATH="/share/app/gcc-5.2.0/lib64:"
source activate rnacock_2

# 03_02
# alignment-free transcript quantification
CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

run_rnacocktail.py quantify --quantifier_idx {{etc['quantifier_idx']}}\
 --start {{etc['start']}}\
 --threads {{etc['threads_salmon']}}\
 --outdir {{etc['out_dir']}}\
 --workdir {{etc['work_dir']}}\
   --1 {{etc['1']}}\
    --2 {{etc['2']}}\
     --U {{etc['U']}}\
       --libtype {{etc['libtype']}}\
        --sample {{etc['sample']}}\
         --unzip {{etc['unzip']}}\
          --salmon {{etc['salmon']}}\
           --salmon_smem_opts {{etc['salmon_smem_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME