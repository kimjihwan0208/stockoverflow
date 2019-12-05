
'''
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

host = 'search-stockoverflow-ve7piq57vont3m2dlw5vfzws64.us-east-2.es.amazonaws.com' # For example, my-test-domain.us-east-1.es.amazonaws.com
region = 'us-east-2' # e.g. us-west-1

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

document = {
    "title": "Moneyball",
    "director": "Bennett Miller",
    "year": "2011"
}

es.index(index="movies", doc_type="_doc", id="5", body=document)

print(es.get(index="movies", doc_type="_doc", id="5"))
'''



from datetime import datetime,date
from elasticsearch import Elasticsearch
es = Elasticsearch('https://ektda2wx9w:a2f28dfrin@stock-data-4002685217.us-west-2.bonsaisearch.net:443')
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://adiach1:1234@cluster0-jgwg7.mongodb.net/CS180?retryWrites=true&w=majority')
db = cluster['test']
collection = db['scraped_cleaned_docs']

# docs = list(collection.find({}))

NSM = datetime.combine(date(2019, 11, 19), datetime.min.time())
docs = list(collection.find({"date":{"$gte": NSM}}))
print(docs)

        
'''
        b = collection.find({
			"stock_symbol": stock_symbol,
			"date":{"$gte": NSM,
					"$lt": NSMax}})
'''
'''
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
'''
#res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
#print(res['result'])
#res = es.index(index = docs[i]['date'].date(), body=doc[i])
#res = es.get(index="test-index", doc_type='tweet', id=1)
#print(res['_source'])

#es.indices.refresh(index="test-index")

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
#print("Got %d Hits:" % res['hits']['total']['value'])
#for hit in res['hits']['hits']:
#    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

for i in range(0,len(docs)):
    del docs[i]['_id']
    del docs[i]['open']
    del docs[i]['close']
    del docs[i]['volume']
    del docs[i]['close_ten_day_pct']
    del docs[i]['open_ten_day_pct']
    del docs[i]['close_one_day_pct']
    del docs[i]['open_one_day_pct']
    del docs[i]['open_tomorrow']
    del docs[i]['close_tomorrow']
    del docs[i]['volume_tomorrow']
    res = es.index(index = 'stocks', body=docs[i])
    print(res['result'])
    # es.indices.refresh(index=docs[i]['date'].date())


# for i in range(0,10):
#     res = es.search(index=docs[i]['date'].date(), body={"query": {"match_all": {}}})
#     print("Got %d Hits:" % res['hits']['total']['value'])
#     for hit in res['hits']['hits']:
#         print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])