import requests
import json
import csv
import os
from dotenv import load_dotenv

# Change the ids
course_id = "8725993"
assignment_id = "44090683"
student_list_path = 'output/student_list_complete.csv'
raw_submission_path = 'output/hw3.json'
output_path = 'output/mapping.json'

base_url = f"https://canvas.instructure.com/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions"

load_dotenv()
auth_token = os.getenv('AUTH_TOKEN')

headers = {
    "Authorization": f"Bearer {auth_token}"
}
body = {
    "include": ["submission_comments"]
}
page = 1
submissions = []

while True:
    url = f"{base_url}?page={page}"
    response = requests.get(url, headers=headers, params=body)
    if response.status_code == 200:
        data = response.json()
        # If the data list is empty, break the loop
        if len(data) == 0:
            break
        submissions.extend(data)
        page += 1
    else:
        print(f"Failed to retrieve page {page}: {response.status_code}")
        break

# Writing the collected data to a JSON file
with open(raw_submission_path, 'w') as json_file:
    json.dump(submissions, json_file, indent=2)

print(f"Data has been written to {raw_submission_path}.")

# Read the student list from the CSV file
students = {}
with open(student_list_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        account_id = row['ACCOUNT ID']
        # Ensure account_id is always stored as a string
        students[str(account_id)] = row

# Load homework submissions from the JSON file
with open(raw_submission_path, 'r', encoding='utf-8') as jsonfile:
    homework_submissions = json.load(jsonfile)
output = {} 
for student in students:
    account_id = student
    output[account_id] = {
        'assignment': {
            'TA': students[account_id]['TA'],
            'STUDENT ID': students[account_id]['STUDENT ID'],
            'preview_url': '',
            'submission_comments': []
        },
        'peer_review': []
    }

for submission in homework_submissions:
    account_id = str(submission['user_id'])
    if account_id in output:
        output[account_id]['assignment']['preview_url'] = submission['preview_url'].split('?')[0]
        # Add submission comments
        for comment in submission.get('submission_comments', []):
            output[account_id]['assignment']['submission_comments'].append({
                'author_name': comment['author_name'],
                'comment': comment['comment']
            })

for submission in homework_submissions:
    reviews = submission.get('submission_comments', [])
    for review in reviews:
        account_id = str(review['author_id'])
        if account_id in output:
            output[account_id]['peer_review'].append({
                'author_name': review['author_name'],
                'comment': review['comment']
            })

with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(output, outfile, indent=4)

print("Mapping complete. Output written to " + output_path )
