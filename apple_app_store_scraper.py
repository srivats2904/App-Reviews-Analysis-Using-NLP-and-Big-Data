from app_store_scraper import AppStore
import json
import numpy as np
import pandas as pd

app=AppStore(country='in',app_name='koo')       
app.review(how_many=200)

df = pd.DataFrame(np.array(app.reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
print(df2.head())

df2.to_csv('koo_apple.csv')
