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

SZ 集群：*/USER/guojiao1/Project/RNAcocktail_test/rnacocktail/( 以下称 ./ )  
QD 集群：*/USRS/guojiao1/pipeline/rnacocktail/RNAcocktail_test/rnacocktail/( 以下称 ./ )  
1. 将 ./configure 和 ./template.sh 拷贝至自己的工作目录中  
2. 在 ./configure/general_parameters.json 中配置基本参数 (如有其他参数需求, 请在 advanced_parameters.json 中设置)  
3. 在 ./configure/seq.txt 中配置 reads 路径
4. 运行 ``` sh template.sh``` 将在 ./RNA_pipeline/ 中 分别生成 6 个对应目录
    - 01_short_read_alignment/  (vf=25g)
    - 02_short_read_reconstruction/  (vf=5g) 
    - 03_alignment_free_transcript_quantification/
    - 04_differential_analysis/
    - 05_denovo_assembly/ ( 峰值内存大小与转录组数据有关 )
    - 06_variant_calling/
5. 可以新建在 ./runlog 分别对应的目录中投递任务

|     内容         |    方法 1    | 方法 2 |
| :--------------: | :---------: | :----------: |
|     转录本定量    |    01-02 (stringtie)   | 03 (salmon) |
|      差异表达     |   01-02-04 (stringtie)<br>根据是否有参考基因组 ref_gtf 选择 /STEP04_02(有) 及 /STEP04_03(无) | 03-04(/STEP04_01)<br>需要 ref_gtf   |
|     转录本组装    |   01-02 (stringtie)<br>有参组装     | 05 (oases)<br>无参组装 |
|   Call variant   | 01-02-06 (GATK) | -|

## configure 目录说明

configure 目录中共有 4 个文件：general_parameters.json, advanced_parameters.json, seq_name.txt, conda_rnacock_simple.txt

- general_parameters.json —— 基本参数设置  

- advanced_parameters.json —— 高级参数设置  

- seq.name.txt —— reads 目录  
支持 PE , SE reads 及 SRA accession numbers (DRR/SSR/ERR)输入，不同样本以换行符分隔,  
PE reads: _1.fastq.gz 和 _2.fastq.gz 以 , 分隔。  

- conda_rnacock_simple.txt （搭建流程用）  
含有流程中环境 rnacock_2 用到的主要软件，不需要改动。  
如需重新搭建，使用  
```conda env create -n rnacock_2 --file ./configure/conda_rnacock_simple.txt ```  
为避免冲突，建议新建一个环境单独安装 R 包 (conda create -n r-test bioconductor-deseq2=1.16.1 r-readr bioconductor-tximport)

    
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


- Short_Read_Alignment
1. ref_genome_fa  
参考基因组
2. align_idx  
index 目录
3. ref_gtf  
参考基因组 .gtf 文件, 若无, 此项设为 "''"  
4. hisat2_sps  
若没有 ref_gtf, 此项设为 "''"
- Short_Read_Transcriptome_Reconstruction  
1. stringtie_opts  
stringtie 参数
- Alignment_free_quantification
1. threads_salmon  
salmon 运行 threads 数量，至少设为 4
2. transcriptome_fa  
参考转录组 fa 文件, 若无, 此项设为 "''"  
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

其他参数设置详见[流程网址](https://bioinform.github.io/rnacocktail/)

- Template_configure
模版配置参数，无需改动!
1. template_path  
模版路径
2. template_header:  
shell header

#  输出结果说明

1. hisat2
    - alignments.sorted.bam 经过排序的 bam 文件
    - splicesites.tab hisat2 的剪切位点信息 (包括根据参考基因组 ref_gtf 得到的剪切位点)
    - splicesites.bed 经 hisat2_jun2bed.py 将剪切位点转换成 bed 文件
2. stringtie
    - transcripts.gtf 基因注释文件
    - gene_abund.tab stringtie -A 生成基因丰度文件
3. salmon_smem
    - quant.sf  
        (1) Name：提供的目标转录本 ID  
        (2) Length: 目标转录本长度  
        (3) EffectiveLength: 目标转录本有效长度，考虑了插入片段长度分布和序列特异性等  
        (4) TPM: transcripts per million，TPM 计算公式中分母是总转录本数量的统计量，而 FPKM 和 RPKM 分母仅仅代表测序深度的变化  
        (5) Numreads: map 到每个转录本的 reads 数量
4. deseq2
    - deseq2_res.tab  
        (1) rownames: 基因 ID  
        (2) baseMean: 样本矫正后的平均 reads 数  
        (3) log2FoldChange: 表达量差异取 log2 后的值  
        (4) lfcSE: standard error: condition treated vs untreated  
        (5) stat: Wald statistic Wald 检验统计量  
        (6) pvalue: 统计学差异显著性检验指标  
        (7) padj: 校正后的 pvalue, padj 越小,表示基因表达差异越显著
5. oases
    - transcripts.fa 无参组装的转录本



#  注意事项

1. json 文件说明, 见[链接]( http://www.w3school.com.cn/json/json_syntax.asp ) (字符串使用 双引号("")， {...} 内最后一个元素不能加",").

2. 除特殊情况外，只进行基本参数设置即可.

3. Hisat 比对默认索引文件默认在 general_parameters.json 中的 ref_genome_fa 目录中生成， 也可以在 advanced_parameters.json 中配置.


4. salmon 比对默认索引文件默认在 general_parameters.json 中的 transcriptome_fa 目录中生成，也可以在 advanced_parameters.json 中配置.


5. work_dir 目录权限必须是 可写入.

#  更新说明

- 2017.11.15  增加 -s 参数，指定每个部分开始的 step
- 2017.11.17  添加功能：删除 oases 结束后产生较大的临时文件 (Graph2等)
- 2018.04.25  增加 reads 中 *.fastq.gz 格式支持





    




