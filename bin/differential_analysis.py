#!/usr/bin/env python3
import pandas as pd
from scipy.stats import ttest_ind
import sys

df = pd.read_csv(sys.argv[1])

# keep numeric data
df = df.select_dtypes(include="number")

if df.shape[1] < 2:
    raise ValueError("Not enough columns for differential analysis")

# split samples into two groups
mid = df.shape[1] // 2
group1 = df.iloc[:, :mid]
group2 = df.iloc[:, mid:]

pvals = []

for i in range(df.shape[0]):
    stat, p = ttest_ind(group1.iloc[i], group2.iloc[i], equal_var=False)
    pvals.append(p)

out = pd.DataFrame({
    "metabolite_index": range(len(pvals)),
    "pvalue": pvals
})

out.to_csv(sys.argv[2], index=False)