!pip install pytrends

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq(hl='en-US', tz=360)

Inp=input("Enter your query: ")

trends.build_payload(kw_list = [Inp])  
df = trends.interest_by_region()    #It is for countries
df = df.sort_values(by = Inp,ascending = False)
df = df.head(15)  #top 15 countries
print(df)


df.reset_index().plot(x="geoName",y=Inp,figsize = (12,10),kind = "bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US',tz=360)
data.build_payload(kw_list = [Inp])
data = data.interest_over_time()
fig,ax = plt.subplots(figsize = (12,10))
data[Inp].plot()
plt.title('Total Google Searches', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Count')
plt.style.use('fivethirtyeight')
plt.show()

