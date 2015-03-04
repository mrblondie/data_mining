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

class RusPrint(pprint.PrettyPrinter):
  def format(self, object, context, maxlevels, level):
    if isinstance(object, unicode):
      return (object.encode('utf8'), True, False)
    return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)


# from apps.twitter.coms
# Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
# OLOLOLO 

CONSUMER_KEY    = ''
CONSUMER_SECRET = ''
TOKEN_KEY       = ''
TOKEN_SECRET    = ''
    

if __name__ == '__main__':
  
  TRAINING_SET_URL = "./Data/Data_Sfera_DM1.txt" # file path
  df_users = pd.read_csv(TRAINING_SET_URL, sep=",", header=1, names=['user_id', 'class'], skiprows = 1)
  

  api = twitter.Api (
                      consumer_key        = CONSUMER_KEY,
                      consumer_secret     = CONSUMER_SECRET,
                      access_token_key    = TOKEN_KEY,
                      access_token_secret = TOKEN_SECRET
                    )
  
  user_ids = df_users['user_id'].tolist() #most important line in this she{i}et
  
  ids_for_info = []
  for i in range(1, 100) : 
    ids_for_info.append(user_ids[i])
  
  statuses = api.UsersLookup(user_id = ids_for_info)
  RusPrint().pprint([s.location for s in statuses])