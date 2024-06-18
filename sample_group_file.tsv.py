import pandas as pd

# Path to the 500x500 subset file
subset_file_path = '/home/abera/data1/data1/500x500_dist_max_PCSK1.tsv'

# Read the subset TSV file
data = pd.read_csv(subset_file_path, sep='\t')

# Print the columns to inspect the DataFrame
print("DataFrame columns:", data.columns)

# Define the function to categorize based on a specific column
# Replace 'ActualColumnName' with the correct column name from the DataFrame
def categorize(value):
    if value < 10:
        return 'Low'
    elif 10 <= value < 20:
        return 'Medium'
    else:
        return 'High'

# Replace 'ActualColumnName' with the correct column name
# Example: if the correct column name is 'Measurement', use 'Measurement'
column_name = 'ActualColumnName'  # Change this to the correct column name

# Check if the column exists before applying the categorization function
if column_name in data.columns:
    data['Category'] = data[column_name].apply(categorize)
    # Select only the relevant columns for the sample group file
    # Assume the sample IDs are in a column named 'ID' and categories in 'Category'
    sample_group_data = data[['ID', 'Category']]
    # Display the sample group data
    print(sample_group_data.head())
    # Path to the output sample group definition file
    output_file_path = '/home/abera/data1/data1/sample_group_file.tsv'
    # Save the sample group definitions to a new TSV file
    sample_group_data.to_csv(output_file_path, sep='\t', index=False)
else:
    print(f"Column '{column_name}' not found in DataFrame")
