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


# from apps.twitter.coms
# Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
# OLOLOLO 

CONSUMER_KEY    = 'key'
CONSUMER_SECRET = 'key'
TOKEN_KEY       = 'key'
TOKEN_SECRET    = 'key'

#class MyPrinter(pprint.PrettyPrinter):
# def format(self, object, context, maxlevels, level):
#   if isinstance(object, unicode):
#      return (object.encode('utf8'), True, False)
#    return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)


api = twitter.Api (
                    consumer_key        = CONSUMER_KEY,
                    consumer_secret     = CONSUMER_SECRET,
                    access_token_key    = TOKEN_KEY,
                    access_token_secret = TOKEN_SECRET
                  )

users = api.GetFriends()
#MyPrinter().pprint([unicode(u.name) for u in users])
print ([u.name for u in users])


