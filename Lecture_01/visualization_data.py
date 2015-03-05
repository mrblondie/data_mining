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
import datetime
import time

def count_users(grouped):
    """
    Counts number of positive and negative users
    created at each date.
    
    Returns:
        count_pos -- 1D numpy array with the counts of positive users created at each date
        count_neg -- 1D numpy array with the counts of negative users created at each date
        dts -- a list of date strings, e.g. ['2014-10-11', '2014-10-12', ...]
    """


    dts = []
    count_pos, count_neg = np.zeros(len(grouped)), np.zeros(len(grouped))
    
    print grouped['class'].value_counts().to_dict()

    return count_pos, count_neg, dts


TRAINING_SET_URL = "./grouped_data" # file path
names_fd = ['user_id','class', 'name', 'screen_name', 'description', 'verified', 'location', 'lat', 'lon', 'country', 'created_at', 'followers_count', 'friends_count', 'statuses_count', 'favourites_count', 'listed_count']
df_full = pd.read_csv(TRAINING_SET_URL, sep=";", header=1, names=names_fd , skiprows = 1)



grouped = df_full.groupby(map (lambda dt: dt.strftime("%Y-%m") if pd.notnull(dt) else "NA", df_full["created_at"]) )
count_pos, count_neg, dts = count_users(grouped)
    
fraction_pos = count_pos / (count_pos + count_neg + 1e-10)
fraction_neg = 1 - fraction_pos

sort_ind = np.argsort(dts)
    
pl.figure(figsize=(20, 3))
pl.bar(np.arange(len(dts)), fraction_pos[sort_ind], width=1.0, color='red', alpha=0.6, linewidth=0, label="Positive")
pl.bar(np.arange(len(dts)), fraction_neg[sort_ind], bottom=fraction_pos[sort_ind], width=1.0, color='green', alpha=0.6, linewidth=0, label="Negative")
pl.xticks(np.arange(len(dts)) + 0.4, sorted(dts), rotation=90)
pl.title("Class distribution by account creation month")
pl.xlim(0, len(dts))
pl.legend()
pl.show()



  