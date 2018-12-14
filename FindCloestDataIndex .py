

import pandas as pd
myf=pd.read_csv('Big.csv')
myf['date'] = pd.to_datetime(myf['date'])
mydate=pd.Index(myf['date'])

# define the date you want
date_=pd.to_datetime('2009-01-05')
index_=mydate.get_loc(date_,method='nearest')

for y in range(2009,2012):
    for m in range(1,13):
        date_=pd.to_datetime(str(y)+'-'+str(m)+'-'+'05')
        index_=mydate.get_loc(date_,method='nearest')
        print(str(index_)+':'+str(myf['date'][index_]))
# for meidiudiu:

for y in range(2016,2019):
    for m in range(1,13):
        date_=pd.to_datetime(str(y)+'-'+str(m)+'-'+'05')
        if date_>(pd.to_datetime('2016-02-29')) and date_<(pd.to_datetime('2018-07')):
                index_=mydate.get_loc(date_,method='nearest')
                print(str(index_)+':'+str(myf['date'][index_]))
