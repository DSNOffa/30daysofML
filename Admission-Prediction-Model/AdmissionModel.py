# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:46:34 2022

@author: Bin Imam
"""
import pandas as pd
import streamlit as st
import pickle
import sklearn
from sklearn.linear_model import LinearRegression


file_name = 'admission_model.sav'
model = pickle.load(open(file_name, 'rb'))

st.title('GRADUATE ADMISSION PREDICTOR')
st.subheader('''This model aims to bring students closer to their university of choice through a robust evaluation of their profiles. The model takes in certain parameters relevant for graduate admission to predict a student\'s chance of admission.''')

def user_input():
    GRE_Score = st.text_input('Enter your GRE score out of 340')
    TOEFL_Score = st.text_input('Enter your TOEFL score out of 120')
    University_Rating = st.selectbox('Select your university rating on a scale of 0-5', options = [0,1,2,3,4,5], index = 0)
    SOP = st.slider('Rate your Statement of Purpose on scale of 0-5', 0.5, 5.0)
    LOR = st.slider('Rate your Letter of Recommendation on a scale of 0-5', 0.5, 5.0)
    CGPA = st.text_input('Enter your CGPA on a scale of 1-10')
    Research = st.selectbox('Do you have a published Research paper?', options= ['Yes', 'No'], index = 0) 

    if (Research == 'Yes'):
        Research = 0
    else:
        Research = 1

    data = {'GRE': GRE_Score,
            'TEOFL': TOEFL_Score,
            'University Rating': University_Rating,
            'SOP': SOP,
            'LOR': LOR,
            'CGPA': CGPA,
            'Research': Research,}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

if st.button("Predict"):
    predict_ = model.predict(df)
    result = round(predict_[0],2) *100
    st.success('Your chance of admission is   {}%'.format(result))

