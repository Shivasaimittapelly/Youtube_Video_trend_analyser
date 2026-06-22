#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas numpy matplotlib seaborn


# In[2]:


# Import libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# Load Data set 

df = pd.read_csv("youtube.csv")

df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


# Step 7: Check Missing Values 

df.isnull().sum()


# In[9]:


# Step 8: Remove Null Values
df = df.dropna()


# In[11]:


# Checking the null values 

df.isnull().sum()


# In[13]:


# Step 9: Create Engagement Rate 
   
df['engagement_rate'] = (
   (df['likes'] + df['comment_count'])
   / df['views']
) * 100


# In[14]:


# check 

df[['views','likes','comment_count','engagement_rate']].head()


# In[15]:


# Step 10: Top 10 Most Viewed Videos
top_views = df.nlargest(10,'views')

plt.figure(figsize=(10,5))

sns.barplot(
    x='views',
    y='title',
    data=top_views
)

plt.title("Top 10 Most Viewed Videos")
plt.show()


# In[16]:


# Step 11: Top 10 Most Liked Videos

top_likes = df.nlargest(10,'likes')

plt.figure(figsize=(10,5))

sns.barplot(
    x='likes',
    y='title',
    data=top_likes
)

plt.title("Top 10 Most Liked Videos")
plt.show()


# In[17]:


# Step 12: Top Categories
# Count Categories 

category_counts = df['category_id'].value_counts()

plt.figure(figsize=(8,8))

category_counts.head(10).plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Video Categories Distribution")
plt.ylabel("")
plt.show()


# In[18]:


# Step 13: Views vs Likes Relationship

plt.figure(figsize=(8,5))

sns.scatterplot(
    x='views',
    y='likes',
    data=df
)

plt.title("Views vs Likes")
plt.show()


# In[19]:


# Step 14: Top Channels by Views

channel_views = df.groupby(
    'channel_title'
)['views'].sum().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10,5))

channel_views.plot(kind='bar')

plt.title("Top Channels By Views")
plt.show()


# In[20]:


# Step 15: Best Engagement Videos

best_engagement = df.nlargest(
    10,
    'engagement_rate'
)

best_engagement[
[
'title',
'channel_title',
'engagement_rate'
]
]


# In[21]:


# Step 16: Analyze Keywords in Titles

df['keyword'] = df['title'].str.split().str[0]


# In[22]:


# Count 
keyword_counts = df['keyword'].value_counts().head(10)

keyword_counts.plot(
    kind='bar'
)

plt.title("Top Keywords")
plt.show()


# In[23]:


# Step 17: Final Insights

# Write these:

# Insight 1
# Music and Entertainment videos dominate trending content.
# Insight 2
# Higher views usually lead to higher likes.
# Insight 3
# Certain channels consistently achieve high engagement.
# Insight 4
# Keywords such as Official, Trailer, Song, and New appear frequently in trending videos.


# In[ ]:




