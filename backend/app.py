from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime, time as T, timedelta
import yfinance as yf
import pandas as pd
from pandas_datareader.data import get_data_yahoo as get_stock_data
import json
from alpha_vantage.timeseries import TimeSeries
from pandas.tseries.holiday import USFederalHolidayCalendar
from copy import deepcopy
import requests
import pickle
cal = USFederalHolidayCalendar()
holidays = cal.holidays(start='2006-01-01', end='2019-12-31').to_pydatetime().tolist()
saturday = 5
sunday = 6
yf.pdr_override()
app = Flask(__name__)
CORS(app)
from elasticsearch import Elasticsearch
es = Elasticsearch('https://ektda2wx9w:a2f28dfrin@stock-data-4002685217.us-west-2.bonsaisearch.net:443')

cluster = MongoClient("mongodb+srv://adiach1:1234@cluster0-jgwg7.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]
def get_percentage_change(previous_number:float, current_number:float) -> float:
    if previous_number == current_number:
        return 0
    try:
        return ((current_number - previous_number) / previous_number) * 100.0
    except ZeroDivisionError:
        return float('inf')

High = 0
Low = 1       
Open = 2     
Close = 3  
Volume = 4  
Adj = 5 
Adj_Close = 6
pkl_filename = 'logisticRegressionModel.pickle'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)


def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']
@app.route("/api/date-to-stocks", methods=['GET', 'POST'])
def main():
	
	if request.method == 'POST':

		dateOne = request.json.get('date') # convert this to datetime object with strftime

		print(dateOne)
		if dateOne is None:
			#dateOne = datetime(2006,11,13)
			return {"Message":"None was sent"}
		date_ = datetime.strptime(dateOne, '%m/%d/%Y')
		#NSM = datetime.combine(date_, datetime.min.time())
		#NSMax = datetime.combine(date_, datetime.max.time())
		date_zeroed = date_.strftime('%Y-%m-%d') +"T00:00:00"
		date_oned = date_.strftime('%Y-%m-%d') +"T23:59:59"


		#b = collection.find({
		#	"date":{"$gte": NSM,
		#			"$lt": NSMax}})


		res = es.search(index='stocks', body={"query": {"range":\
			{"date" : { "gte" : date_zeroed, "lte" : date_oned}}}})
		# print("Got %d Hits:" % res['hits']['total']['value'])



		c = []
		for hit in res['hits']['hits']:
			c.append(hit['_source']['stock_symbol'])


		#    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

		#print(res)
		c = list(set(c))
		return {"Stocks":c}
		# a = list(b)
		# c= []
		# for i in a:
		# 	c.append(i["stock_symbol"])
		
		# return {"Stocks":c}


	return {"Hello":"World"}

@app.route("/api/stockdata", methods=['GET','POST'])
def stocks():

	if request.method == 'POST':

		dateOne = request.json.get('date')
		

		if dateOne is None:
			return {"Message":"No date was provided"}

		date_ = datetime.strptime(dateOne, '%m/%d/%Y')
		date_zeroed = date_.strftime('%Y-%m-%d') +"T00:00:00"
		date_oned = date_.strftime('%Y-%m-%d') +"T23:59:59"
		stock_symbol = request.json.get('stock')

		if stock_symbol is None:
			return {"Message":"No stock symbol was provided"}




		# query the function for that date. Talk to John/Eric and Eric/John for minimum number of points
		print(stock_symbol)
		try:
			stock_data = get_stock_data(stock_symbol,start=date_.strftime('%m/%d/%Y'),end=date_.strftime('%m/%d/%Y'),interval='d')
			# print(stock_data)
		except KeyError:
			return {"Message":"There is something seriously wrong here. Stock data was stored for this exact date in the DB but is now not available"}

	


		
		stock_data = stock_data.to_dict()

		open_ = stock_data.get("Open").get(pd.Timestamp(datetime.combine(date_, datetime.min.time())))
		close = stock_data.get("Close").get(pd.Timestamp(datetime.combine(date_, datetime.min.time())))

		NSM = datetime.combine(date_, datetime.min.time())
		NSMax = datetime.combine(date_, datetime.max.time())


		
		ts = TimeSeries(key='LC3BDD962B0ZBR5S', output_format='pandas')
		data, meta_data = ts.get_intraday(symbol=stock_symbol,interval='60min', outputsize='full')
		data = data.to_dict()



		'''
		b = collection.find({
			"stock_symbol": stock_symbol,
			"date":{"$gte": NSM,
					"$lt": NSMax}})
		
		'''
