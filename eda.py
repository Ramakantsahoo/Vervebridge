# eda.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def explore_dataset(df):
    try:
        logger.info("Exploring dataset")
        print("Dataset Information:")
        print(df.info())

        print("\nFirst Few Rows of the Dataset:")
        print(df.head())

        print("Summary Statistics:")
        print(df.describe())

        print("\nNumber of Unique Values:")
        print(df.nunique())

        missing_values = df.isnull().sum()
        print("\nMissing Values:")
        print(missing_values)
    except Exception as e:
        logger.error("Error while exploring dataset: %s", e)

def plot_distributions(df):
    try:
        logger.info("Plotting distributions")
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(8, 6))
        sns.countplot(x='Height', data=df)
        plt.title('Height Distribution')
        plt.xlabel('Height')
        plt.ylabel('Count')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.countplot(y='Genre', data=df, order=df['Genre'].value_counts().index)
        plt.title('Genres Distribution')
        plt.xlabel('Count')
        plt.ylabel('Genre')
        plt.show()

        plt.figure(figsize=(12, 8))
        sns.countplot(y='Author', data=df, order=df['Author'].value_counts().iloc[:10].index)
        plt.title('Top 10 Authors by Book Count')
        plt.xlabel('Count')
        plt.ylabel('Author')
        plt.show()

        plt.figure(figsize=(12, 8))
        sns.countplot(y='Publisher', data=df, order=df['Publisher'].value_counts().iloc[:10].index)
        plt.title('Top 10 Publishers by Book Count')
        plt.xlabel('Count')
        plt.ylabel('Publisher')
        plt.show()

        numeric_cols = ['Height']
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[numeric_cols])
        plt.title('Boxplot of Height')
        plt.show()
    except Exception as e:
        logger.error("Error while plotting distributions: %s", e)

def print_unique_genres(df):
    try:
        logger.info("Printing unique genres")
        unique_genres = df['Genre'].unique()
        print("Unique Genres:")
        for genre in unique_genres:
            print(genre)
    except Exception as e:
        logger.error("Error while printing unique genres: %s", e)
