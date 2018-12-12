



#### Extract useful data from RNA-seq results in WT and transgenic tomato fruits

              
              
                             Haiping Liu Ph.D


#### Introduction
- Material

RNA-seq results from amiR396 (miR396 overexpressed) and STTM396 (miR396 being silenced) tomato fruits

- Objective

Visualization of RNA-seq data, especially extract differentially expressed genes I am interested in.


#### Overview

1. Import CVS file
2. Evaluation the quality of RNA-seq results (histogram)
3. Display how many genes are differentially expressed (how many up- or down-regulated).
4. Display genes with annotation containing targeted words


#### Load the libraries and read CSV file

```
#load the libraries
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np

#Read CVS file form local
df = pd.read_csv('/Users/haipingliu/Desktop/BiOF309/Final_project/
DEG_anno.csv')
```

#### Display how many genes are differentially expressed

<img src="image\gene_N_columns.png" width="1200">

#### Display how many genes have fold change above 2
<img src="image\N_Fold2.png" width="1000">
<img src="image\Head_Fold2.png" width="600">

#### Display up-regulated genes in STTM396 fruits

<img src="image\OE_N.png" width="1200">
<img src="image\OE_head.png" width="1200">

#### Display down-regulated genes in STTM396 fruits
<img src="image\D_N.png" width="1200">
<img src="image\D_head.png" width="1200">

#### RNA-seq result follows standard normal distribution (histogram)
<img src="image\his_distribution.png" width="700">

#### Extract interested genes related with sweetness of fruits
- Sugar
<img src="image\Sugar.png" width="1300">

#### Starch
<img src="image\Starch.png" width="1300">

#### Sucrose
<img src="image\Sucrose.png" width="1200">

#### Cobine all the genes related with sweetness

<img src="image\combine_code.png" width="1200">
<img src="image\combined_genes.png" width="800">

#### Write a CSV file from DataFrame

```
Sugar_gene.to_csv('Sugar_gene.csv')
```

<img src="image\sugar_genes_CVS.png" width="1200">

#### Get targeted columns (FPKM values for two samples) from "Sugar_gene"

<img src="image\FPKM.png" width="1200">

#### Heatmap for expression of sweetness-related genes

```
Heatmap for expression of sweetness-related genes (codes)

df_FPKM_index = df_FPKM.set_index('Gene_ID')
sns.clustermap(df_FPKM_index,
              z_score=1,
              metric="euclidean",
              method="ward",
              cmap="Blues",
              annot=True,
              linewidths=1.0)
plt.show()
```

#### Output for heatmap
<img src="image\Heatmap.png" width="700">

#### Conclusion

1. RNA-seq result is fine
2. 18 genes related with fruit sweetness are differentially expressed between amiR396 and STTM396 transgenic fruits.


