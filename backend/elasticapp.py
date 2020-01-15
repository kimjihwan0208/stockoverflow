from datetime import datetime,date
from elasticsearch import Elasticsearch
es = Elasticsearch()
from pymongo import MongoClient

cluster = MongoClient()
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