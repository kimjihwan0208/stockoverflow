import requests
from bs4 import BeautifulSoup


baseurl = 'http://www.reuters.com/news/archive/worldNews?view=page='
valid_pages = 'abcdefghijlmnoprstuvw'
total_urls = []
for n in range(1,10):
    total_urls.append(baseurl + format(n))
print(total_urls)

titles = []
summary = []
timestamp = []


for url in total_urls:
    result = requests.get(url)
    content = result.content
    content.decode().strip().replace('\t','').split('\n')

    soup = BeautifulSoup(content, 'html.parser')
    soup.find_all('h3', {'class':'story-title'})

    for title in soup.find_all('h3', {'class':'story-title'}):
        titles.append(title.string.strip())

    try:
        for summary in soup.find_all('p'):
            summary.append(summary.string.strip())
    except:
        pass

    for written_time in soup.find_all('span', {'class':'timestamp'}):
        timestamp.append(written_time.string.strip())

print(titles)
print(summary)
print(timestamp)
