import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def transform_data(df):
    df=df.copy()
    #Categorize players into age groups (e.g., "young", "adult", "senior")
    df['AgeGroup']=df['Age'].apply(lambda x: 'young' if x<18 else 'adult' if 18<=x<40 else 'senior')
    #create playtime in hours per session to see more clearly who is casual, Binger or Light gamer
    df['PlayTimePerSession']=df.apply(lambda df: df['PlayTimeHours']/(df['SessionsPerWeek']+1),axis='columns')
    df['IsMale'] = df['Gender'].map({'male': 1, 'female': 0})
    #transform numerical to new categorical session group column for simplify analyze
    df['SessionGroup'] = pd.cut(
    df['SessionsPerWeek'],         # column to cut
    bins=[0, 5, 10, 20],           # numeric boundaries
    labels=['low', 'medium', 'high']  # category names
        )
  

    return df
