# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform a quick EDA
def run_eda(csv_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Display the shape of the dataset
    print("\nDataset shape (rows, columns):")
    print(df.shape)
    
    # Display data types of each column
    print("\nColumn data types:")
    print(df.dtypes)
    
    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # Generate descriptive statistics
    print("\nDescriptive statistics:")
    print(df.describe())
    
# Correlation matrix for numerical features only
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if numeric_df.empty:
        print("\nNo numerical data available for correlation matrix.")
    else:
        plt.figure(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()
    
    # Plot distribution of numerical columns
    if not numeric_df.empty:
        numeric_df.hist(bins=15, figsize=(15, 10), color='skyblue', edgecolor='black')
        plt.suptitle('Distribution of Numerical Features')
        plt.show()
    else:
        print("\nNo numerical data available for histograms.")

# Call the function with your CSV file path
run_eda('data/imdb-movies-dataset.csv')