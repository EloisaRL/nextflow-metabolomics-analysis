#!/usr/bin/env python3
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], sep="\t")

# keep only columns that look like sample IDs
cols = [c for c in df.columns if "ADG" in c]

df = df[cols]

df = df.dropna()

df.to_csv(sys.argv[2], index=False)