#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import pandas as pd
import numpy as np
import pylab as pl
import mpl_toolkits.basemap as bm

import twitter
import requests
import datetime
import dateutil
import csv
import json
import pprint
import sys
import random

TRAINING_SET_URL = "./Data/Data_Sfera_DM1.txt" # insert file path here
df_users = pd.read_csv(TRAINING_SET_URL, sep=",", header=1, names=["user_id", "class"], skiprows=1)

counts, bins = np.histogram(df_users["class"], bins=[0, 1, 2])

print '0 - negative' # counts[0]
print '1 - positive' # counts[1]
print counts

# Plot the distribution
pl.figure(figsize=(7,7))
pl.bar(bins[:-1], counts, width=0.5, alpha=0.4)
pl.xticks(bins[:-1] + 0.3, ["negative", "positive"])
pl.xlim(bins[0] - 0.5, bins[-1])

pl.ylabel("Number of users")
pl.title("Target variable distribution")

pl.show()
