import pandas as pd
file_path = '/home/abera/data1/data1/MF915__exam/AberaTest__abera_distmat_list__population__pvals.tsv'
pvals_df = pd.read_csv(file_path, sep='\t')
pvals_df['Feature'] = pvals_df.index
melted_pvals_with_features_df = pvals_df.melt(id_vars=['Feature'], var_name='Population', value_name='p-value')
melted_pvals_with_features_df = melted_pvals_with_features_df[melted_pvals_with_features_df['Population'].str.contains('p-value')]
sorted_pvals_with_features_df = melted_pvals_with_features_df.sort_values(by='p-value')
sorted_pvals_with_features_df['adjusted_p-value'] = pd.Series(sorted_pvals_with_features_df['p-value']).rank(method='first') / len(sorted_pvals_with_features_df) * 0.05
top_features_with_lowest_pvals = sorted_pvals_with_features_df[['Feature', 'Population', 'p-value', 'adjusted_p-value']].head(10)

# Save the top 10 features to a CSV file
output_csv_file_path = '/home/abera/data1/data1/MF915__exam/top_features_with_lowest_pvals.csv'
top_features_with_lowest_pvals.to_csv(output_csv_file_path, index=False)

print(f"Top features with the lowest adjusted p-values saved to {output_csv_file_path}")
