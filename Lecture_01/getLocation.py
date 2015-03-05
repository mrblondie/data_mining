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

def generateUsers(id):
  rand_users = []
  for i in range(1, 30):
    rand_users.append(random.randint(0, KremlinRussiaID+1000000))
  return rand_users



# from apps.twitter.coms
# Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
# OLOLOLO 
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''
TOKEN_KEY       = ''
TOKEN_SECRET    = ' '


if __name__ == '__main__':

  KremlinRussiaID = 158650448
  api = twitter.Api (
                      consumer_key        = CONSUMER_KEY,
                      consumer_secret     = CONSUMER_SECRET,
                      access_token_key    = TOKEN_KEY,
                      access_token_secret = TOKEN_SECRET
                    )

#mine_user stuff
#users = api.GetFriends()
#RusPrint().pprint([u.name for u in users])

  rand_users = generateUsers(KremlinRussiaID)
  statuses = api.UsersLookup(user_id = rand_users)
  RusPrint().pprint([s.location for s in statuses])

  
