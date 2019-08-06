import json
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=e98b8fc50ef743b1a712da9e8500fff7')
response = requests.get(url)
print (response.json())