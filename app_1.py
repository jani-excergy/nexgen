# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:47:40 2021

@author: varma
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import math
import seaborn as sns


pickle_in = open("best_model_latest.pkl","rb")
model=pickle.load(pickle_in)



uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    #df=df.drop(['Unnamed: 0'],axis=1)
    df=df.sort_values(by=['Created Date'])
    
    df['Created Date']=pd.to_datetime(df['Created Date'])
    
    
    
    
    
    
    df['month'] = df['Created Date'].dt.month
    df['weekday'] = df['Created Date'].dt.dayofweek

    df['quarter'] = df['Created Date'].dt.quarter
    
    
    date=df['Created Date']
    
    df=df.drop(['Created Date'],axis=1)
    
    
    
    df['month_cos']= np.cos(2 * np.pi * (df['month']/12))
    df['weekday_sin'] = np.sin(2 * np.pi * (df['weekday']/7))
    df['quarter_sin'] = np.sin(2 * np.pi * (df['quarter']/4))
    
    
    df=df.drop(['month',  'weekday', 'quarter'],axis=1)
    
    
    
    
    prediction=model.predict(df)
    
    df['pred_Income']=prediction
    
    new_df=pd.DataFrame({'Date':date,'Projected Revenue':prediction})
    
    new_df = new_df.rename(columns={'Date':'index'}).set_index('index')
    
    
    
    st.line_chart(new_df)
    
    

    
   
    st.write('THE PROJECTED REVENUE $ ',round(sum(prediction)))
    


    
    
    
    
    
    
    
    
    
    


    
