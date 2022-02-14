import psutil
import hashlib 
import os
import signal
import pandas as pd

untrusted = []
whitelist = {}
while (True):

	#getting all running processes
	for pr in psutil.process_iter(['pid','name','username']):
    
		#filtering using username
		if pr.username()!='root':
			filename= pr.cmdline()[0]
        		
 
			try:
        			#hashing the running processes
				with open(filename,"rb")as f:
					bytes=f.read()
					readable=hashlib.md5(bytes).hexdigest();
   
            			#checking the database for signatures 
				#dataset=pd.read_csv('database.csv')
            
            			#for r in dataset:
				if readable =="abe4aa0cd94155349263e476666f33d2":
					if whitelist.get(filename) == None:
						pi=pr.pid 
						untrusted.append({'name': pr.name() , 'path': filename})
						os.kill(pi,signal.SIGTERM)
     
			except Exception:
				pass
	for pr in untrusted:
		print (str(pr['name']) + " has virus do you want to delete it? [Y/n]")
		while (1):
			delete = input()
			if delete == "n":
				whitelist[pr['path']] =1
				untrusted.remove(pr)
				break
			elif delete == "Y":
				os.remove(pr['path'])
				print ("Malicious file is deleted successfully")
				untrusted.remove(pr)
				break
			else:
				print ("Your answer must be [Y/n]. Please try again")

