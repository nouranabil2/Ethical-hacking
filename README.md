# Ethical-hacking
We started by creating a “malicious” file. The file keeps on working forever in a while loop incrementing values. 
The executable file runs infinitely, thus increasing CPU utilization. Then, the file was hashed using SHA256 hash function and the “Signature” of the malicious file is added to the database.
The first program starts by checking the files running on the computer, hashing the binary format “in the RAM” and comparing it with the signature in the database. 
If it’s a match, the program kills the executable file terminating it.
The second program checks a folder and all of its subdirectories and adds it to a list.Then it loops through the list and hash all the files in the list and compare it with the database.
If it’s a match, the program indicates that there’s a virus and states it’s path.
