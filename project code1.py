#!/usr/bin/env python
# coding: utf-8

# In[151]:


##check for duplicate value in the data
import pandas as pd
tweet=pd.read_csv("/Users/krishna/Desktop/Sentiment analysis project/Tweets.csv")
tweet.duplicated().sum() ##here we have used (.sum) to know that total duplicate value is 0
tweet


# In[156]:


##create a word cloud
get_ipython().system('pip install wordcloud ##this is used to install the word cloud in python')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
tweet = pd.read_csv("/Users/krishna/Desktop/Sentiment analysis project/Tweets.csv")
#tweet = tweet.transpose() ##transpose is used to change rows into columns and vise versa.
tweet.columns = ['textID', 'text', 'selected_text','sentiment']
#tweet.head()
plt.axis('off')
a=tweet['text']
wordcloud = WordCloud().generate(str(a))##here we have used (.str) to convert the data into string
plt.imshow(wordcloud)


# In[135]:


##convert the tweet into lower and upper case.
import pandas as pd
tweet=pd.read_csv("/Users/krishna/Desktop/Sentiment analysis project/Tweets.csv")
a=tweet['text']
print(a)
type(a)
a.str.upper()##by writing (.str) we have converted whole data set into str
a.str.lower()##by writing (.str) we have converted whole data set into str


# In[162]:


##Using nltk tokenize the words
##(Use nltk to tokenize words before and after converting the values to lower case)
##(and note the difference in number of tokens)
#!pip install nltk

##when data is in lower case
import nltk ##this is the library used for tokenizing.tokenizing means converting the sentence into list.
nltk.download('punkt')
import pandas as pd
tweet=pd.read_csv("/Users/krishna/Desktop/Sentiment analysis project/Tweets.csv")
a=tweet['text']
words = nltk.word_tokenize(str(a))##here (.str) is used to convert the data into string.Bec nltk converts words into list.
print(words)



# In[169]:


##when data is in upper case
import nltk ##this is the library used for tokenizing.tokenizing means converting the sentence into list.
nltk.download('punkt')
import pandas as pd
tweet=pd.read_csv("/Users/krishna/Desktop/Sentiment analysis project/Tweets.csv")
a=tweet['text']
b=a.str.upper()
print(b)
words = nltk.word_tokenize(str(b))##here (.str) is used to convert the data into string.Bec nltk converts words into list.
print(words)


# In[ ]:




