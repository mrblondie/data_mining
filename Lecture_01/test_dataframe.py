import pandas as pd
import numpy as np
import pylab as pl
import mpl_toolkits.basemap as bm
import twitter
import requests
import datetime
import dateutil
import csv
import random 


df = pd.DataFrame({'A': ['foo', 'bar', 'ololo'] * 4,
                            'B': np.random.randn(12),
                            'C': np.random.randint(0, 2, 12)})
print df

ga = df.groupby(['A'])['C'].value_counts()
print ("\n\n---------------")
print ga
print type(ga)
print ga.to_dict()
print ga.tolist()
