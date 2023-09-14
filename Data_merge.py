#!/usr/bin/env python
# coding: utf-8

#importing libraries
import pandas as pd
pd.options.display.max_columns = None
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import warnings
import plotly.graph_objects as go
warnings.filterwarnings('ignore') 

#importing datasets
df1= pd.read_csv('patient_df.csv')
df2= pd.read_csv('allergy_df.csv')
df3= pd.read_csv('condition_df.csv')
df4= pd.read_csv('coverage_df.csv')
df5= pd.read_csv('encounter_df.csv')
df6= pd.read_csv('medicalclaim_df.csv')
df7= pd.read_csv('medication_df.csv')
df8= pd.read_csv('vitalsign_df.csv')

#performing concat
merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)

#seeing merged_df
merged_df.info()
merged_df.head()

# exporting
merged_df.to_csv('merged_df.csv')

#reading the merged file 
df = pd.read_csv("/Users/pallavijain/Desktop/data_6212/merged_df.csv")

#preprocessing the merged file - dropping nulls and redundant columns
df = df.dropna() 
df = df.drop(columns='Unnamed: 0')
df = df.drop(columns='Unnamed: 0.1')
df = df.drop(columns='Unnamed: 0.2')
df = df.drop(columns='Unnamed: 0.3')
df = df.drop(columns='Unnamed: 0.4')
df = df.drop(columns='Unnamed: 0.5')
df = df.drop(columns='Unnamed: 0.6')
df = df.drop(columns='Unnamed: 0.7')
df = df.drop(columns='Unnamed: 0.8')
df = df.drop(columns='patient_id.1')
df = df.drop(columns='patient_id.2')
df = df.drop(columns='patient_id.3')
df = df.drop(columns='patient_id.4')
df = df.drop(columns='patient_id.5')
df = df.drop(columns='patient_id.6')
df = df.drop(columns='patient_id.7')
df = df.drop(columns='encounter_id.1')
df = df.drop(columns='encounter_id.2')
df = df.drop(columns='encounter_id.3')
df = df.drop(columns='encounter_id.4')
df = df.drop(columns='encounter_id.5')
df = df.drop(columns='diagnosis_rank')
df = df.drop(columns='gender_male')

#exporting cleaned merged dataset to csv for modeling
df.to_csv("/Users/pallavijain/Desktop/data_6212/cleaned_merged_df.csv")
