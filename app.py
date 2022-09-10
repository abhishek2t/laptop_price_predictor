import streamlit as st
import numpy as np
import pickle

pipe=pickle.load(open('pipe7.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

## now creating title

st.title("Laptop Predictor")

## brand
company=st.selectbox('Brand',df['Company'].unique())

# type of laptop

type=st.selectbox('Type',df['TypeName'].unique())

## ram

typeram=st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

## weight
weight=st.number_input('weight of the laptop')

## touchscreen

touchscreen=st.selectbox('Touchscreen',['Yes','No'])
## ips
IPS=st.selectbox('IPS',['Yes','No'])

##
screen_size=st.number_input('screen_size')

resolution=st.selectbox('SCreen Resolution',['1920X1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
## cpu

cpu=st.selectbox('brand',df['Cpu brand'].unique())

## hdd
hdd=st.selectbox('HDD in gb',[0,128,256,512,1024,2048])

## ssd
ssd=st.selectbox('SSD in gb',[0,128,256,512,1024,2048])

## gpu
gpu=st.selectbox('Gpu',df['Gpu brand'].unique())

# os
os=st.selectbox('Gpu',df['os'].unique())

## now making the button

if st.button('predict price'):
    pass




