import pandas as pd
from src.data_cleaning import clean_data




def main():
    df=pd.read_csv(r'C:\Users\assaf\Data_Engineering_course\online_gaming_project\data\online_gaming_behavior_dataset.csv')
    df_clean=clean_data(df)
    



if __name__=="__main__":
    main()