import pandas as pd
import hashlib
import os

pathes = []
for path, currentDirectory, files in os.walk("/home"):
    for file in files:
        #print(os.path.join(path, file))
        pathes.append((os.path.join(path, file)))


dataset = pd.read_csv('database.csv')
for path in pathes:
	try:
		filename = path
		with open(filename, "rb") as f:
			bytes = f.read()
			readable = hashlib.sha256(bytes).hexdigest()
		for r in dataset:
			if r == readable:
				print (path + "   has virus")	
	except Exception:
		pass 
