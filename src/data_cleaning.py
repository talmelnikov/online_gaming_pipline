import pandas as pd
import matplotlib.pyplot as plt



df=pd.read_csv(r'C:\Users\assaf\Data_Engineering_course\online_gaming_project\data\online_gaming_behavior_dataset.csv')

print(df.head(10))
print(df.tail())
df.info()
print(df.isnull().sum())