# 		q = es.search(index='stocks', body= \

# 		{ \
#   			"query": {  
#     			"bool": { \
#       "must": [ \
#         { \
#           "term": { \
#             "stock_symbol": stock_symbol \
#           } \
#         }, \
#         { \
#           "range": { \
#             "date": { \
#               "gte": date_zeroed, \
#               "lte": date_oned 
#             } \
#           } \
#         } \
#       ] \
#     } \
#   } \
# } 
# 		)
		q = es.search(index='stocks', body={"query": {"range":\
			{"date" : { "gte" : date_zeroed, "lte" : date_oned}}}})



		'''
		{"query": { \
			{"range": { \
				"date" : { \
					 "gte" : date_zeroed, "lte" : date_oned \
					 } \
					 }}, \
			{"match": { "stock_symbol":stock_symbol } }}}) 
			'''


		print(q)
		b = []
		sentiment = 0
		sentiment_denominator = 0
		for hit in q['hits']['hits']:
			if hit['_source']['stock_symbol'] == stock_symbol:
				b.append(hit['_source'])
				sentiment += hit['_source']['sentiment']['score']
				sentiment_denominator += 1
				print(b)

		# print(b['tf_idf'])
		
		results = b
		
		stock_data_list = []
		
		date_ = datetime.combine(datetime.now(), datetime.min.time())
		date_ -= timedelta(days=1)

		while date_.weekday() == saturday or date_.weekday() == sunday or datetime.combine(date_, datetime.min.time()) in holidays:
			date_ -= timedelta(days=1)




		for i in range(0,7):
			
			a = { "Value":(data.get("1. open").get(pd.Timestamp(datetime.combine(date_, T(hour=(9 + i), minute=30))))), \
					"time": str(9 + i)+":" + "30" }
			stock_data_list.append(a)

		

		

		termz = []
		for key in results[0]['tf_idf']['tfidf']:
			t = {key:results[0]['tf_idf']['tfidf'][key]}
			print(t)
			termz.append(t)

		print(termz)

		Articles = []
		for result in results:
			a = {'summary':result['summary'], 'link':result['link'], 'title':result['title'], "date":result['date'], "sentiment":result['sentiment']['label']}
			terms = []
			for key in result['tf_idf']['tfidf']:
				terms.append(key)

			a['terms'] = terms
			Articles.append(a)	


		start_datetime = deepcopy(date_)	
		while start_datetime.weekday() == saturday or start_datetime.weekday() == sunday  or  datetime.combine(start_datetime, datetime.min.time()) in holidays:
			start_datetime -= timedelta(days=1)


		yesterday_datetime = start_datetime - timedelta(days=1)


		while yesterday_datetime.weekday() == saturday or yesterday_datetime.weekday() == sunday or datetime.combine(yesterday_datetime, datetime.min.time()) in holidays:
			yesterday_datetime -= timedelta(days=1)


		tomorrow_datetime = start_datetime + timedelta(days=1)

		while tomorrow_datetime.weekday() == saturday or tomorrow_datetime.weekday() == sunday or datetime.combine(tomorrow_datetime, datetime.min.time()) in holidays:
			tomorrow_datetime += timedelta(days=1)

		ten_days_datetime = start_datetime - timedelta(days=10)

		yesterday_stock_data = None

		try:
			yesterday_stock_data = get_stock_data(stock_symbol, start=yesterday_datetime.strftime('%m/%d/%Y'), end=tomorrow_datetime.strftime('%m/%d/%Y'))
			ten_days_stock_data = get_stock_data(stock_symbol, start=ten_days_datetime.strftime('%m/%d/%Y'), end=start_datetime.strftime('%m/%d/%Y'), interval='d')


		except KeyError:
			pass

		if yesterday_stock_data is not None and ten_days_stock_data is not None:
			yest_stock_dict = yesterday_stock_data.to_dict()
			yest_stock_list = yesterday_stock_data.values.tolist()
			ten_days_list = ten_days_stock_data.values.tolist()

			# if company["text"] == "Hulu": 
			# 	print(company["text"])
			# 	print(yest_stock_dict)
			# 	print(yest_stock_list)
			# 	print(ten_days_list)
			# 	pass




			open_ = yest_stock_dict["Open"].get(pd.Timestamp(datetime.combine(start_datetime, datetime.min.time())))
			close = yest_stock_dict["Close"].get(pd.Timestamp(datetime.combine(start_datetime, datetime.min.time())))
			volume = yest_stock_dict["Volume"].get(pd.Timestamp(datetime.combine(start_datetime, datetime.min.time())))

			if open_ is None:
				open_ = ten_days_list[len(ten_days_list) - 2][Open]
				close = ten_days_list[len(ten_days_list) - 2][Close]
				volume = ten_days_list[len(ten_days_list) - 2][Volume]



			
			open_yesterday = yest_stock_dict["Open"].get(pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time())))
			close_yesterday = yest_stock_dict["Close"].get(pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time())))
			volume_yesterday = yest_stock_dict["Volume"].get(pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time())))


			if open_yesterday is None:
				open_ = ten_days_list[len(ten_days_list) - 3][Open]
				close = ten_days_list[len(ten_days_list) - 3][Close]
				volume = ten_days_list[len(ten_days_list) - 3][Volume]




			open_tomorrow = yest_stock_dict["Open"].get(pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time())))
			close_tomorrow = yest_stock_dict["Close"].get(pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time())))
			volume_tomorrow = yest_stock_dict["Volume"].get(pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time())))

			if open_tomorrow is None:
				open_tomorrow = ten_days_list[len(yest_stock_list)-1][Open]
				close_tomorrow = ten_days_list[len(yest_stock_list)-1][Close]
				volume_tomorrow = ten_days_list[len(yest_stock_list)-1][Volume]


			open_ten_days = ten_days_list[0][Open]
			close_ten_days = ten_days_list[0][Close]
			volume_ten_days = ten_days_list[0][Volume]

			# print(open_)
			# print(close)
			# print(volume)

			# print(open_yesterday)
			# print(close_yesterday)
			# print(volume_yesterday)

			# print(open_tomorrow)
			# print(close_tomorrow)
			# print(volume_tomorrow)

			# print(open_ten_days)
			# print(close_ten_days)
			# print(volume_ten_days)


			if close is None or close_ten_days is None or close_yesterday is None or open_ is None or open_ten_days is None or open_yesterday is None:
				print("WTF FOUND YOU")
				


			close_ten_day_pct = get_percentage_change(close_ten_days,close)
			open_ten_day_pct = get_percentage_change(open_ten_days, open_)

			close_one_day_pct = get_percentage_change(close_yesterday,close)
			open_one_day_pct = get_percentage_change(open_yesterday, open_)

			vals = [close_ten_day_pct, open_ten_day_pct, close_one_day_pct, open_one_day_pct, open_tomorrow, close_tomorrow, volume_tomorrow, open_yesterday, close_yesterday, volume_yesterday]
			company = get_symbol(stock_symbol)

			sentiment = sentiment/sentiment_denominator

			input_ = {'close_ten_day_pct': close_ten_day_pct, 'open_ten_day_pct': open_ten_day_pct, 'close_one_day_pct': close_one_day_pct, \
				'open_one_day_pct': open_one_day_pct, 'score': sentiment }

			
			df = pd.DataFrame(input_, index=[0])
			print(df)

			up_or_down = pickle_model.predict(df)
			print("Up or down", up_or_down)
			print(type(up_or_down))
			UD = up_or_down.tolist()[0]
			sentence = ""
			if UD == 1:
				UD = "up"
				sentence = "Wow, great news! It looks like the stock price is going to go up!"
			elif UD == 0:
				UD = "down"
				sentence = "Bummer. It looks like the stock price might go down. Do you know what short selling is?"

		return {"Stocks":stock_data_list, "Open":open_, "Close":close, "Articles":Articles, "Terms":termz, "vals":vals, "company_name":company, "prediction":UD, "predictionMessage":sentence}
		
		#return {"Hello":"ES did not CONK"}

	return {"Message":"You did not send a post chief"}		
		# There are three scenarios
		#1. The date is in the last 6 days. In this case, the data can be obtained from 






if __name__ == "__main__":
	app.run(debug=True)


