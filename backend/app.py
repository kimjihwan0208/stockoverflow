from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


cluster = MongoClient("mongodb+srv://adiach1:1234@cluster0-jgwg7.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

post = {"_id": 4, "name":"Aditya", "score":1}

collection.insert_one(post)

@app.route("/", methods=['GET', 'POST'])
def main():
	
	return 'Hi JiHwan'


if __name__ == "__main__":
	app.run(debug=True)


