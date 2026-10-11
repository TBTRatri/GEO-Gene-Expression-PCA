# High-Dimensional Genomic Expression Profiling & PCA (NCBI GEO GSE6613)

This project explores computational dimensionality reduction and unsupervised variance analysis on high-dimensional microarray gene expression profiles retrieved from the NCBI Gene Expression Omnibus (GEO).

## Overview
- **Dataset:** NCBI GEO Accession [GSE6613](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE6613) (Platform GPL96)
- **Data Scale:** 22,283 probe sets across 105 biological samples
- **Domain Challenge:** Addressing the $p \gg n$ curse of dimensionality in functional genomics

## Pipeline & Methods
1. **Automated Parsing:** Extracted series matrices, sample annotations, and probe-to-gene mapping dictionaries via `GEOparse`.
2. **Quality Control & Preprocessing:** Implemented zero-variance filtering and missing-value imputation.
3. **Z-Score Normalization:** Scaled multi-dimensional expression variance with `StandardScaler`.
4. **Principal Component Analysis (PCA):** Projected orthogonal variance vectors to isolate dominant biological variance axes.
5. **Expression Landscaping:** Generated multi-sample expression heatmaps using Seaborn and Matplotlib.

## Tech Stack
- **Language:** Python
- **Libraries:** GEOparse, Scikit-Learn, Pandas, NumPy, Seaborn, Matplotlib
