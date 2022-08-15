# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:11:50 2022

@author: User
"""

import pandas as pd
import streamlit as st
import sklearn
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
image = Image.open('hos.jpg')

st.image(image)

filename = 'heart_attack.sav'
model = pickle.load(open(filename, 'rb'))

#####with st.sidebar:
selected = option_menu(
    menu_title = None, #this is required
    options = ['BMI CALCULATOR', 'HEART DISEASE PREDICTION'], #required
    icons = ['calculator', 'activity'], #optional
    menu_icon = 'cast', #optional
    default_index = 0,
    orientation = 'horizontal',
    )


#image = ima.open('ima.jpg')
#st.image(image, '')

if selected == 'BMI CALCULATOR':
    st.title('CALCULATE YOUR BMI HERE')
    def BMI(Height, Weight):
        return round(Weight / (Height/100)**2, 2)
    
    Height = st.number_input('Enter your height in cm: ', 1, 272)
    Weight = st.number_input('Enter your weight in Kg: ', 1, 635)
   
    bmi = BMI(Height, Weight)
   
    success = st.button('Calculate')
    if(success):
        if bmi <= 18.5:
            st.success('Your BMI is {}. You\'re underweight'.format(bmi))
        elif 18.5 < bmi <= 24.9:
            st.success('Your BMI is {}. Your weight is normal'.format(bmi))
        elif 25 < bmi <= 29.29:
            st.success('Your BMI is {}. You\'re overweight'.format(bmi))
        else:
            st.success('Your BMI is {}. You\'re obese'.format(bmi))
        
        
        
    
                    

            
if selected == 'HEART DISEASE PREDICTION':
    st.title('HEART DISEASE OR ATTACK.')
    st.subheader(""" This App is used to Predict if an Individual is prone to Heart Attack/Disease.""")
    def user_input():
        HighBP = st.selectbox('Do you have High Blood Pressure?', options = ['YES', 'NO'], index = 0)
        HighChol = st.selectbox('Do you have High Cholesterol?', options =['YES', 'NO'], index = 0 )
        CholCheck = st.selectbox('Cholesterol check?', options = ['Cholesterol check last in 5 years', 'No cholesterol check in 5 years'], index = 0)
        BMI = st.number_input('Your BMI (BODY-MASS-INDEX)? ', step=1.,format="%.2f")
        Smoker = st.selectbox('Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]', options = ['YES', 'NO'], index = 0)
        Stroke = st.selectbox('Have you ever had a Stroke?', options = ['YES', 'NO'], index = 0)
        Diabetes = st.selectbox('What form of Diabetes do you have?', options = ['No Diabetes', 'Prediabetes', 'Diabetes'], index = 0)
        PhysActivity = st.selectbox('Have you partaken in any form of physical activity in past 30 days - not including job?', options = ['YES', 'NO'], index = 0)
        Fruits = st.selectbox('Do you consume Fruit 1 or more times per day?', options = ['YES', 'NO'], index = 0)
        Veggies = st.selectbox('Do you consume Vegetables 1 or more times per day?', options = ['YES', 'NO'], index = 0)
        HvyAlcoholConsump = st.selectbox('Are you a heavy drinker (adult men having more than 14 drinks per week and adult women > having more than 7 drinks per week)?', options = ['YES', 'NO'], index = 0)
        AnyHealthcare = st.selectbox('Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.?', options = ['YES', 'NO'], index = 0)
        NoDocbcCost = st.selectbox('Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?', options = ['YES', 'NO'], index = 0)
        GenHlth = st.selectbox('What would you rate your General Health?', options =['EXCELLENT', 'VERY GOOD', 'GOOD', 'FAIR', 'POOR'], index = 0)
        MentHlth = st.slider('Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?', 0, 30)
        PhysHlth = st.slider('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?', 0, 30)
        DiffWalk = st.selectbox('Do you have serious difficulty walking or climbing stairs?', options = ['YES', 'NO'], index = 0)
        Sex = st.selectbox('Are you a Male or Female?', options = ['MALE', 'FEMALE'], index = 0)
        Age = st.selectbox('What range of age do you fall between?', options = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+'], index = 0)
        Education = st.selectbox('What is your highest Educational status attained?', options = ['NEVER ATTENDED SCHOOL','ELEMENTARY', 'SOME HIGH SCHOOL', 'HIGH SCHOOL GRADUATE', 'SOME COLLEGE', 'SOME COLLEGE GRADUATE'], index = 0)
        Income = st.selectbox('What is your monthly income?', options = ['$0 - $10000', '$10001 - $15000', '$15001 - $20000', '$20001 - $25000', '$25001 - $35000','$35001 - $50000', '$50001 - $75000', '$75001+'], index = 0)
        
        if (HighBP == 'YES'):
            HighBP = 1
        else:
            HighBP = 0
            
        if (HighChol == 'YES'):
            HighChol = 1
        else:
            HighChol = 0
            
        if (CholCheck == 'Cholesterol check in 5 years'):
            CholCheck = 1
        else:
            CholCheck = 0
            
        if (Smoker == 'YES'):
            Smoker = 1
        else:
            Smoker = 0
            
        if (Stroke == 'YES'):
            Stroke = 1
        else:
            Stroke = 0
            
        if (Diabetes == 'No Diabetes'):
            Diabetes = 0
        elif (Diabetes == 'Prediabetes'):
            Diabetes = 1
        else:
            Diabetes = 2
            
        if (PhysActivity == 'YES'):
            PhysActivity = 1
        else:
            PhysActivity = 0
            
        if (Fruits == 'YES'):
            Fruits = 1
        else:
            Fruits = 0
            
        if (Veggies == 'YES'):
            Veggies = 1
        else:
            Veggies = 0
            
        if (HvyAlcoholConsump == 'YES'):
            HvyAlcoholConsump = 1
        else:
            HvyAlcoholConsump = 0
            
        if (AnyHealthcare == 'YES'):
            AnyHealthcare = 1
        else:
            AnyHealthcare = 0
            
        if (NoDocbcCost == 'YES'):
            NoDocbcCost = 1
        else:
            NoDocbcCost = 0
            
        if (GenHlth == 'EXCELLENT'):
            GenHlth = 1
        elif (GenHlth == 'VERY GOOD'):
            GenHlth = 2
        elif (GenHlth == 'GOOD'):
            GenHlth = 3
        elif (GenHlth == 'FAIR'):
            GenHlth = 4
        else:
            GenHlth = 5   
               
        if (DiffWalk == 'YES'):
            DiffWalk = 1
        else:
            DiffWalk = 0
            
        if (Sex == 'MALE'):
            Sex = 1
        else:
            Sex = 0
            
        if (Age == '18-24'):
            Age = 1
        elif (Age == '25-29'):
            Age = 2
        elif (Age == '30-34'):
            Age = 3
        elif (Age == '35-39'):
            Age = 4
        elif (Age == '40-44'):
            Age = 5
        elif (Age == '45-49'):
            Age = 6
        elif (Age == '50-54'):
            Age = 7
        elif (Age == '55-59'):
            Age = 8
        elif (Age == '60-64'):
            Age = 9
        elif (Age == '65-69'):
            Age = 10
        elif (Age == '70-74'):
            Age = 11
        elif (Age == '75-79'):
            Age = 12
        else:
            Age = 13
            
        if (Education == 'NEVER ATTENDED SCHOOL'):
            Education = 1
        elif (Education == 'ELEMENTARY'):
            Education = 2
        elif (Education == 'SOME HIGH SCHOOL'):
            Education = 3
        elif (Education == 'HIGH SCHOOL GRADUATE'):
            Education = 4
        elif (Education == 'SOME COLLEGE'):
            Education = 5
        else:
            Education = 6
            
        if (Income == '$0-$10000'):
            Income = 1
        elif (Income == '$10001 - $15000'):
            Income = 2
        elif (Income == '$15001 - $20000'):
            Income = 3
        elif (Income == '$20001 - $25000'):
            Income = 4
        elif (Income == '$25001 - $35000'):
            Income = 5
        elif (Income == '$35001 - $50000'):
            Income = 6
        elif (Income == '$50001 - $75000'):
            Income = 7
        else:
            Income = 8
        
        
        data = {'High Blood Pressure': HighBP,
                'High Cholesterol': HighChol,
                'Cholesterol Check' : CholCheck,
                'Body Mass Index' : BMI,
                'Smoker' : Smoker,
                'Stroke' : Stroke,
                'Diabetes' : Diabetes,
                'Physical Activity' : PhysActivity,
                'Fruits' : Fruits,
                'Vegetables' : Veggies,
                'Heavy Alcohol Consumption' : HvyAlcoholConsump,
                'Any HealthCare' : AnyHealthcare,
                'No Doctor Because of Cost' : NoDocbcCost,
                'General Health Scale' : GenHlth,
                'Mental Health Scale' : MentHlth,
                'Physical Health Scale' : PhysHlth,
                'Difficulty Walking' : DiffWalk,
                'Sex' : Sex,
                'Age' : Age,
                'Education' : Education,
                'Income' : Income
                }
        
        features = pd.DataFrame(data, index = [0])
        return features
    
    df = user_input()
    
    def prediction():
        predict_ = model.predict(df)
        result = ''
        if predict_ == 0:
            result = 'This AI algorithm predicts you to not be susceptible to coronary heart disease(CHD) or myocardial infraction(MI)'
        else:
            result = 'This AI algorithm predicts you to being susceptible to coronary heart disease(CHD) or myocardial infraction(MI)'
        return result
    
    
    if st.button('Predict'):
        result = prediction()
        st.success('Thank you for filling this form.')
        st.success(' {}'.format(result))