import pandas as pd
from src.data_cleaning import clean_data
from src.transformation import transform_data
from src.visualizations import plot_target_distribution, plot_numerical_vs_target, plot_categorical_vs_target, plot_sessionPerHour, plot_is_male_by_engagement



def main():
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', 100000)    
    df=pd.read_csv(r'C:\Users\assaf\Data_Engineering_course\online_gaming_project\data\online_gaming_behavior_dataset.csv')
    plt_target=plot_target_distribution(df)
    plt_numerical=plot_numerical_vs_target(df,['Age', 'PlayTimeHours', 'SessionsPerWeek'])
    plt_categorial=plot_categorical_vs_target(df,['Gender', 'GameGenre', 'GameDifficulty'])
    df_clean=clean_data(df)
    df_transform=transform_data(df_clean)
    play_time_per_session_engagement=plot_sessionPerHour(df_transform)
    is_male_engagement=plot_is_male_by_engagement(df_transform)
    plt_categorial_after=plot_categorical_vs_target(df_transform,['AgeGroup', 'SessionGroup'])
    df_transform.to_json("output/cleaned_data.json", orient="records", lines=True)



if __name__=="__main__":
    main()