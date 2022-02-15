import pandas as pd
import hashlib
import os
import sqlite3

pathes = []

#getting all the files pathes
for path, currentDirectory, files in os.walk("/home"):
    for file in files:
        pathes.append((os.path.join(path, file)))

#checking signatures with the database
#dataset = pd.read_csv('database.csv')
conn=sqlite3.connect("signatures.db")
c=conn.cursor()
c.execute('''SELECT * FROM sign''')
df=pd.DataFrame
rows=c.fetchall()
for path in pathes:

	try:
		filename = path
		with open(filename, "rb") as f:
			bytes = f.read()
			readable = hashlib.md5(bytes).hexdigest()
		
		for row in rows:
			if row[0] ==readable:
				print (path + "   has virus do you want to delete it? [Y/n]")
				while (1):
					delete = input()
					if delete == "n":
						break
					elif delete == "Y":
						os.remove(path)
						print ("Malicious file is deleted successfully")
						break
					else:
						print ("Your answer must be [Y/n]. Please try again")	
	except Exception:
		pass 
