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

# Todoist API calls tasks "items"
for item in api.state['items']:
	if '!!' in item['content']:
		print("ORIGINAL TASK NAME: " + item['content'])
		new_item_name = item['content'].replace('!!','**')
		print("NEW TASK NAME: " + new_item_name)
		print()
		
