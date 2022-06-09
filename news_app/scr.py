from requests import get
import json
import pprint
api = "YOUR_API_HERE"
news= get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api}")
print(news)
news = json.loads(news.content)
#print(news)
names= []
titles= []
descs= []
articles= []
imgs= []
links= []
total = news['totalResults']
for i in news['articles']:
    # print(i)
    name=(i['source']['name'])
    title=(i['title'])
    desc=(i['description'])
    cntnt=(i['content'])
    img=(i['urlToImage'])
    link=(i['url'])
    names.append(name)
    titles.append(title)
    descs.append(desc)
    articles.append(cntnt)
    imgs.append(img)
    links.append(link)
print(len(links))
articless = []
for i in articles:
    if i:
        val = i.rfind("[")
        print (i,val)
        i = i[0:val]
    articless.append(i)
def get_news():
    return (names, titles, descs, articless, imgs, links)