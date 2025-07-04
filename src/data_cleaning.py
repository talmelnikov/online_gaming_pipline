import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_data(df):
    # Make a copy to avoid modifying the original
    df = df.copy()
    placeholder_values=['unknown','n/a','?','null','none','None','',' ']
    #drop duplicates
    df.drop_duplicates(inplace=True)
    cols_to_clean=['Gender','Location','GameGenre','GameDifficulty','EngagementLevel']
    #changed all object to lower strings for making easy to check if there is placeorders values
    df[cols_to_clean]= df[cols_to_clean].apply(lambda col:col.str.strip().str.lower())
    #convert all the missing values to Null
    df.replace(placeholder_values,np.nan,inplace=True)
    #convert object to category to cach less space in memory and have a faster run
    df[cols_to_clean]=df[cols_to_clean].astype('category')
    print(df.info())
    return df


