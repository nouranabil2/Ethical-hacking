import psutil
import hashlib 
from hashlib import md5
import os
import signal
import pandas as pd
from subprocess import Popen, PIPE,call
import sqlite3



untrusted = []
whitelist = {}
#giving access to root user only
command = 'sudo bpftrace -e \'tracepoint:syscalls:sys_enter_openat { printf("%d, %s\\n", args->flags, str(args->filename)); }\''
#conn=sqlite3.connect("signatures.db")
#c=conn.cursor()
#The Program should run infinitely
with Popen(command, shell=True, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
	while (True):
		#getting all running processes
		for pr in psutil.process_iter(['pid','name','username']):
    
			#filtering using username
			if pr.username()!='root':
				filename= pr.cmdline()[0]
			conn=sqlite3.connect("signatures.db")
			c=conn.cursor()
			c.execute('''SELECT * FROM sign''')
			df=pd.DataFrame
			rows=c.fetchall()
			#print(rows)
			try:
        				#hashing the running processes
				with open(filename,"rb")as f:
					bytes=f.read()
					readable=hashlib.md5(bytes).hexdigest()
					for row in rows:
						#print(row)
						if readable == row[0]:
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
