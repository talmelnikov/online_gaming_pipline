import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def transform_data(df):
    df=df.copy()
    play_time_per_gamegener=df.groupby('GameGenre').agg({
        'PlayTimeHours':'mean'
    })
    achievement_per_difficulty=df.groupby('GameDifficulty').agg({
        'AchievementsUnlocked':'sum'
    })
    df['AgeGroup']=df['Age'].apply(lambda x: 'young' if x<35 else 'adult')
    active__age=df.groupby('AgeGroup').agg({
        'SessionsPerWeek':'sum'
    })

    print("Average Play Time per Genre:\n",play_time_per_gamegener)
    print("\nTotal Achievements per Difficulty:\n", achievement_per_difficulty)
    print("\nSessions per Age Group:\n", active__age)
    return df
