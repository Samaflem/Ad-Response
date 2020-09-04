# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:01:11 2020

@author: Sam
"""


#%% libraries

import streamlit as st
import datetime
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
#%% Lists


age_options = ['18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', 
               '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', 
               '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 
               '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', 
               '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', 
               '73', '74', '75', '76', '77', '78', '80', '81', '82', '83', '84']

job_dict = {1 : 'Administration', 2 : 'Blue-collor', 3 : 'Entrepreneur', 4 : 'Househelp',
               5 : 'Management', 6 : 'Retired', 7 : 'Self-employed', 8 : 'Services',
               9 : 'Student', 10 : 'Technician', 11 : 'Unemployed', 12 : 'Others'}

marital_options = ["Married", "Single", "Divorced", "Widowed"]
marital_values = [1, 2, 3, 4]
marital_dict = dict(zip( marital_values, marital_options))


education_options = ['Primary', 'Secondary', 'Tertiary', 'None']
education_values = [1, 2, 3, 4]
education_dict = dict(zip(education_values, education_options))

default_dict = {1: "Yes", 0: "No" }

housing_dict = {1: "Yes", 0: "No"}

loan_dict = {1: "Yes", 0: "No"}

contact_dict = {1: "Telephone", 2: "Email", 3: "Personal Contact", 4 : "None"}

campaign_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

poutcome_dict = {0: "Did not Subscribe", 1: "Subscribed"}


#%% Outline



#title
st.title("Customer Response")


#header/subheader
st.header('Customer Biographical Information')

age = st.selectbox("Customer's age", age_options)

#TODO... Get a better name for the data point
job_var = st.selectbox("Customer's Current Employment",
                       options = list(job_dict.keys()), 
                       format_func = lambda x: job_dict[x])

marital_var = st.selectbox("Customer's Marital Status", 
                           options = list(marital_dict.keys()),
                           format_func = lambda x: marital_dict[x])

education_var = st.selectbox("Customer's Highest Level of Education", 
                             options = list(education_dict.keys()),
                             format_func = lambda x: education_dict[x])

st.header("Customer Relationship Information")


balance_var = st.text_input("Customer's Balance", int("0"))

if balance_var.isdigit() != True:
    st.warning("Enter an Integer value")
else: 
    balance = balance_var
   

housing_var = st.selectbox("Does Customer Own a House", 
                           options = list(housing_dict.keys()), 
                           format_func = lambda x: housing_dict[x])

loan_var = st.selectbox("Does Customer Have an Active Loan", 
                        options = list(loan_dict.keys()), 
                        format_func = lambda x: loan_dict[x])

default_var = st.selectbox("Has Customer Defaulted on Previous Loan", 
                           options = list(default_dict.keys()), 
                           format_func = lambda x: default_dict[x])

contact_var = st.selectbox("How is the Customer Usually Contacted?", 
                           options = list(contact_dict.keys()), 
                           format_func = lambda x: contact_dict[x])

today = datetime.date.today()
date_contact = st.date_input("Date of Contact", today)

#TODO Extract the day name from the data

duration_var = st.text_input("Estimated Duration of the Contact", int("0000"))

if duration_var.isdigit() != True:
    st.warning("Enter an Integer value")
else:
    duration = int(duration_var)
    
previous_var = st.text_input("Number of Contacts before this Campaign", int("0"))
if previous_var.isdigit() != True:
    st.warning("Enter an Integer value")
else:
    previous = int(previous_var)

poutcome_var = st.selectbox("Outcome of Previous Campaign", 
                            options = list(poutcome_dict.keys()), 
                            format_func = lambda x: poutcome_dict[x])

pdays_var = st.text_input("Number of Days Passed after last Contact", 
                         int("0"))
st.subheader("Notice!!!")
st.info(" -1 represent NO CONTACT, Do not use 0 for NO CONTACT")
if pdays_var.isdigit() != True:
    st.warning("Enter an Integer value")
else:
    pdays = int(pdays_var)

campaign = st.selectbox("Number of Contacts During Current Campaign",
                            campaign_list)
    
del[age_options, job_dict, default_dict, contact_dict, campaign_list,
    poutcome_dict, housing_dict, education_options, education_values,
    education_dict, marital_dict, marital_options, marital_values, loan_dict]
#%% Data Processing

# job values label conversion
if job_var == 1:
    job = "admin." 
elif job_var == 2:
    job = "blue-collar"
elif job_var == 3:
    job = "entrepreneur"
elif job_var == 4: 
    job = "housemaid"
elif job_var == 5:
    job = "management"
elif job_var == 6:
    job = "retired"
elif job_var == 7:
    job = "self-employed"
elif job_var == 8:
    job = "services"
elif job_var == 9:
    job = "student"
elif job_var == 10:
    job = "technician"
elif job_var == 11:
    job = "unemployed"
elif job_var == 12:
    job = "unknown"
    
# marital value label conversion    
if marital_var == 1: 
    marital = "married"
elif marital_var == 2:
    marital = "single"
elif marital_var == 3:
    marital = "divorced"
elif marital_var == 4: 
    marital = "divorced" 

# education value label conversion
if education_var == 1:
    education = "primary"
elif education_var == 2:
    education = "secondary"
elif education_var == 3:
    education = "tertiary"
elif education_var == 4:
    education = "unknown"

# default value label conversion
if default_var == 0:
    default = "no"
elif default_var == 1:
    default = "yes"

# housing value label conversion
if housing_var == 0:
    housing = "no"
elif housing_var == 1:
    housing = "yes"
    
# loan value label conversion    
if loan_var == 0:
    loan = "no"
elif loan_var == 1:
    loan = "yes"

# contact value label conversion
if contact_var == 1:
    contact = "cellular"
elif contact_var == 2:
    contact = "unknown"
elif contact_var == 3:
    contact = "unknown"
elif contact_var == 4:
    contact = "unknown"
    

if poutcome_var == 0:
    poutcome = "failure"
elif poutcome_var == 1:
    poutcome = "success"

@st.cache(suppress_st_warning = True)
def load_data():
    raw_df = pd.read_excel("Raw_data.xlsx")
    return raw_df

raw_df = load_data()

target = raw_df.term_deposit
raw_df = raw_df.drop(["term_deposit"], axis = 1, inplace = False)

new_df = [[age, job, marital, education, default, balance, housing, loan, 
           contact, date_contact, duration, campaign, pdays, previous, 
           poutcome]]

column_name = ["age", "job", "marital", "education", "default", "balance", 
               "housing", "loan","contact",  "date", "duration","campaign", 
               "pdays", "previous", "poutcome"]

new_df = pd.DataFrame(new_df, columns = column_name)


features = pd.concat([new_df, raw_df],axis=0)

del[pdays_var, previous_var, duration_var, contact_var, default_var, housing_var, 
    balance_var, education_var, marital_var, job_var, poutcome_var, loan_var, 
    column_name,age, job, marital, education, default, balance, housing, loan, 
    contact, date_contact, duration, campaign, pdays, previous, poutcome]
#%%
features["pdays_cat"] = pd.cut(features.pdays, [-1, 0, 60, 120, 180, 240, 300, 360, 420, 
                                      480, 520, 600, 660, 720, 780, 840, 900, 
                                      960, 1020, 1080], labels=["no contact",
                                    "two months", "four months", "six months", 
                                    "eight months", "ten months", "one year",
                                    "one year and two months","one year and four months", 
                                    "one year and six months", "one year and eigth months", 
                                    "one year and ten months", "two years", "two years and two months", 
                                    "two years and four months", "two years and six months", 
                                    "two years and eight months", "two years and ten months", 
                                    "three years or later"], include_lowest=True) 
                                                    
features["previous_cat"] = pd.cut(features.previous, [-1 , 0, 3, 9, 100], labels = ["no contact",
                                    "less often", "often", "more often"],
                      include_lowest=True)

features["duration_cat"] = pd.cut(features.duration, [-1, 0,600, 1200, 1800, 2400, 3000, 3600, 4200, 
                                    4800, 5400, 6000, 6600, 7200, 7800],
                      labels = ["no contact", "ten minutes", "twenty minutes", 
                                "thirty minutes", "forty minutes", "fifty minutes", 
                                "one hour", "one hour and ten minutes", "one hour and twenty minutes",
                                "one hour and thirty minutes", "one hour and forty minutes", 
                                "one hour and fifty minutes", "two hours", "over two hours"], 
                      include_lowest=True)


features["day_names"] = features["date"].apply(lambda x: x.strftime("%A"))

features["month"] = features["date"].apply(lambda x: x.strftime("%B"))

dropvar = features[["date", "duration", "pdays", "previous"]]

for col in dropvar:
    features = features.drop(col, axis = 1, inplace = False)
    
del[dropvar, today]
#%% Data processing

   
    

cat = features[['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 
          'month', 'day_names', 'duration_cat', 'pdays_cat', 'previous_cat',
          'poutcome']]
    
for col in cat:
    dummy = pd.get_dummies(features[col], prefix=col)
    features = pd.concat([features,dummy], axis=1)
    
for col in cat: 
    features = features.drop(col, axis = 1, inplace = False)
    
del[col, cat, dummy]
#%%Scoring
@st.cache(suppress_st_warning = True)
def load_model():
    load_clf = pickle.load(open('bank.pkl', 'rb'))
    return load_clf

load_clf = load_model()

new_data = features[:1]
#Apply model to make predictions
if st.button("Process"):
    prediction = load_clf.decision_function(new_data) > - 2.45
    prediction_proba = load_clf.predict_proba(new_data)
    st.subheader('Prediction')
    if int(prediction) == 0:
        st.write("Customer will not Subscribe")
    elif int(prediction) == 1:
        st.write("Customer will Subscribe")
    #st.subheader('Prediction Probability')
    #st.write(prediction_proba)
    
del[features]
#%%