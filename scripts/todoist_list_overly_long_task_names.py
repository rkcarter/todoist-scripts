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

for task in api.state['items']:
	if len(task['content']) > 500:
		length=len(task['content'])
		print('*** TASK TOO LONG ***: ' + task['content'] + " LENGTH: " + str(length))
