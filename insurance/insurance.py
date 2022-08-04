# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:28:26 2022

@author: HP
"""

import pandas as pd
import streamlit as st
import pickle

filename = 'insurance_prediction.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Insurance Policy Prediction App')
st.subheader("""This app takes in certain variables to enable prediction whether or not a building is insured""")
image = Image.open('OIP.jpg')
st.image(image, '')


def user_input():
    YearObservation = st.slider('What year was your building insured', 2012, 2016)
    Insured_Period = st.slider('What is the duration of insurance policy', 0.0, 10.0)
    Residential = st.selectbox('Is your building residential or not?', options= [0,1], index=0)
    building_fenced = st.selectbox('Is your building fenced or not?', options= [0,1], index=0)
    settlement = st.selectbox('Is your area rural or urban', options= [0,1], index=0)
    building_dimension = st.slider('What is the dimension of your building', 1.0, 30000.0)
    building_type = st.selectbox('What building type is yours', options= [0,1,2,3], index=0)
    date_of_occ = st.slider('Which date did you move in?', 1545.0, 2016.0)
    Geo_code = st.slider('What is the geographical code of the building', 0.0, 1400.0)
    
    data = {'Year of Observation': YearObservation,
            'Insurance Period': Insured_Period,
            'Residential': Residential,
            'Building Fenced': building_fenced,
            'Settlement': settlement,
            'Building Dimesion': building_dimension,
            'Building Type': building_type,
            'Date of Occupancy': date_of_occ,
            'Geographical Code': Geo_code}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

     
def prediction():
    predict_ = model.predict(df)
    result = ''
    if predict_ == 0:
       result = 'Not Qualified'
       #print('Thank you for filling this form. We recommend that you see a doctor immediately as you show signs of diabetes')
    else:
       result = 'Qualified'
    return result

#prediction button
if st.button("Predict"): 
  result = prediction()
  st.success('Thank you for filling this form. You are {}'.format(result))
        