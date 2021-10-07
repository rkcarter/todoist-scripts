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

for note in api.state['notes']:
	if '!!' in note['content']:
		print("ORIGINAL NOTE: " + note['content'])
		new_note = note['content'].replace('!!','**')
		print("NEW NOTE: " + new_note)
		print()
		api.notes.update(note['id'], content=new_note)
		update_counter += 1
		if update_counter >= sync_every:
			print("*** COMMITTING ***")
			api.commit()
			update_counter = 0
print("*** FINAL COMMIT ***")
api.commit()	# final commit
