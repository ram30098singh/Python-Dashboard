#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import numpy as np
from plotly import graph_objects as go


# In[14]:


st.set_page_config(page_title="Cookie Sales Performanace Dashboard",
                  page_icon="bar_chart:",
                  layout="wide")


# In[15]:


df = pd.read_csv("C:/Users/Dell/Desktop/Project_2_035043_035024_Group 3/Project_2_035043_035024_Group 3.csv")


# In[16]:


st.sidebar.header('Please Filter Here:')
Country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique())

Product = st.sidebar.multiselect(
    "Select the Product:",
    options=df["Product"].unique(),
    default=df["Product"].unique())

Date = st.sidebar.multiselect(
    "Select the Date:",
    options=df["Date"].unique(),
    default=df["Date"].unique())

df_selection = df.query(
    "Country ==@Country & Product ==@Product & Date ==@Date") 
st.dataframe(df_selection)


# In[17]:


st.title(' Cookie Sales Performanace Dashboard')
st.markdown('##')
Total_Unit_Sold= int(df_selection['Units Sold'].sum())
Total_Cost= int(df_selection['Cost'].sum())
Total_Revenue= int(df_selection['Revenue'].sum())
Total_Profit= int(df_selection['Profit'].sum())


# In[18]:


left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader('Total Unit Sold')
    st.subheader(f' {Total_Unit_Sold:,}')
with middle_column:
    st.subheader('Total Cost')
    st.subheader(f'US ${Total_Cost:,}')
with middle_column:
    st.subheader('Total Revenue')
    st.subheader(f'US ${Total_Revenue:,}')
with right_column:
    st.subheader('Total Profit')
    st.subheader(f'US ${Total_Profit:,}')
st.markdown("---")


# In[19]:


sales_by_product = df_selection.groupby(by=['Product']).sum()[['Units Sold']].sort_values(by=['Units Sold'])
fig_Product_sales = px.bar(
    sales_by_product,
    x='Units Sold', y = sales_by_product.index,
    orientation='h', title="<b>Sales by Product</b>",
    color_discrete_sequence=["#0083B8"]* len(sales_by_product),
    template="plotly_white",)


# In[20]:


bar_chart=px.bar(df_selection, x="Country", y="Units Sold", color="Product", title="Unit Sold Country & Product wise")

left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart, use_container_width=True)
right_column.plotly_chart(fig_Product_sales, use_container_width=True)

Pie_chart= px.pie(df_selection, title='Unit Sold Product wise', values='Units Sold', names='Product')
Revenue_Country =px.pie(df_selection, title='Revenue generated Region Wise', values='Revenue', names='Country')

right_column, middle_column, left_column= st.columns(3)
right_column.plotly_chart(Pie_chart, use_container_width=True)
left_column.plotly_chart(Revenue_Country, use_container_width=True)


# In[21]:


bar_chart1=px.bar(df_selection, x="Country", y="Revenue", color="Product", title="Total Revenue Country & Product wise")
bar_chart2=px.bar(df_selection, x="Country", y="Profit", color="Product", title="Total Profit Country & Product wise")

left_column, right_column = st.columns(2)
left_column.plotly_chart(bar_chart1, use_container_width=True)
right_column.plotly_chart(bar_chart2, use_container_width=True)


# In[22]:


import plotly.graph_objects as go
map = go.Figure(data=go.Choropleth(
    locations=df['Country'],
    z = df['Units Sold'],
    locationmode = 'country names', 
    colorscale = 'jet',
    colorbar_title = "Units Sold",
))

map.update_layout(
    title = dict(text = '<b>Units Sold by Countries</b>',
    x = 0.5)
)

map.show()


# In[23]:


left_column = st.columns(1)
st.plotly_chart(map, use_container_width=True)


# In[24]:


hide_st_style = """
            <style>
            #mainMenu {Visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:




