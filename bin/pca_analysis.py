#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sys

df = pd.read_csv(sys.argv[1])

X = df.T

pca = PCA(n_components=2)
components = pca.fit_transform(X)

plt.scatter(components[:,0], components[:,1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA of Metabolomics Samples")

plt.savefig(sys.argv[2])