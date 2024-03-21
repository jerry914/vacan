import csv
import json

# Load the JSON data
with open('data/hw2.json', 'r') as json_file:
    hw_data = json.load(json_file)

# Create a dictionary to hold the combined data for each student
student_data = {}

# Process each homework submission in the JSON file
for submission in hw_data:
    user_id = submission['user_id']
    preview_url = submission.get('preview_url', '')
    comments = '\n'.join([comment['comment'] for comment in submission.get('submission_comments', [])])

    # Check if the student already exists in the dictionary
    if user_id in student_data:
        # Append the preview URL and comments to the existing entry
        student_data[user_id]['preview_urls'].append(preview_url)
        student_data[user_id]['comments'].append(comments)
    else:
        # Create a new entry for the student
        student_data[user_id] = {'preview_urls': [preview_url], 'comments': [comments]}

print(student_data)
# Read the students' information from the CSV file
students_info = []
with open('data/roaster_accountId.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        account_id = row['ACCOUNT ID']
        # Match the ACCOUNT ID with the user_id in the homework data
        if account_id in student_data:
            # Combine preview URLs and comments
            combined_preview_urls = '\n'.join(student_data[account_id]['preview_urls'])
            combined_comments = '\n'.join(student_data[account_id]['comments'])
            row['Combined Preview URLs and Comments'] = f'{combined_preview_urls}\n{combined_comments}'
        else:
            row['Combined Preview URLs and Comments'] = 'No submissions/comments found'
        
        students_info.append(row)
