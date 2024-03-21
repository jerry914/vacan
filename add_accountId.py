import csv
import json

# Modify the file name if needed
with open('data/students.json', 'r') as json_file: 
    students = json.load(json_file)

updated_rows = []
# Modify the file name if needed
with open('data/BACS 2024 Roster - BACS Roster.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    fieldnames = csv_reader.fieldnames + ['ACCOUNT ID']
    for row in csv_reader:
        for student in students:
            if row['STUDENT ID'] in student['name'] or \
               row['STUDENT ID'] in student['sortable_name'] or \
               row['STUDENT ID'] in student['sortable_name'] or \
               row['EMAIL'] in student['name']:
                row['ACCOUNT ID'] = student['id']
                break
        updated_rows.append(row)

with open('output/Updated_Roaster.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)
