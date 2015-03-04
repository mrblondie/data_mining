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

ts_parser = lambda date_str: dateutil.parser.parse(date_str) if pd.notnull(date_str) else None

def twitter_user_to_dataframe_record(user):
    record = {
        "user_id": user.id,
        "name": user.name,
        "screen_name": user.screen_name,        
        "created_at": ts_parser(user.created_at),        
        "followers_count": user.followers_count,
        "friends_count": user.friends_count,
        "statuses_count": user.statuses_count,
        "favourites_count": user.favourites_count,
        "listed_count": user.listed_count,
        "verified": user.verified
    }
    
    if user.description is not None and user.description.strip() != "":
        record["description"] = user.description
        
    if user.location is not None and user.location.strip() != "":
        record["location"] = user.location
        record["lat"], record["lon"], record["country"] = get_coordinates_by_location(user.location)
    
    return record





def get_json_by_location(location):
  rows = 1
  base = 'http://api.geonames.org/searchJSON'
  options = {'q':location, 'maxRows':rows, 'username':'rageblonde'}
  r = requests.get(base, params=options)
  return r.json()
  

def get_coordinates_by_json(json_object):
  return ( 
           json_object['geonames'][0]['lng'], 
           json_object['geonames'][0]['lat'], 
           json_object['geonames'][0]['countryName']
          )

def get_coordinates_by_location(location):
  return get_coordinates_by_json(get_json_by_location(location))






def get_user_records(df):
  
  result = []
  user_ids = df['user_id'].tolist()  # get id's of all user

  # from apps.twitter.coms
  # Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
  # OLOLOLO   
  CONSUMER_KEY    = 'r0yEHpewpZvKkdqIL79NK4h1H'
  CONSUMER_SECRET = '4YEWfgPByZCTWoNlh5xHSxEr0sdUx4HdhWdKxtN4X2EbbLtD4K'
  TOKEN_KEY       = '3067337884-ZBE4YspxgXU3ZTEQdb3pGEXjWWW6EcsA7S89iyo'
  TOKEN_SECRET    = 'HUTX2RdHLteVS7aSfRIQXegphPytKUaYEgyM2zXqKoTN6'
  
  
  api = twitter.Api (
                      consumer_key        = CONSUMER_KEY,
                      consumer_secret     = CONSUMER_SECRET,
                      access_token_key    = TOKEN_KEY,
                      access_token_secret = TOKEN_SECRET
                    )
# Temp solution
  ids_for_request = []
  for i in range(0, 2) : 
    ids_for_request.append(user_ids[i])
# WE NEED ALL FUCKING USER"s HERE

  users_info = api.UsersLookup(user_id = ids_for_request) #list of users
  for ui in users_info :
    result.append(twitter_user_to_dataframe_record(ui))
    print twitter_user_to_dataframe_record(ui)

  

if __name__ == '__main__':
  
  TRAINING_SET_URL = "./Data/Data_Sfera_DM1.txt" # file path
  df_users = pd.read_csv(TRAINING_SET_URL, sep=",", header=1, names=['user_id', 'class'], skiprows = 1)
  
  user_records = get_user_records(df_users)



  