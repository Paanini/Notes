#!/usr/bin/python
import sqlite3
import re
path = "/media/Software/Dropbox/Notes/"
conn = sqlite3.connect('/media/Software/Dropbox/SimplyNotes/inotes.bak')
c = conn.cursor()
notes = c.execute(
    'SELECT text, created, gtask_completed, _id FROM notes').fetchall()
text = []
date_create = []
date_done = []
#for note in notes:
#    try:
#        title=re.search(r'.+?\n',note[0]).group(0)[:-1]
#    except AttributeError:
#        title=re.search(r'\w+',note[0]).group(0)
#    f=open(path+title,"w")
#    f.write(note[0]+"\n\n Date of Creation: "+note[1]+"\n\n Date of Completion: "+note[2])
#    f.close()
#    text.append(note[0])
#    date_create.append(note[1])
#    date_create.append(note[2])
#print notes[2]
for note in notes:
    print note[0]
    print "\n"
    print "*" * 20
    print note[1]

print text
print date_create
print date_done
