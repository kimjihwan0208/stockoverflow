import os
import string
import json
import requests
from datetime import datetime, timedelta
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from pandas_datareader.data import get_data_yahoo as get_stock_data #stock symbol, start date, end date, interval = 'd'
import pandas as pd
import yfinance as yf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import stop_words
import re

'''@adi
from sklearn.decomposition import PCA
pca = PCA(n_components=15, svd_solver='full')
pcs = pca.transform(returnsClosePrevRaw1)
# the market return is the first PC
mkt_return = pcs[:,0].reshape(num_days,1)

# the betas of each stock to the market return are in
# the first column of the components
mkt_beta = pca.components_[0,:].reshape(num_stocks,1)

# the market portion of returns is the projection of one onto the other
mkt_portion = mkt_beta.dot(mkt_return.T).T

# ...and the residual is just the difference
residual = returnsClosePrevRaw1 - mkt_portion

residual is returnsPrevCloseMktres
'''

tfidf_vectorizer=TfidfVectorizer(stop_words=stop_words.ENGLISH_STOP_WORDS, use_idf=True,token_pattern=r'(?u)\b[A-Za-z]+\b')

yf.pdr_override()

from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays(start='2006-01-01', end='2015-12-31').to_pydatetime().tolist()
saturday = 5
sunday = 6

authenticator = IAMAuthenticator('')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

# natural_language_understanding.set_service_url('{url}')

High = 0
Low = 1       
Open = 2     
Close = 3  
Volume = 4  
Adj = 5 
Adj_Close = 6


def get_percentage_change(previous_number:float, current_number:float) -> float:
    if previous_number == current_number:
        return 0
    try:
        return ((current_number - previous_number) / previous_number) * 100.0
    except ZeroDivisionError:
        return float('inf')
  




path = './financial-news-dataset-master/ReutersNews106521'

def readContent(relPath):
    global count
    if(relPath.find('.DS') > -1):
        return
    files = os.listdir(relPath)
    articles = []
    for f in files:
        if(f.find('.tar') > -1 or f.find('.DS') > -1):
            continue
        pwf = open(relPath + '/' + f, 'r')
        lines = pwf.readlines()
        if(len(lines) < 7): #skip if the article is missing
            continue
        lines.append('\n')
        article = ''
        
        for line in lines[7:-1]:
            article = article + str(line.replace('\n', ' '))
    
        articles.append(article)

    tfidf_vectorizer_vectors=tfidf_vectorizer.fit_transform(articles) #what if it's empty?
    

    fileNum = 0
    for f in files:
        if(f.find('.tar') > -1 or f.find('.DS') > -1):
            continue
        pwf = open(relPath + '/' + f, 'r')
        lines = pwf.readlines()
        
        col2 = lines[2][3: lines[2].find('\n')].replace(',', '') # date
        col2 = col2[4:-4]
        col2 = datetime.strptime(col2, '%b %d %Y %I:%M%p')
        print(col2)
        print(lines[2])
        col3 = lines[0][3: lines[0].find('\n')].replace(',', '') # title

        # news_summary = lines[7]
        # news_body = lines[9]


        # complete_text = lines[7]

        if(len(lines) < 7):
            continue
        lines.append('\n')
        limit = lines[7: ].index('\n')

        data = ''
        for i in range(7, 7 + limit):
            data = data + str(lines[i].replace('\n', ' '))

        # print(data)

        #1. Get the companies
        response = natural_language_understanding.analyze(
        text=data,
        features=Features(
            entities=EntitiesOptions(sentiment=True),
            # keywords=KeywordsOptions(emotion=True, sentiment=True,
                                #)
                                )).get_result()

        # print(data)
        entities = response['entities']
        # print(entities)
        # print(len(entities))
        # print(type(entities))
        print(col2)
        companies = []
        documents = []
        for entity in entities:
            if entity["type"] == "Company":
                if entity.get("text") != "Bloomberg" and entity.get("text") != "Reuters": 
                    if entity.get("disambiguation"):
                        if entity.get("disambiguation").get("name") != "Reuters" and entity.get("disambiguation").get("name") != "Bloomberg":
                            entity["text"] = entity["text"].translate(str.maketrans('', '', string.punctuation))
                            companies.append(entity) 

        print(companies)
        for company in companies:
             stock_symbol = requests.get("http://d.yimg.com/aq/autoc?query=" + company["text"] +  "&region=US&lang=en-US").json()
             
             
             
             if stock_symbol['ResultSet']['Result']:
                stock_symbol = stock_symbol['ResultSet']['Result'][0]['symbol']
                print(stock_symbol)
                start_date = end_date = col2.strftime('%m/%d/%Y')
                start_datetime = col2
                
                #first, there needs to be a check if today is either a weekend or a federal holiday. 
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

                if yesterday_stock_data is not None:
                    yest_stock_dict = yesterday_stock_data.to_dict()
                    ten_days_list = ten_days_stock_data.values.tolist()

                    open_ = yest_stock_dict["Open"][pd.Timestamp(datetime.combine(start_datetime, datetime.min.time()))]
                    close = yest_stock_dict["Close"][pd.Timestamp(datetime.combine(start_datetime, datetime.min.time()))]
                    volume = yest_stock_dict["Volume"][pd.Timestamp(datetime.combine(start_datetime, datetime.min.time()))]


                    open_yesterday = yest_stock_dict["Open"][pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time()))]
                    close_yesterday = yest_stock_dict["Close"][pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time()))]
                    volume_yesterday = yest_stock_dict["Volume"][pd.Timestamp(datetime.combine(yesterday_datetime, datetime.min.time()))]

                    open_tomorrow = yest_stock_dict["Open"][pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time()))]
                    close_tomorrow = yest_stock_dict["Close"][pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time()))]
                    volume_tomorrow = yest_stock_dict["Volume"][pd.Timestamp(datetime.combine(tomorrow_datetime, datetime.min.time()))]

                    open_ten_days = ten_days_list[0][Open]
                    close_ten_days = ten_days_list[0][Close]
                    volume_ten_days = ten_days_list[0][Volume]

                    print(open_)
                    print(close)
                    print(volume)

                    print(open_yesterday)
                    print(close_yesterday)
                    print(volume_yesterday)

                    print(open_tomorrow)
                    print(close_tomorrow)
                    print(volume_tomorrow)

                    print(open_ten_days)
                    print(close_ten_days)
                    print(volume_ten_days)


                    close_ten_day_pct = get_percentage_change(close_ten_days,close)
                    open_ten_day_pct = get_percentage_change(open_ten_days, open_)

                    close_one_day_pct = get_percentage_change(close_yesterday,close)
                    open_one_day_pct = get_percentage_change(open_yesterday, open_)
                    vector_tfidfvectorizer = tfidf_vectorizer_vectors[fileNum]
                    df = pd.DataFrame(vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
                    df.sort_values(by=["tfidf"],ascending=False)
                    #print(df)



        if count == 30:
            break

        count += 1
        fileNum = fileNum + 1
        

files = os.listdir(path)
count = 0
for i in files:
    readContent(path + '/' + i)
    break
