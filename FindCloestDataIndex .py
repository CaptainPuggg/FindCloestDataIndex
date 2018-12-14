

import pandas as pd
myf=pd.read_csv('Big.csv')

myf['date'] = pd.to_datetime(myf['date'])

mydate=pd.Index(myf['date'])

date_=pd.to_datetime('2009-01-05')

mydate.get_loc(date_,method='nearest')
