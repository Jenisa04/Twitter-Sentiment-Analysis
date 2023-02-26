#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
ds = pd.read_csv("/Users/satyasanegepalli/Downloads/Tweets.csv")

#deleting null values
bool_series = pd.isnull(ds["text"])
length = len(bool_series)
i=1
while i<length:
    if bool_series[i]=="False":
        ds.drop(i,axis=0,inplace=True)

#tag_id
ds['tag_id'] = ds['sentiment']
for i in ds.index:
    if ds['sentiment'][i] == "neutral":
        ds['tag_id'][i] = 0
    elif ds['sentiment'][i] == "positive":
        ds['tag_id'][i] = 1
    elif ds['sentiment'][i] == "negative":
        ds['tag_id'][i] = 2
