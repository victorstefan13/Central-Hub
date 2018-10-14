from newsapi import NewsApiClient
from pprint import pprint
from os import system

# Init
newsapi = NewsApiClient(api_key='9554a40cc2354d05bbe4bc675ea45a22')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')

print(top_headlines)
# res = requests.get(url)

# data = res.json()

# headlines = data['content']

# print('{}'.format(headlines))
# pprint(data)