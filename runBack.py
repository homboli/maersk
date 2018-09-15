
# coding: utf-8

# In[70]:


import pandas as pd
import matplotlib.pyplot as plt
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
import numpy as np
import pickle


# In[71]:


df = pd.read_csv("input.csv")
df2 = pd.read_csv("schedule.csv")
df2 = pd.concat([df2,df], axis = 0)


# In[72]:


X = df2
print(X.columns)
X = pd.get_dummies(X,prefix=['Company', 'Truck', 'Driver' ])
X = X.iloc[-1:, :]


# In[73]:


# regressor = DecisionTreeRegressor(random_state=0)
regressor  = pickle.load( open( "save.p", "rb" ) )


# In[74]:


X = X.drop(['pred', 'ActualArrival'], axis = 1)


# In[75]:


y_pred = regressor.predict(X)


# In[76]:


df = pd.read_csv("input.csv")
outFinal = pd.read_csv('schedule.csv')
df['pred'] = np.round(y_pred)


# In[77]:


outFinal = pd.concat([df,outFinal], axis = 0 )
outFinal = outFinal.sort_values('pred')
outFinal.to_csv('schedule.csv', index = False)


# In[78]:


len(outFinal)

