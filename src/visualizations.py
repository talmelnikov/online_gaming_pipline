import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_target_distribution(df):
    sns.countplot(x='EngagementLevel',data=df)
    plt.title("Distribution of EngagementLevel")
    plt.xlabel("Engagement Level")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"output/target_distribution.png")
    plt.show()



def plot_numerical_vs_target(df,numeric_cols):
    for col in numeric_cols:
        grouped=df.groupby('EngagementLevel')[col].mean().reset_index()
        plt.figure(figsize=(6, 4))
        sns.barplot(x="EngagementLevel", y=col, data=grouped)
        plt.title(f"{col} by Engagement Level")
        plt.xlabel("Engagement Level")
        plt.ylabel(col)
        plt.tight_layout()
        plt.savefig(f"output/bar_{col}_vs_engagement.png")
        plt.show()

def plot_categorical_vs_target(df,categorial_column):
    for col in categorial_column:
        sns.countplot(x=col,hue='EngagementLevel',data=df)
        plt.title(f"{col} by Engagment Level")
        plt.xlabel(col)
        plt.ylabel("Engagement LevelCount")
        plt.tight_layout()
        plt.savefig(f"output/count_{col}_vs_engagement.png")
        plt.show()        
def plot_sessionPerHour(df):
        plt.figure(figsize=(6, 4))
        sns.barplot(x="EngagementLevel", y="PlayTimePerSession", data=df)
        plt.title(f"PlayTimePerSession by Engagement Level")
        plt.xlabel("Engagement Level")
        plt.ylabel("PlayTimePerSession")
        plt.tight_layout()
        plt.savefig(f"output/bar_PlayTimePerSession_vs_engagement.png")
        plt.show()
def plot_is_male_by_engagement(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x='IsMale', hue='EngagementLevel', data=df)
    plt.title("IsMale by Engagement Level")
    plt.xlabel("Is Male (1=Male, 0=Female)")
    plt.ylabel("Count")
    plt.legend(title="Engagement Level")
    plt.tight_layout()
    plt.savefig("output/is_male_vs_engagement.png")
    plt.show()