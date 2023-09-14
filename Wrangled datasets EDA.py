#!/usr/bin/env python
# coding: utf-8

#import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import warnings
import plotly.graph_objects as go
warnings.filterwarnings('ignore') 


# # Wrangled datasets

# Medication

#Read data
df= pd.read_csv('medication_df.csv')


top_20_medications = df['medication_name'].value_counts().nlargest(20)


top_20_medications = df['medication_name'].value_counts().nlargest(20).index
plt.figure(figsize=(15, 6))
sns.countplot(data=df, x='medication_name', order=top_20_medications)
plt.xticks(rotation=90)
plt.title('Top 20 Medications Prescribed')
plt.show()



'''Top 20 medications prescribed sorted by it's count.
They are: 

DEMEROL INJ                                           
Albuterol-Ipratrop 3 mg / 0.5 (3 ml) UD               
METOPROLOL SUCCINATE XL 50 MG TAB                     
DOCUSATE SOD 100 MG CAP                               
MethylPREDNISolone 40 mg Vial                         
MULTIPLE VITAMIN  TAB                                 
Pantoprazole 40 mg EC Tab                             
Multivitamin Therapeutic Tab                          
Carvedilol 6.25 MG Tab                                
Magnesium Sulfate 1 gm in D5W 1 GM/100 ML BAG         
MULTIVITAMINS THERAPEUTIC TAB                         
DOCUSATE SODIUM 50 MG/SENNA 8.6 MG TAB                
ASPIRIN EC 81 MG TABEC                                
Vitamins A & D Oint UD Foilpak                        
guaiFENesin 100 mg/5 ml Syrup UD                      
Azithromycin 500 MG in Sodium Chloride 0.9% 250 ML    
SODIUM CHLORIDE 0.9% INJ 3ML FLUSH                    
cefTRIAXone 1 gm 1 GM/100 ML BAG                      
GlipiZIDE 10 mg SR Tab                                
Azithromycin 250 mg Tab '''


# Encounter

#Read data
data = pd.read_csv('encounter_df.csv')

# Get the top 20 patients with the highest number of encounters
top_20_patient_encounter_counts = data['patient_id'].value_counts().head(20).reset_index()
top_20_patient_encounter_counts.columns = ['patient_id', 'encounter_count']

# Barplot of the number of encounters for the top 20 patients
plt.figure(figsize=(15, 6))
sns.barplot(data=top_20_patient_encounter_counts, x='patient_id', y='encounter_count')
plt.title('Top 20 Patients with the Highest Number of Encounters')
plt.xlabel('Patient ID')
plt.ylabel('Number of Encounters')
plt.xticks(rotation=90)
plt.show()



'''Top 20 Patients with highest encounters are: 
 
12052, 12686, 12589, 1066, 11662, 13208, 11591, 12772, 1228, 11540, 11363, 10156, 10805, 13289, 10725, 11842, 12955, 12519, 12047, 12083.
    '''


# Patients



#Read data
df = pd.read_csv('patient_df.csv')


# Gender splits
gender_counts = df[['gender_female', 'gender_male']].sum()


plt.figure(figsize=(10, 6))
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
plt.show()


'''The percentage distribution of males and females are 60.1% and 39.9% respectively'''


# Medical Claim 

#Read data
df = pd.read_csv('medicalclaim_df.csv')


df.info()


# correlations between variables

correlations = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0)
plt.show()



'''High correlation between paid_amount and charge_amount
Weak postive correlation between clain_type_I and charge_amount
Strong negative correlation between claim_type_I and claim_type_P'''

