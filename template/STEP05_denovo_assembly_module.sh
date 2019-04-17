{{etc['template_header']}}


CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'Start at' $CURTIME

# 05
# Denovo assembly

run_rnacocktail.py denovo --threads {{etc['threads']}}\
  --start {{etc['start']}}\
  --sample {{etc['sample']}}\
  --outdir {{etc['out_dir']}}\
  --workdir {{etc['work_dir']}}\
  --1 {{etc['1']}}\
   --2 {{etc['2']}}\
    --U {{etc['U']}}\
     --I {{etc['I']}}\
      --assmebly_hash {{etc['assembly_hash']}}\
       --file_format {{etc['file_format']}}\
        --read_type {{etc['read_type']}}\
         --oases_opts {{etc['oases_opts']}}\
          --velvetg_opts {{etc['velvetg_opts']}}\
            --velveth_opts {{etc['velveth_opts']}}

CURTIME=`date +"%Y-%m-%d %H:%M:%S"`
echo 'End at' $CURTIME

