#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
table = pd.read_csv(r"C:\Users\wrsto\Desktop\Tweets.csv")
count = table['sentiment'].value_counts()
total_count = len(table)
neutral_count = count[0]
positive_count = count[1]
negative_count = count[2]
neutral_percentage = (round((neutral_count/total_count)*100))
positive_percentage = (round((positive_count/total_count)*100))
negative_percentage = (round((negative_count/total_count)*100))


# In[ ]:




