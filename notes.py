#!/usr/bin/python
import sqlite3
import re
path = "/media/Software/Dropbox/Notes/"
conn = sqlite3.connect('/media/Software/Dropbox/SimplyNotes/inotes.bak')
c = conn.cursor()
notes = c.execute(
    'SELECT text, created, gtask_completed, _id FROM notes').fetchall()

for note in notes:
#    print note[0], type(note[0])
#    print note[1], type(note[1])
    try:
        title = re.search(r'.+?\n', note[0]).group(0)[:-1]
    except AttributeError:
        title = re.search(r'\w+', note[0]).group(0)
    f = open(path + title, "w")
    text = str(note[0]) + "\n\nDate Created: " + str(note[1]) + "\n\nDate Completed: " + str(note[2])
    f.write(text)
