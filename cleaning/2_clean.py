## Following the EDA, we will clean the dataset to generate a new one.

import pandas as pd
import numpy as np

def clean_dataset(csv_file_path):

    # Load the dataset
    df = pd.read_csv(csv_file_path)

    # Small number of missing values
    df['Genre'] = df['Genre'].fillna('Unknown')
    df['Director'] = df['Director'].fillna('Unknown')
    df['Cast'] = df['Cast'].fillna('Unknown')

    # Significant number of missing values
    df['Certificate'] = df['Certificate'].fillna('Not Rated')
    df['Duration (min)'] = df['Duration (min)'].fillna(df['Duration (min)'].median())
    df['Rating'] = df['Rating'].fillna(df['Rating'].median())

    # Remove movies with no year. Huge hypothesis for our analysis that I can justify.
    df = df.dropna(subset=['Year'])

    # Remove movies with no vote. Huge hypothesis for our analysis that I can justify.
    df = df.dropna(subset=['Votes'])

    return df

# Define the function to clean the dataset and save it
def create_analysis_dataset(input_csv, output_csv):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)
    
    # List of columns to remove
    columns_to_remove = ['Metascore', 'Review Count', 'Review Title', 'Review']
    
    # Remove the columns
    df_cleaned = df.drop(columns=columns_to_remove, errors='ignore')
    
    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)
    
    return df_cleaned

# Call the function with your input and output CSV file paths
df_cleaned = create_analysis_dataset('data/imdb-movies-dataset.csv', 'data/imdb-movies-cleaned.csv')