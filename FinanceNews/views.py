from turtle import title
from django.shortcuts import render
#from newsapi import NewsApiClient
import requests

def index(request):
    #newsApi = NewsApiClient(api_key='1e1142c781204aa8b0de8eb5066cef43')
    #headLines = newsApi.get_top_headlines(sources='cnn')
    r = requests.get('https://bb-finance.p.rapidapi.com/stories/list?id=usdjpy&template=CURRENCY', 
    headers={'X-RapidAPI-Key': '3e0c82d23dmsh8aa923431107b2ap12db5fjsn66d8d6d8a8cc',
    'X-RapidAPI-Host': 'bb-finance.p.rapidapi.com'})

    res=r.json()
    print(res)
    articles = res['stories']
    description =[]
    img =[]
    news =[]
    url =[]
    mylist=[]

    for i in range(len(articles)):
        '''
        article= articles[i]
        article_obj = dict()
        description.append(article['description'])
        img.append(article['urlToImage'])
        news.append(article['title'])
        url.append(article['url'])
        article_obj.update()
        '''
        mylist.append(articles[i])

    #mylist = list (zip(news, description, img,url))
    print(mylist[0])
    return render(request, "main/index.html", context={"mylist": mylist})

    '''
    r = requests.get('https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=1e1142c781204aa8b0de8eb5066cef43')
    res = r.json()
    data = res['articles']
    title = []
    description =[]
    urltoimage =[]
    url =[]
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        urltoimage.append(i['image'])
        url.append(i['url'])
    news = zip(title, description,urltoimage, url)
    return render(request,'FinanceNews/index.html',{'news':news})
    '''
