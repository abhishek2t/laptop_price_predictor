# -*- coding: utf-8 -*-
import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe3.pkl','rb'))
df = pickle.load(open('df3.pkl','rb'))

st.title("Laptop Predictor")

# brand
Company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
TypeName = st.selectbox('Type',df['TypeName'].unique())

# Ram
Ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
Ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
Cpu_brand = st.selectbox('CPU',df['Cpu_brand'].unique())

HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

Gpu_brand = st.selectbox('GPU',df['Gpu_brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if Ips == 'Yes':
        Ips = 1
    else:
        Ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([Company,TypeName,Ram,weight,touchscreen,Ips,ppi,Cpu_brand,HDD,SSD,Gpu_brand,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))



