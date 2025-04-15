#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"Funnel Analysis by Alankrati"


# In[1]:


import pandas as pd


# In[7]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
import plotly.graph_objs as go
import plotly.offline as py
import plotly.express as px


# In[4]:


import warnings
warnings.filterwarnings('ignore')


# In[6]:


get_ipython().system('pip install plotly')


# In[8]:


df = pd.read_csv('user_data.csv', delimiter=',', encoding='ISO-8859-2')
pd.set_option('display.max_columns', None)
df.tail()


# In[10]:


#no missing values
df.isnull().sum()


# In[13]:


df["stage"].value_counts().plot.barh(color=['pink', '#f5005a', '#006400', '#9932CC', '#2F4F4F', 'blue' ], title='Funnel Analysis Stages')


# In[14]:


df["conversion"].value_counts()


# In[16]:


dfgr = df.groupby('stage').count()['conversion'].reset_index().sort_values(by='conversion',ascending=False)
dfgr


# In[17]:


import plotly.express as px
data = dict(
    number=[10000, 5000, 1500, 450, 225],
    stage=["homepage", "product_page", "purchase", "checkout", "cart"])
fig = px.funnel(data, x='number', y='stage')
fig.show()


# In[18]:


from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["homepage", "product_page", "purchase", "checkout", "cart"],
    x = [10000, 5000, 1500, 450, 225],
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65, marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
    "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )

fig.show()


# In[22]:


#Basic Area Funnel Plot with plotly.express
import plotly.express as px
fig = px.funnel_area(names=["homepage", "product_page", "purchase", "checkout", "cart"],
                    values=[10000, 5000, 1500, 450, 225])
fig.show()


# In[21]:


#Basic Area Funnel Plot with go.Funnelarea
from plotly import graph_objects as go

fig = go.Figure(go.Funnelarea(
    text = ["homepage", "product_page", "purchase", "checkout", "cart"],
    values = [10000, 5000, 1500, 450, 225]
    ))
fig.show()


# In[23]:


from plotly import graph_objects as go

fig = go.Figure(go.Funnelarea(
      values = [10000, 5000, 1500, 450, 225], text = ["homepage", "product_page", "purchase", "checkout", "cart"],
      marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
                "line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat"], "width": [0, 1, 5, 0, 4]}},
      textfont = {"family": "Old Standard TT, serif", "size": 13, "color": "black"}, opacity = 0.65))
fig.show()


# In[24]:


from plotly import graph_objects as go

colors = ["gold", "gold", "lightgreen", "lavender"]

fig = go.Figure(
    go.Funnelarea(
        labels=["homepage", "product_page", "purchase", "checkout", "cart"],
        values=[10000, 5000, 1500, 450, 225],
        textfont_size=20,
        marker=dict(colors=colors, pattern=dict(shape=["", "/", "", ""])),
    )
)
fig.show()


# In[ ]:




