import pandas as pd

# * Read the transformation specification CSV
transformation_df = pd.read_csv('Prep Parameters.csv')

# * Read the raw data CSV from APIFY
# ? Original GPT script
# raw_data_df = pd.read_csv('apify_raw_data.csv')

# ! This is just for testing purposes and will have to be reworked for easier UX
raw_data_df = pd.read_csv('input/GMS Raw - F&B, Columbus, Ohio.csv', low_memory=False) # !

# * Filter the columns
columns_to_keep = transformation_df['COLUMN RAW'].dropna().tolist()
filtered_df = raw_data_df[columns_to_keep]

# * Rename the columns
rename_mapping = transformation_df.set_index('COLUMN RAW')['COLUMN FIXED'].dropna().to_dict()
filtered_df = filtered_df.rename(columns=rename_mapping)

# * Add 'Categories' column
categories_columns = [f'categories/{i}' for i in range(10)]
filtered_df['Categories'] = filtered_df[categories_columns].apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)

# * Add 'Compiled' column for opening hours
filtered_df['Compiled'] = (
    "Monday: " + filtered_df['Monday'].fillna('Closed') + "\n" +
    "Tuesday: " + filtered_df['Tuesday'].fillna('Closed') + "\n" +
    "Wednesday: " + filtered_df['Wednesday'].fillna('Closed') + "\n" +
    "Thursday: " + filtered_df['Thursday'].fillna('Closed') + "\n" +
    "Friday: " + filtered_df['Friday'].fillna('Closed') + "\n" +
    "Saturday: " + filtered_df['Saturday'].fillna('Closed') + "\n" +
    "Sunday: " + filtered_df['Sunday'].fillna('Closed')
)

# * Define the final column order
final_columns = []
for group in transformation_df['GROUP'].unique():
    group_columns = transformation_df[transformation_df['GROUP'] == group].sort_values(by='COLUMN ORDER')['COLUMN FIXED'].tolist()
    final_columns.extend(group_columns)

# * Remove any potential NaN values from the final_columns list
final_columns = [col for col in final_columns if pd.notna(col)]

# * Check if all final_columns are in the DataFrame and filter the DataFrame by existing columns
existing_columns = [col for col in final_columns if col in filtered_df.columns]
missing_columns = [col for col in final_columns if col not in filtered_df.columns]
if missing_columns:
    print(f"Warning: The following columns were not found in the DataFrame and will be ignored: {missing_columns}")

# * Reorder columns
final_df = filtered_df[existing_columns]

# * Export the transformed data to CSV
final_df.to_csv('output/F&B, Columbus, Ohio.csv', index=False)