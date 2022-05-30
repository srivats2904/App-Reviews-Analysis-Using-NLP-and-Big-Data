from google_play_scraper import app,reviews,Sort
import json
import numpy as np
import pandas as pd

# The continuation stream is used to get the stream of data with respect to the reviews method called earlier

result,continuation_token=reviews('com.koo.app',lang='en',country='in',sort=Sort.MOST_RELEVANT,count=200)   
result,_=reviews('com.koo.app',continuation_token=continuation_token)

df=pd.DataFrame(result)
print(df.head())

df.to_csv('koo_google.csv')
