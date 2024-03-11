import pandas as pd


df1 = pd.read_csv('data/BACS 2024 Roster - BACS Roster.csv')  # Replace 'path_to_first_csv.csv' with the actual path
df2 = pd.read_csv('data/SURVEY-About Us (Responses) - Form Responses 1.csv')  # Replace 'path_to_second_csv.csv' with the actual path

# Rename the student_id column in df2 is needed
df2.rename(columns={'Please provide your NTHU student ID': 'STUDENT ID'}, inplace=True)

join_columns = ['Email Address'] # Define the column from df2 need to be merge

merged_df = pd.merge(df1, df2[['STUDENT ID']+join_columns], on='STUDENT ID', how='left')

missing_ids = df2[~df2['STUDENT ID'].isin(df1['STUDENT ID'])]['STUDENT ID']
if not missing_ids.empty:
    print("Missing SCHOOL IDs in the first file:", missing_ids.to_list())
else:
    print("No missing SCHOOL IDs.")

merged_df.to_csv('output/merged_output.csv', index=False)

print("Merging complete. Output saved to 'merged_output.csv'.")


