import requests
from bs4 import BeautifulSoup
import datetime
import time
from pymongo import MongoClient

baseurl = 'https://www.reuters.com/finance/markets?view=page='
total_urls = []
for n in range(1,10):
    total_urls.append(baseurl + format(n))
print(total_urls)

titles = []
summary = []
timestamp = []
f = open('soup.txt','w')
g = open('article.txt','w')
cluster = MongoClient()

db = cluster["scraped_data"]
collection = db["data"]
for url in total_urls:
    result = requests.get(url)
    content = result.content
    content.decode().strip().replace('\t','').split('\n')

    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify(),file=f)
    
    for article in soup.find_all('article', {'class':'story'}):

        title = article.find('h3',{'class':'story-title'})
        timestamp = article.find('span', {'class':'timestamp'})
        link = article.find('a', href=True)
        story = article.find('p')


        #print("title", title.string.strip())
        title = title.string.strip()
        if timestamp.string.strip().find('EST') != -1: # cotains a timezone
            t = timestamp.string.strip().split()[0]
            #print("timestamp", datetime.datetime.combine(datetime.datetime.now().date(),datetime.datetime.strptime(t, '%I:%M%p').time()))
            timestamp = datetime.datetime.combine(datetime.datetime.now().date(),datetime.datetime.strptime(t, '%I:%M%p').time())
        else:
            #print("timestamp", datetime.datetime.combine(datetime.datetime.strptime(timestamp.string.strip(), '%b %d %Y'),datetime.time(00,00)))
            timestamp = datetime.datetime.combine(datetime.datetime.strptime(timestamp.string.strip(), '%b %d %Y'),datetime.time(00,00))
        #print("link", "reuters.com"+link['href'])
        link = "reuters.com"+link['href']
        #print("story", story.string.strip())
        story = story.string.strip()

        post = {"title":title, "timestamp":timestamp, "link":link, "story":story}
        print(post)        
        
        print(list(collection.find(post)))

        if len(list(collection.find(post))) > 0:
            print("Duplicate")
        else:
            collection.insert_one(post)
            print(post)
    

        
        


    # for title in soup.find_all('h3', {'class':'story-title'}):
    #     titles.append(title.string.strip())

    # try:
    #     for summary in soup.find_all('p'):
    #         summary.append(summary.string.strip())
    # except:
    #     pass

    # for written_time in soup.find_all('span', {'class':'timestamp'}):
    #     timestamp.append(written_time.string)

# print(titles)
# print(len(titles))
# print(summary)
# print(type(summary))
# print(len(summary))
# for s in summary:
#     print(s)
#     print()
#print(timestamp)
