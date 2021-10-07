#!/usr/bin/env python3

import todoist
sync_every = 50 # sync every 50 updates

# Get my personal API (copied into a file from Todoist | Integrations |
# API token. Strip off end-of-line character)
with open('todoist_api.txt', 'r') as f:
        todoist_api = f.readline().rstrip()
#print('DEBUG: My Todoist API = |' + todoist_api + '|')

# Login with the api
api = todoist.TodoistAPI(todoist_api)
# Full sync before starting
api.sync()

update_counter = 0      # do a sync every 50 updates

# API calls tasks "items"
for item in api.state['items']:
	if '!!' in item['description']:
		print("ORIGINAL TASK DESCRIPTION: " + item['description'])
		new_item_description = item['description'].replace('!!','**')
		print("NEW TASK DESCRIPTION: " + new_item_description)
		print()
		api.items.update(item['id'], description=new_item_description)
		update_counter += 1
		if update_counter >= sync_every:
			print("*** COMMITTING ***")
			api.commit()
			update_counter = 0
print("*** FINAL COMMIT ***")
api.commit()	# final commit
