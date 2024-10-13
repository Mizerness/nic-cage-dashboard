import pandas as pd

# Function to perform EDA and store the results in a CSV file
def run_eda_to_csv(input_csv, output_csv):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)
    
    # Initialize an empty list to store the results
    results = []

    # Loop through each column in the DataFrame
    for col in df.columns:
        # Gather basic statistics for each column
        col_data = df[col]
        col_info = {
            "Column Name": col,
            "Data Type": col_data.dtype,
            "Missing Values": col_data.isnull().sum(),
            "Unique Values": col_data.nunique(),
            "Min": col_data.min() if pd.api.types.is_numeric_dtype(col_data) else None,
            "Max": col_data.max() if pd.api.types.is_numeric_dtype(col_data) else None,
            "Mean": col_data.mean() if pd.api.types.is_numeric_dtype(col_data) else None,
            "Median": col_data.median() if pd.api.types.is_numeric_dtype(col_data) else None,
            "Standard Deviation": col_data.std() if pd.api.types.is_numeric_dtype(col_data) else None,
            "Top Category": col_data.mode().iloc[0] if not pd.api.types.is_numeric_dtype(col_data) else None,
            "Frequency of Top Category": col_data.value_counts().iloc[0] if not pd.api.types.is_numeric_dtype(col_data) else None
        }

        # Append the column information to the results list
        results.append(col_info)
    
    # Convert the results into a DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_csv, index=False)

    print(f"EDA results saved to {output_csv}")

# Call the function with input and output file paths
run_eda_to_csv('data/imdb-movies-cleaned.csv', 'data/eda_results.csv')
