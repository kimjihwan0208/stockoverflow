from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import yfinance as yf
yf.pdr_override()
app = Flask(__name__)
cluster = MongoClient("mongodb+srv://adiach1:1234@cluster0-jgwg7.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

@app.route("/", methods=['GET', 'POST'])
def main():
	
	if request.method == 'POST':

		dateOne = request.form.get('date') # should be a datetime object

		Nov_Six = datetime(2006,11,13)


		NSM = datetime.combine(Nov_Six, datetime.min.time())
		NSMax = datetime.combine(Nov_Six, datetime.max.time())


		b = collection.find({
			"date":{"$gte": NSM,
					"$lt": NSMax}})
		print("b is")
		print(b)

		a = list(b)
		print("a is")
		c= []
		for i in a:
			c.append(i["stock_symbol"])
		return {"Stocks":c}

	return {"Hello":"World"}
		# There are three scenarios
		#1. The date is in the last 6 days. In this case, the data can be obtained from 






if __name__ == "__main__":
	app.run(debug=True)


