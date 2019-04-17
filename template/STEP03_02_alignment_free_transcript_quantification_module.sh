{{etc['template_header']}}

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
        --sample {{etc['single_sample']}}\
         --unzip {{etc['unzip']}}\
          --salmon {{etc['salmon']}}\
           --salmon_smem_opts {{etc['salmon_smem_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME