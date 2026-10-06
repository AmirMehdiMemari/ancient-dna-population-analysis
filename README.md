\# Ancient DNA Population Analysis



Exploratory population-genetics analysis of ancient DNA from Britain and Ireland using Python, PCA, unsupervised clustering, archaeological metadata, and sensitivity analysis.



The project investigates broad genetic structure through time while carefully distinguishing large-scale patterns from site-specific, technical, and small-sample effects.



\---



\## Project Overview



This project uses the COMMIOS/AADR ancient DNA dataset to explore population structure among ancient individuals from Britain and Ireland.



The workflow combines:



\- Archaeological metadata processing

\- Ancient DNA quality control

\- Packed genotype decoding

\- SNP and individual missingness filtering

\- Minor allele frequency filtering

\- Physical SNP thinning

\- Genotype imputation and standardization

\- Principal Component Analysis (PCA)

\- K-Means clustering

\- Silhouette analysis

\- Archaeological-period comparison

\- Temporal and geographic visualization

\- Sensitivity analysis for site and representation effects



\---



\## Dataset



\*\*Source:\*\*  

Metz et al. (2025), \*COMMIOS: A curated dataset and web application for Integrative Analysis of Ancient DNA from Britain and Ireland\*



\*\*Zenodo\*\*



\- Version DOI: `10.5281/zenodo.15536132`

\- All versions DOI: `10.5281/zenodo.15536131`

\- License: CC BY 4.0



The original dataset used in this project contains:



\- \*\*6,872 individuals\*\*

\- \*\*584,131 SNPs\*\*



The Human Origins files used were:



\- `COMMIOS\_aadr\_HO\_v62.anno.gz`

\- `COMMIOS\_aadr\_HO\_v62.geno.gz`

\- `COMMIOS\_aadr\_HO\_v62.ind.gz`

\- `COMMIOS\_aadr\_HO\_v62.snp.gz`



The raw genotype data are not included in this repository because the main genotype file is approximately \*\*634 MB\*\*.



See \[`data/README.md`](data/README.md) for additional information.



\---



\## Analysis Workflow



The dataset was progressively filtered to obtain a higher-quality ancient DNA cohort.



Major stages included:



1\. Selecting individuals from Britain and Ireland

2\. Removing present-day individuals

3\. Keeping samples marked `PASS` or `MERGE\_PASS`

4\. Resolving duplicate individuals using the highest available SNP coverage

5\. Applying a minimum Human Origins SNP coverage threshold

6\. Filtering SNPs by missingness

7\. Filtering individuals by genotype missingness

8\. Removing low-frequency variants

9\. Applying 50 kb physical SNP thinning

10\. Mean-imputing remaining missing genotype calls

11\. Standardizing genotype features

12\. Performing PCA

13\. Evaluating exploratory K-Means clustering

14\. Investigating site-specific and representation-related effects

15\. Performing post-Neolithic sensitivity analyses



\---



\## Final Analytical Dataset



The principal analysis contained:



| Archaeological Period | Samples |

|---|---:|

| Mesolithic | 1 |

| Neolithic | 98 |

| Bronze Age | 103 |

| Iron Age | 231 |

| Roman | 2 |

| Transitional / Mixed | 6 |

| Early Medieval | 172 |

| Medieval | 3 |

| \*\*Total\*\* | \*\*616\*\* |



The final PCA used:



\- \*\*616 individuals\*\*

\- \*\*33,906 SNPs\*\*



\---



\## Main PCA Result



The strongest population-structure pattern was a pronounced separation between \*\*Neolithic individuals and later archaeological populations\*\*.



Mean PC1 values included:



| Period | Mean PC1 |

|---|---:|

| Neolithic | -30.69 |

| Bronze Age | 7.77 |



Bronze Age, Iron Age, Roman, and Early Medieval individuals showed substantially greater overlap in PCA space.



!\[Final PCA](images/plots/final\_pca\_pc1\_pc2.png)



The first ten principal components together explained approximately \*\*2.57%\*\* of the standardized genotype variance.



!\[PCA Explained Variance](images/plots/pca\_explained\_variance.png)



\---



\## Genetic Structure Through Time



PC1 was plotted against approximate archaeological calendar year to investigate how the strongest genetic structure varied through time.



!\[Genetic Structure Through Time](images/plots/genetic\_structure\_through\_time.png)



The plot shows a pronounced shift between Neolithic individuals and subsequent archaeological periods.



This temporal pattern should not by itself be interpreted as proof of a particular migration event or complete population replacement.



\---



\## Archaeological Period Comparison



PC1 distributions were also compared across broad archaeological periods.



!\[PC1 by Archaeological Period](images/plots/pc1\_by\_archaeological\_period.png)



The Neolithic group occupies a substantially different region of PC1 space, while Bronze Age, Iron Age, Roman, and Early Medieval samples overlap more strongly.



The following groups have very small sample sizes and should therefore not support strong period-level conclusions:



\- Mesolithic: `n = 1`

\- Roman: `n = 2`

\- Medieval: `n = 3`



\---



\## K-Means Clustering



K-Means clustering was evaluated using the first 10 principal components.



The strongest solution in the main dataset was:



```text

k = 2

Silhouette score = 0.3158

```



Cluster composition was:



| Cluster | Samples | Main Composition |

|---|---:|---|

| 0 | 98 | Neolithic |

| 1 | 518 | Later archaeological samples |



The clustering therefore largely recovered the same major structure already identified by PCA: \*\*Neolithic versus later individuals\*\*.



!\[K-Means Clusters](images/plots/kmeans\_clusters\_pca.png)



The cluster labels are treated only as data-driven statistical groupings and are not interpreted as direct ancestry categories.



\---



\## Post-Neolithic Analysis



To investigate more subtle genetic structure, Neolithic and Mesolithic samples were removed and PCA was recalculated for the remaining \*\*517 post-Neolithic individuals\*\*.



The first ten components explained approximately \*\*2.62%\*\* of the variance.



!\[Post-Neolithic PCA](images/plots/post\_neolithic\_pca.png)



Initial clustering produced:



```text

k = 2

Silhouette score = 0.6888

```



However, closer inspection showed that one of the two clusters contained only \*\*three Early Medieval individuals from Lakenheath\*\*.



The apparently strong clustering result was therefore driven by a very small site-specific group rather than a broad division among post-Neolithic populations.



\---



\## Clustering Sensitivity Analysis



The three-person Lakenheath cluster was temporarily excluded to test whether strong post-Neolithic clusters remained.



The resulting silhouette scores were:



| k | Silhouette Score |

|---:|---:|

| 2 | 0.0838 |

| 3 | 0.0791 |

| 4 | 0.0751 |

| 5 | 0.0821 |

| 6 | 0.0763 |

| 7 | 0.0801 |

| 8 | 0.0887 |



These low scores provide little evidence for clearly separated discrete clusters among the remaining post-Neolithic individuals.



This demonstrates the importance of inspecting cluster composition rather than interpreting a high silhouette score in isolation.



\---



\## Quality-Control and Sensitivity Findings



During PCA inspection, a group of extreme observations was associated with individuals from \*\*Hazleton North\*\* carrying `TW`-containing genetic representations.



All `TW`-containing samples in the filtered dataset originated from Hazleton North. Representation type and archaeological site were therefore completely confounded.



Because these two factors could not be separated statistically, the samples were excluded from the main PCA as a \*\*robustness decision\*\* rather than being classified as definite technical artifacts.



A separate sensitivity analysis showed that the broad Neolithic separation remained after these samples were excluded.



The Lakenheath observations were retained in the primary analysis but investigated separately because of their strong influence on post-Neolithic clustering.



\---



\## Geographic Distribution



The dataset includes archaeological samples distributed across Britain and Ireland.



!\[Geographic Distribution](images/plots/geographic\_distribution\_clean.png)



\---



\## Chronological Distribution



The chronological distribution of the filtered ancient samples is shown below.



!\[Chronological Distribution](images/plots/chronological\_distribution.png)



\---



\## Archaeological Period Distribution



!\[Samples by Period](images/plots/samples\_by\_period.png)



\---



\## Methodological Notes



The genotype data used in the selected ancient samples were effectively represented using \*\*pseudohaploid allele calls\*\*.



Physical SNP thinning at \*\*50 kb intervals\*\* was used as a lightweight approximation for reducing highly local marker redundancy. This should \*\*not\*\* be interpreted as formal linkage-disequilibrium pruning.



Archaeological periods were derived from broad patterns in the source `Group ID` labels and are intended as analytical context rather than precise cultural classifications.



PCA and K-Means identify statistical patterns in genetic variation. They do not independently demonstrate ancestry proportions, migration events, population replacement, or causal historical processes.



Close genetic relatives may also influence local PCA structure. The available metadata were used to investigate obvious relationship and site patterns, but formal kinship pruning was not performed.



\---



\## Key Conclusion



The analysis identifies a strong broad-scale genetic distinction between \*\*Neolithic individuals and later ancient populations from Britain and Ireland\*\*.



After the Neolithic, genetic structure becomes substantially more overlapping and continuous.



Exploratory clustering did not provide robust evidence for multiple discrete post-Neolithic genetic populations after site-specific outliers were investigated.



The project also demonstrates the importance of:



\- quality control

\- metadata interpretation

\- duplicate handling

\- missing-data filtering

\- outlier investigation

\- sensitivity analysis

\- cautious interpretation of unsupervised machine-learning results



when working with ancient DNA.



\---



\## Repository Structure



```text

ancient-dna-population-analysis/

│

├── README.md

├── requirements.txt

├── .gitignore

│

├── data/

│   ├── README.md

│   ├── raw/

│   └── processed/

│       ├── analysis\_summary.csv

│       ├── britain\_ireland\_ancient\_metadata.csv

│       ├── final\_pca\_results.csv

│       └── period\_pca\_summary.csv

│

├── images/

│   └── plots/

│

├── notebooks/

│   └── 01\_ancient\_dna\_population\_analysis.ipynb

│

└── src/

&#x20;   ├── \_\_init\_\_.py

&#x20;   ├── preprocessing.py

&#x20;   ├── pca\_analysis.py

&#x20;   ├── clustering.py

&#x20;   └── visualization.py

```



\---



\## Processed Outputs



Important processed files include:



\### `final\_pca\_results.csv`



Contains the final analytical sample metadata together with PCA coordinates and exploratory cluster labels.



\### `period\_pca\_summary.csv`



Contains period-level sample counts and PC1 summary statistics.



\### `analysis\_summary.csv`



Contains the main project metrics and analytical conclusion.



\### `britain\_ireland\_ancient\_metadata.csv`



Contains the cleaned archaeological metadata used during the analysis.



\---



\## Installation



Clone the repository and move into the project directory.



Create a virtual environment if desired, then install the required packages:



```bash

pip install -r requirements.txt

```



Start Jupyter Notebook:



```bash

jupyter notebook

```



Open:



```text

notebooks/01\_ancient\_dna\_population\_analysis.ipynb

```



Raw COMMIOS/AADR files must be downloaded separately and placed inside:



```text

data/raw/

```



\---



\## Requirements



Main Python packages:



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Jupyter Notebook



\---



\## Project Skills Demonstrated



This project demonstrates practical experience with:



\- Data cleaning

\- Biological metadata processing

\- Ancient DNA quality control

\- Binary genotype-data handling

\- High-dimensional genetic data

\- Missing-data analysis

\- Feature filtering

\- PCA

\- Unsupervised machine learning

\- K-Means clustering

\- Silhouette analysis

\- Outlier detection

\- Sensitivity analysis

\- Scientific visualization

\- Reproducible Python workflows

\- Scientific interpretation of machine-learning results



\---



\## Author



\*\*Amir Mehdi Memari\*\*  

MSc Data Science \& Machine Learning  

Sultan Qaboos University

