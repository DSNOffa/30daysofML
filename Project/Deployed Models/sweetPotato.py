# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:55:52 2022

@author: User
"""

import pandas as pd
import streamlit as st
import pickle
import sklearn

filename = "sweet.sav"
model = pickle.load(open(filename, "rb"))


y_train = "y.sav"
pred = pickle.load(open(y_train, "rb"))

X_train = "X.sav"
fita = pickle.load(open(X_train, "rb"))


st.title("Sweet Potato Marketable Yield Prediction Application")
st.subheader("This app takes in certain variables to enable the prediction of marketable yield of Orange Flesh Sweet Potato in contrast with White Flesh Sweet Potato")
st.info("The experiment was conducted in two different locations, Cameroon (Nkolbisson) and Tanzania (Njombe)")

def userInput():
    Location = st.selectbox("Where is the location of the farm - Input either 0 or 1, 1 is Nkolbisson and 0 is Njombe ", options = [0 , 1], index = 0)
    Soil = st.selectbox("What type of soil was utilized? - Input either 0 or 1 - 1 is Nitisol and 0 is Andosol ", options = [0 , 1], index = 0)
    Varient = st.selectbox("Is the potato White Fleshed or Orange Fleshed? - Input either 0 or 1 - 1 is Orange Fleshed and 0 is White Fleshed ", options = [0 , 1], index = 0)
    Fertilizer = st.number_input("What fertilizer was used? - The fertilizers tested are:- Control, FC, NPK20-10-10, PL, Tithonia, NPK6-15-28, RHB, FC/NPK20-10-10, PL/NPK20-10-10, RHB/NPK20-10-10 - Input a number from 0 to 9 respectively", 0, 9)
    Reps = st.selectbox("Is it the first rep, the second rep or the third rep? - Input either 0, 1 or 2 - 0 is the first rep, 1 is the second rep and 2 is the third rep", options = [0 , 1], index = 0)
    Branches = st.number_input("How many branches did the plant have in the selected rep?  - Input any number from 2 to 8 - The numbers can either be integers or decimals", 2, 8)
    Stem = st.number_input("What is the length of the stem in the selected rep? - Input any number from 70cm to 400cm - The numbers can either be integers or decimals", 70, 400)
    Leaf = st.number_input("What is the index of the leaf area? - Input any number from 1 to 7 - The numbers can either be integers or decimals", 1, 7)
    Petoile = st.number_input("What is the petoile length of the leaf? - Input any number from 20cm to 40cm - The numbers can either be integers or decimals", 20, 40)
    Root = st.number_input("What is the weight of the adventitious root? - Input any number from 0kg to 1kg - The numbers can either be integers or decimals", 0, 1)
    Biomass = st.number_input("What is the weight of the dry biomass? - Input any number from 1kg to 4kg - The numbers can either be integers or decimals", 1, 4)
    totalRoot = st.number_input("What is the total storage weight of the roots? - Input any number from 1kg to 20kg - The numbers can either be integers or decimals", 1, 20)
    marketRoot = st.number_input("What is the total storage weight of the marketable roots? - Input any number from 1kg to 20kg - The numbers can either be integers or decimals", 1, 20)
    totalNumber = st.number_input("What is the total number of the roots stored? - Input any number from 1kg to 70kg - The numbers can either be integers or decimals", 1, 70)
    
    
    
    data = {
        "location" : Location,
        "soilType": Soil,
        "varietalCode": Varient,
        "fertilizerCode": Fertilizer,
        "reps": Reps,
        "branchNumber": Branches,
        "lengthMainStemCM" : Stem,
        "leafAreaIndex": Leaf,
        "petoileLength_CM": Petoile,
        "weightAdventitousRootsKG": Root,
        "dryBiomassKG": Biomass,
        "totalWeightStorageRootsKG": totalRoot,
        "weightMarketableStorageRootsKG": marketRoot,
        "totalNumberStorageRoots": totalNumber
        }
    
    features = pd.DataFrame(data, index = [0])
    return features


df = userInput()

def prediction():
    predict = model.predict(df)
    return predict


if st.button("Predict"):
      result = prediction()
      st.success(f"Thank you for filling this form. The marketable yield is {result} T/ha (Tonnes/hectres")
      st.info("Note: This prediction might not be 100% accurate as it is an AI prediction")