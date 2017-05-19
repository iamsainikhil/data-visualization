
# coding: utf-8

# # ASSIGNMENT 1

# In[5]:

import pandas as pd


# In[6]:

from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')
import numpy as np


# In[7]:

import seaborn as sns


# In[ ]:

#In the above cells, I imported libraries required for this assignment.


# In[9]:

df_math = pd.read_clipboard(header=None)


# In[ ]:

#In the above cell, I created a dataframe with the clipboard text.


# In[11]:

df_math = df_math.rename(index=int, columns={0:"Rank",1:"Country",2:"Score"})


# In[ ]:

#In the above cell, I changed the name of the columns. In this scenario, [0,1,2] are integers.


# In[13]:

df_science = pd.read_clipboard(header=None)


# In[15]:

df_science = df_science.rename(index=int, columns={0:"Rank",1:"Country",2:"Score"})


# In[19]:

df_reading = pd.read_clipboard(header=None)


# In[21]:

df_reading = df_reading.rename(index=int, columns={0:"Rank",1:"Country",2:"Score"})


# In[23]:

temp = pd.merge(df_math,df_science, on='Country', how='outer')


# In[ ]:

#In the above cell, I merged df_math & df_science dataframes based on country in the form of outer.


# In[25]:

temp = pd.merge(temp,df_reading, on='Country', how='outer')


# In[ ]:

#In the above cell, I merged tempo & df_reading dataframes based on country in the form of outer.


# In[35]:

del temp['Rank']


# In[ ]:

#In the above cell, I deleted the column with name 'Rank'.


# In[43]:

df = temp.rename(index=int, columns={"Score_x":"Math","Score_y":"Science","Score":"Reading"})


# In[45]:

df['Math'] = pd.to_numeric(df['Math'])
df['Science'] = pd.to_numeric(df['Science'])
df['Reading'] = pd.to_numeric(df['Reading'])


# In[ ]:

#In the above cell, I converted the data from string to numeric.


# In[46]:

df['Average'] = (df['Math'] + df['Science'] + df['Reading']) / 3


# In[ ]:

#In the above cell, I added a new column 'Average' which has values [mean of values in 'math','science', and 'reading']


# In[50]:

df['Rank'] = df['Average'].rank(ascending=False)


# In[ ]:

#In the above cell, I added a new column 'Rank' which has values sorted in descending order based on average.


# In[ ]:

##In the above cell, describe() gives all the statistical values related to column 'Average'.


# In[61]:

data1=df['Average']
data2=df['Math']


# In[67]:

plt.hist(data1,color='red')


# In[ ]:

#In the above cell, I created a histogram plot for 'Average'.


# In[68]:

plt.hist(data2,color='blue')


# In[ ]:

#In the above cell, I created a histogram plot for 'Math'.


# In[81]:

import numpy as np


# In[93]:

plt.title("Assignment 6")
plt.xlim(xmin=360,xmax=630)
plt.xticks(np.arange(360, 640, 30))

plt.xlabel('Average')
plt.ylabel('Math')


plt.hist(data1,alpha=0.5,color='red',label='Average',linewidth=1)
plt.hist(data2,alpha=0.5,color='blue',label='Math',linewidth=1)
plt.legend(loc='upper right')
plt.rc('lines', linewidth=1, color='r',linestyle="--")
plt.grid(True)
plt.show()


# In[ ]:

#In the above cell, I created a histogram plot with 'Average' on x-axis with red color and 'Math' on y-axis with blue color.
#I created a legend with color description in the upper right.
#I created xlimits of min=360 and max=630.
#I created xticks with 30 interval between 360 and 630.


# In[85]:

sns.distplot(df["Average"],norm_hist=True)
sns.distplot(df["Math"],norm_hist=True)


# In[ ]:

#I created the above plot using seaborn with normalized form.


# # ASSIGNMENT 2

# In[243]:

def find_outlier(string):
    outlier = []
    mean = df[string].describe()[1]
    std = df[string].describe()[2]
    for i in xrange(len(df[string])):
        n = (df[string][i])
        if abs(mean - n) > 1.8 * std:
            f =df[df[string]==n]['Country']
            outlier.append(f)
            
    print("The outliers in string are", outlier)


# In[ ]:

#In the above cell, I created a find_outlier function which takes string as column_name.
#The outliers are appended to outlier list.


# In[244]:

find_outlier("Average")
find_outlier("Math")
find_outlier("Science")
find_outlier("Reading")


# In[ ]:

#Thus, the above cell satisfies the assignment output. 
#Only exeption is name, dtype, and index of the dataframe are also included in the output.
##I tried a lot but failed. I searched a lot but couldn't got the exact output.

