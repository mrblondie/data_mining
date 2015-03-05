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


#
# http://api.geonames.org/search?q="San Francisco, CA"&maxRows=10&username=demo
#

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


if __name__ == '__main__':
  
  location = 'Tucson, AZ,'
  print get_coordinates_by_location(location)