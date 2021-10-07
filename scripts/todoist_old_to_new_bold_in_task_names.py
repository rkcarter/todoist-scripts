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

# Todoist api calls tasks "items"
for item in api.state['items']:
	if '!!' in item['content']:
		print("ORIGINAL TASK NAME: " + item['content'])
		new_item_name = item['content'].replace('!!','**')
		print("NEW TASK NAME: " + new_item_name)
		print()
		api.items.update(item['id'], content=new_item_name)
		update_counter += 1
		if update_counter >= sync_every:
			print("*** COMMITTING ***")
			api.commit()
			update_counter = 0
print("*** FINAL COMMIT ***")
api.commit()	# final commit
