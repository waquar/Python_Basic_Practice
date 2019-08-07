from win32com.client import  Dispatch
import json
import requests

url = ('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e98b8fc50ef743b1a712da9e8500fff7')

def speak(text):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(text)

if __name__ == '__main__':
    speak('Today news are these')
    news_json = requests.get(url).text
    news_python = json.loads(news_json)                                                               #converts it to python readable text
    articles = news_python['articles']
    for items in articles:
        print(items['title'])
        print(items['url'])
        speak(items['content'])
        speak('next news is ')




