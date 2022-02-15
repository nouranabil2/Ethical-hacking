import psutil
import hashlib 
import os
import signal
import pandas as pd

for pr in psutil.process_iter(['pid','name','username']):
    
    if pr.username()!='root':
        filename= pr.cmdline()[0]
 
        try:
            with open(filename,"rb")as f:
                bytes=f.read()
                readable=hashlib.sha256(bytes).hexdigest();
   
            #checking the database for signatures 
            dataset=pd.read_csv('database.csv')
            
            for r in dataset:
                if r ==readable:
                    pi=pr.pid 
                    os.kill(pi,signal.SIGTERM)
     
        except Exception:
            pass
