#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas.io.json import json_normalize
from pymongo import MongoClient
from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression

client = MongoClient()

collection = client['test']['new_docs']

docs = list(collection.find({}))


# In[2]:


df = pd.DataFrame(docs[:8000])
sample = df[['open_ten_day_pct', 'close_ten_day_pct', 'sentiment', 'close_one_day_pct', 'open_one_day_pct']]
sample = pd.concat([sample.drop(['sentiment'], axis=1), sample['sentiment'].apply(pd.Series)], axis=1)
sample = sample.drop(['label', 'mixed'], axis=1)
x = sample #open_ten_day and sentiment
y = (df['open_tomorrow'] - df['open'])
y[y > 0] = 1
y[y <= 0] = 0
y = y.astype(int)


# In[3]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=0)


# In[4]:


logreg = LogisticRegression(solver='lbfgs', multi_class='multinomial')
logreg.fit(x_train, y_train)
y_pred=logreg.predict(x_test)

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)


# In[5]:


class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')


# In[ ]:




