import requests
from bs4 import BeautifulSoup


url = 'http://www.reuters.com/news/archive/worldNews?view=page'
result = requests.get(url)
content = result.content
content.decode().strip().replace('\t','').split('\n')

# EXTRACTING CONTENT
soup = BeautifulSoup(content, 'html.parser')
soup.find_all('h3', {'class':'story-title'})

# TITLES
titles = []
for title in soup.find_all('h3', {'class':'story-title'}):
    titles.append(title.string.strip())

# SUMMARY
summary = []
try:
    for summary in soup.find_all('p'):
        summary.append(summary.string.strip())
except:
    pass

# DATE/TIME WRITTEN
timestamp = []
for written_time in soup.find_all('span', {'class':'timestamp'}):
    timestamp.append(written_time.string.strip())


#GETTING URL

# urls = []
# import re
# for tags in soup.find_all('a'):
#    if re.search('article', tags['href']):
#        urls.append(tags['href'])
# urls = urls[:-5]
# final_urls = []
# for url in urls:
#    if url not in final_urls:
#        final_urls.append(url)


# Testing

print(titles)
print(summary)
print(timestamp)
#print(final_urls)
