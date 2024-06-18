import pandas as pd

# Provide the file path for the 500x500 subset data
subset_file_path = '/home/abera/data1/data1/500x500_dist_max_PCSK1.tsv'

# Read the subset TSV file
subset_data = pd.read_csv(subset_file_path, sep='\t')

# Define the function to categorize based on a column value (e.g., first column after the index)
# Adjust the column name or index as per your dataset
def categorize(value):
    if value < 10:
        return 'Low'
    elif 10 <= value < 20:
        return 'Medium'
    else:
        return 'High'

# Apply the categorization function to the relevant column
# Assuming we are categorizing based on the first column after the index
# Adjust 'ColumnName' to the actual column name you want to categorize by
subset_data['Category'] = subset_data.iloc[:, 1].apply(categorize)

# Display the categorized data (optional)
print(subset_data)

# Provide the file path for the output group category definition file
output_file_path = '/home/abera/data1/data1/group_category_definition_file.tsv'

# Save the categorized data to a new TSV file
subset_data.to_csv(output_file_path, sep='\t', index=False)
