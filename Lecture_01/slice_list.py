
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



data = range(0, 3678)
chunks = [data[x:x+100] for x in xrange(0, len(data), 100)]

print chunks[0]
print '------------------//---------------------'
print chunks[-1]