# RNAcocktail 2.0 流程使用说明
此流程是 2017.07 发表在 NC 上的 RNA-seq 流程.  
RNAcocktail 2.0 重新对二代测序的 alignment, transcriptome reconstruction, denovo transcriptome assembly, alignment-free quantification, differential expression analysis, variant calling 进行封装， 并用 conda 进行环境管理。

Publication

> If you use RNACocktail in your work, please cite the following:  
Sayed Mohammad Ebrahim Sahraeian, Marghoob Mohiyuddin, Robert Sebra, Hagen Tilgner, Pegah T. Afshar, Kin Fai Au, Narges Bani Asadi, Mark B. Gerstein, Wing Hung Wong, Michael P. Snyder, Eric Schadt, and Hugo Y. K. Lam  
__Gaining comprehensive biological insight into the transcriptome by performing a broad-spectrum RNA-seq analysis__
Nature Communications 8, Article number: 59 (2017). doi:10.1038/s41467-017-00050-4


## 流程工具及输出文件

|               short read         |    Tools    | Output files |
| :------------------------------: | :---------: | :----------: |
|          alignment               |    HISAT2   | __alignments__: alignments.sorted.bam<br> __junctions__: splicesites.tab |
| transcriptome reconstruction     |   StringTie | __trasncripts__: transcripts.gtf<br>__expressions__: gene_abund.tab  |
| denovo transcriptome assembly    |   Oases     | __trasncripts__: transcripts.fa |
| alignment-free quantification    | Salmon-SMEM | __expressions__: quant.sf|
| differential expression analysis |  DESeq2     | __differential expressions__: deseq2_res.tab
|       variant calling            |   GATK      | __variants__: variants_filtered.vcf |

## 使用说明

1. 将 */USER/guojiao1/Project/RNAcocktail_test/rnacocktail/ ( 以下称 ./ ) 拷贝至自己的工作目录中
2. 在 ./configure/configure_file.json 中配置不同步骤相应的参数
3. 在 ./configure/seq.txt 中配置 reads 路径
4. 运行 ``` sh template.sh``` 将在 ./RNA_pipeline/ 中 分别生成 6 个对应目录
    - 01_short_read_alignment/  (qsub -cwd -l vf=25g -q st.q -P P17Z10200N0003 -l num_proc=3 )
    - 02_short_read_reconstruction/  (qsub -cwd -l vf=5g -q st.q -P P17Z10200N0003 -l num_proc=3) 
    - 03_alignment_free_transcript_quantification/
    - 04_differential_analysis/
    - 05_denovo_assembly/ (根据基因组大小而定，基因组超过 2G 时, 峰值内存 200 G)
    - 06_variant_calling/
5. 可以在 ./runlog 分别对应的目录中投递任务

## configure 目录说明

1. ./configure/  
    configure 目录中共有 3 个文件：conda_rnacock_simple.txt, seq_name.txt, configure_file.json

    - conda_rnacock_simple.txt  
    含有流程中环境 rnacock_2 用到的主要软件，不需要改动。  
    如需重新搭建，使用  
    ```conda install --file ./configure/conda_rnacock_simple.txt ```  
    为避免冲突，建议新建一个环境单独安装 R 包 (conda create -n r_test bioconductor-deseq2 r-readr bioconductor-tximport)
    - seq.name.txt  
    支持 PE , SE reads 及 SRA accession numbers (DRR/SSR/ERR)输入，不同样本以换行符分隔,  
    PE reads: _1.fastq.gz 和 _2.fastq.gz 以 , 分隔。  
    - configure.json  
    json 文件说明, 见[链接]( http://www.w3school.com.cn/json/json_syntax.asp ) (字符串使用 "..."， {...} 内最后一个元素不能加",")
## configure.json 参数说明
- General_Arguement (流程中通用参数)  
需要设置的参数:  
1. sample 
样品编号  
例 "A1,A2 B1,B2"  A, B 代表不同样品, A1, A2 为重复样本  
若没有重复样本，则以空格分隔
2. threads  
Number of threads to use (默认为 3)
3. start  
从流程中某一步开始运行(默认为 0)
4. work_dir  
结果目录及其他文件目录(可写入)
5. out_dir  
结果文件目录(可写入)

- Short_Read_Alignment
1. ref_genome_fa  
参考基因组
2. align_idx  
index 目录
3. ref_gtf  
参考基因组 .gtf 文件, 若无，此项设为 ''  
4. hisat2_sps  
若没有 ref_gtf, 此项设为 ''
- Short_Read_Transcriptome_Reconstruction  
无需设置，参数自动生成，如需更改 stringtie 参数，请在 stringtie_opts 中添加
- Alignment_free_quantification
1. threads_salmon  
salmon 运行 threads 数量，至少设为 4
2. transcriptome_fa  
参考转录组 fa 文件
3. quantifier_idx  
salmon index 索引位置
4. salmon_k  
SMEM's smaller than this size will not be considered by Salmon. (default 19).  
5. libtype  
Format string describing the library type. (For Salmon check [here](http://salmon.readthedocs.io/en/latest/library_type.html#fraglibtype))  
- Differential_Analysis
1. mincount  
Minimum read counts per transcripts. Differential analysis pre-filtering step removes transcripts that have less than this number of reads. (default 2)  
2. alpha_float  
Adjusted p-value significance level for differential analysis. (default 0.05)  
- De_novo_assembly
1. assembly_hash  
Odd integer, or a comma separated list of odd integers that specify the assembly has length (for Oases/Velvet).  
2. read_type  
Input sequence read type for de novo assembly Options: __short__, __shortPaired__, __short2, __shortPaired2__, __long__, __longPaired__, reference. (Check here for [description](https://www.ebi.ac.uk/~zerbino/velvet/Manual.pdf)) (default short)
3. file_format  
Input file format for de novo assembly Options: fasta, fastq, raw, fasta.gz, fastq.gz, raw.gz, sam, bam, fmtAuto. (default fasta)
- Variant Calling
1. knownsites  
A database of known polymorphic sites (e.g. dbSNP). Used in GATK BaseRecalibrator and RealignerTargetCreator. NOTE: to run BaseRecalibrator step knownsites should be provided.
2. ref_genome_dict  
将 ref_genome_fa 格式 *.fa 中 (.fa) 替换为 (.dict).

其他参数设置详见[流程网址](https://bioinform.github.io/rnacocktail/)

- Template_configure
模版配置参数，无需改动!
1. template_path
模版路径
2. template_header
shell header






    




