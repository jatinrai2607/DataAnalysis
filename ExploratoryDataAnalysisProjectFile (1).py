#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv("Diwali Sales Data.csv", encoding='unicode_escape')
df.head()


# In[3]:


df.info()


# In[4]:


#dropping or deleting the column which making no sense in DataFrame, inplace keword save the action 

df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[5]:


df.info()


# In[6]:


df.isnull()
#Tells about the Null values present in the DataFrame


# In[7]:


df.isnull().sum()
#sum() method will show the total Null values


# In[8]:


df.dropna(inplace=True)
#Deleted All the null values present in the DataFrame


# In[9]:


df.isnull().sum()


# In[10]:


df['Amount']= df['Amount'].astype('int')

#Changed the DataType of column Name Amount from float to int 


# In[11]:


df['Amount'].dtype


# In[12]:


df.columns


# In[13]:


df.rename(columns={'Marital_Status':'Shaadi'})
#Rename the Column


# In[14]:


df.describe() 
#The describe() method returns description of the data in the DataFrame. 
#The description contains these information for each column: count -
#The number of not-empty values. mean - The average (mean) value. std - The standard deviation.


# In[15]:


df[['Age','Amount','Orders']].describe()
#Describe for the specific values


# In[16]:


#Exploratory Data Analysis
df.columns


# In[17]:


ax=sns.countplot(x='Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)
    
     #Creating graph through we are able to visualize the Male and female count


# In[18]:


sale_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sale_gen
#Grouping by Gender is similar as we do in Sql


# In[19]:


sns.barplot(x='Gender',y='Amount', data=sale_gen)
#Through this graph we can see that Female  is the majority in the shopping 


# In[20]:


df.columns


# In[21]:


ax=sns.countplot(data=df, x='Age Group', hue='Gender')
#Created the plot on the basis of Age group and clearly see the number of female and male
#Female the fast movers in the concern of spending.
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


#Total Amount vs Age group
sale_age=df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sale_age )
#Clearly can see that Age group of 26 to 35 spent the most money


# In[23]:


#orders bs State
sale_state=df.groupby('State', as_index=False)['Orders'].sum().sort_values('Orders', ascending =False)
#sales data according to states

sns.set(rc={'figure.figsize':(25,7)})
sns.barplot(x='State', y='Orders' ,data=sale_state)
#we can  see Up state has spent most on the shopping 


# In[24]:


#Totol Amounts/top sales from states
sales_state=df.groupby('State', as_index=False)['Amount'].sum().sort_values('Amount', ascending=False)

sns.barplot(data=sales_state, x='State', y='Amount')

#Below Graph is showing clearly that UP, Maharastra , Karnatka has most orders respectively.


# In[25]:


#Plotting on the basis of Marital Status

ax=sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(5,5)})

for bars in ax.containers:
    ax.bar_label(bars)

#6518 People are married     


# In[26]:


sales_Marital=df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values('Amount' , ascending= False)

sns.barplot(data=sales_Marital , x='Marital_Status', y='Amount', hue='Gender')


# In[27]:


#From the above graph we can see that most of the buyers are married(Women) and they have high purchasing Power


# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
sns.countplot(data=df, x='Occupation')


# In[29]:


sales_occp=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values('Amount',ascending=False)
 
sns.barplot(data=sales_occp, x='Occupation',y='Amount')


# In[30]:


#From the above graph most buyers are from IT sector , Healthcare and aviation industry


# In[31]:


#Product category
sns.set(rc={'figure.figsize':(25,7)})
ax=sns.countplot(data=df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


sale_pc=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values('Amount', ascending=False)

sns.barplot(data=sale_pc, x='Product_Category', y='Amount')


# In[33]:


#From the above graph we can state that most sold product is Food, Clothing, and Electronic catergory


# In[34]:


df.columns


# In[35]:


sale_PI=df.groupby('Product_ID', as_index=False)['Orders'].sum().sort_values('Orders', ascending = False).head(10)

sns.barplot(data=sale_PI, x='Product_ID', y='Orders')


# In[36]:


#Conclusion

#Married women from the age group of 26-35 from UP, Maharastra and Karnatka working IT, Healthcare and
#Aviation are more likely to buy Products from Food, clothing and Electronics category

