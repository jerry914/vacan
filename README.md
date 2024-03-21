# Vacan - Roster Hacker

This suite of Python scripts is designed to automate the integration and processing of data from Google Surveys and Canvas into a course roster. It simplifies the management of course-related data, such as student information, assignment submissions, and peer reviews.

## Overview of Scripts

1. **merge_csv.py**: Merges data from Google Surveys into the course roster.
2. **add_accountId.py**: Integrates Canvas account IDs into the roster.
3. **get_assignment.py**: Downloads details of student assignment submissions, including comments received and peer reviews, organized by the roster.

## Canvas API Usage

The scripts interact with the Canvas Learning Management System (LMS) through its API, which allows programmatic access to course information, student data, assignments, and more.

### Authentication

Canvas API authentication is achieved via OAuth2. The recommended method is to use the HTTP Authorization header, but sending the access token as a query string or POST parameter is also supported.

#### Obtaining an Access Token

1. Log in to Canvas and navigate to **Account > Settings > Approved Integrations**.
2. Click on **"+ New Access Token"**.
3. Follow the instructions to generate a new token.

Keep your access token secure and do not share it publicly.

### Example API Call

Using `curl` to make an API call with your OAuth2 token:

```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" "https://canvas.instructure.com/api/v1/courses"
```
Replace <YOUR_ACCESS_TOKEN> with your actual token.

### Script Instructions
Ensure Python 3 is installed on your system and you have your Canvas API access token in `.env` before proceeding.


1. Adding Canvas Account IDs

Before running this script, download students.json from Canvas:
```
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" "https://canvas.instructure.com/api/v1/courses/:course_id/students" > students.json
```
- Replace :course_id with your course's actual ID and <YOUR_ACCESS_TOKEN> with your token.

```
python3 add_accountId.py
```


2. Downloading Assignments and Reviews
- set `AUTH_TOKEN` in .env file before run the code:
```
python3 get_assignment.py
```
