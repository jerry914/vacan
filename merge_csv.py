import pandas as pd

# Load data from CSV files
df1 = pd.read_csv('data/BACS 2024 Roster - BACS Roster.csv')
df2 = pd.read_csv('data/QUIZ - Required Readings 2 (Responses) - Form Responses 1.csv')

df2.rename(columns={'School ID (that you registered with)': 'STUDENT ID'}, inplace=True) # Modify the columns name if needed

df2['STUDENT ID'] = df2['STUDENT ID'].astype(int)

df2_unique = df2.drop_duplicates(subset=['STUDENT ID'], keep='first')

join_columns = ['Score'] # MAdd the columns name you want to merge

merged_df = pd.merge(df1, df2_unique[['STUDENT ID'] + join_columns], on='STUDENT ID', how='left')

missing_ids = df2[~df2['STUDENT ID'].isin(df1['STUDENT ID'])]['STUDENT ID']
if not missing_ids.empty:
    print("Missing SCHOOL IDs in the first file:", missing_ids.to_list())
else:
    print("No missing SCHOOL IDs.")

merged_df.to_csv('output/merged_output.csv', index=False)

print("Merging complete. Output saved to 'merged_output.csv'.")
