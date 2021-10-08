# todoist-scripts
Scripts for examining and manipulating Todoist objects

Use these at your own risk! There's no error checking in any of them, so you can seriously break things in Todoist if something goes wrong. Also, there's at least one limitation I know of: the script converting old bold to new bold doesn't check that occurrences of "!!" are paired -- so though the intent is to change e.g. "This is !!vital!! information" to "This is **vital** information," it will also change "I'm so happy to see you!!" to "I'm so happy to see you**"

You will need the following:
https://pypi.org/project/todoist-python/

The first thing you will need to make these work is to create a file
called "todoist_api.txt" in the same directory as these scripts. It needs to contain one line, that is the text copied from going to your Todoist app, Then click your picture to get to Settings, then Integrations and where the API token is, click on "Copy to clipboard." Put that in todoist_api.txt as the only line.

When I tested these, I did things one step at a time, and used "break" in the loops to ensure I got the first one right, generally commented out the modify steps at first also.

Also, Todoist fairly recently changed their task names down from several thousand characters, to 500 characters, so I first ran todoist_find_urls_in_task_notes.py, and hand-modified them in the Todoist app. Didn't know if they would cause errors when I modified item names, so got that done first. Then started modifying away.

TO DO: 

learn enough Python regex stuff to find and match the old-style urls:

http[s]://server/and/path (URL title) (with one space between)

to:

[URL title](http[s]://server/and/path)

... while remembering that "URL title" could itself have parens inside when trying to parse it out of the old-style URL. Also check when looking for the old-style URL that I'm not finding the new-style one, i.e. it's not preceded by "](" .

