# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:02:20 2022

@author: hp
"""

import pandas as pd
import streamlit as st
import pickle
import sklearn

#st.image('img.jpg', '')

filename = 'crime_predict.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Crime Prediction System')
st.subheader("""This app takes in certain variables to enable prediction of Crime in a certain Region""")

#image = Image.open('img.jpg')
#st.image('img.jpg', '')

def user_input():
    Dates = st.text_input('choose the Date', 30, 2000)
    DayOfWeek = st.slider('slide to choose a day from sunday-saturday(0-6)', 0, 6)
    PdDistrict = st.selectbox('choose your District', options= [0,1,2,3,4,5,6,7,8,9], index=0)
    Address = st.text_input('Input your address', 100,2000)
    X= st.slider('choose X coodinate', -122.000000,-123.000000)
    Y = st.slider('choose Y coodinate', 37.000000, 38.000000)
    
    data = {'Dates': Dates,
            'DayOfWeek': DayOfWeek,
            'PdDistrict': PdDistrict,
            'Address': Address,
            'X': X,
            'Y': Y
            }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

#cc=model.predict(df)
def prediction():
    predicts = model.predict(df)
    result = ''
    if predicts == 0:
       result = 'The Crime Rate In These Region Is Low'
       #print('Thank you for filling this form. We recommend that you see a doctor immediately as you show signs of diabetes')
    else:
       result = 'The Crime Rate In These Region Is High'
    return result

#prediction button
if st.button("Predict"): 
  resultt = prediction()
  st.success(resultt)
  #st.success(cc)
        
