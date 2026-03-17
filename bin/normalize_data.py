#!/usr/bin/env python3
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])

df = df / df.max()

df.to_csv(sys.argv[2], index=False)