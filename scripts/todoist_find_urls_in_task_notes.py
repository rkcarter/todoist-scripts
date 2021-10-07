#!/usr/bin/env python3

import todoist

# Get my personal API (copied into a file from Todoist | Integrations |
# API token. Strip off end-of-line character)
with open('todoist_api.txt', 'r') as f:
	todoist_api = f.readline().rstrip()
#print('DEBUG: My Todoist API = |' + todoist_api + '|')

# Login with the api
api = todoist.TodoistAPI(todoist_api)
# Full sync before starting
api.sync()

for note in api.state['notes']:
	if 'http:' in note['content'] or 'https:' in note['content']:
		print("***NOTE WITH URL***: ")
		print(note['content'])
		print ("")
