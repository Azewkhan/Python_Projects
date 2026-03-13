import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#Keyword research by region
trends.build_payload(kw_list=["Python Projects"])
data = trends.interest_by_region()
#print(data.sample(10))

# Plot histogram of our data
df = data.sample(15)
df.reset_index().plot(x="geoName", y="Python Projects", figsize=(120,16), kind="bar")
#plt.show()

#Trending search in a given region
data = trends.trending_searches(pn="US")
#print(data.head(10))

#keyword suggestion related to given word
keyword = trends.suggestions(keyword="Programming")
data = pd.DataFrame(keyword)
#print(data.head())