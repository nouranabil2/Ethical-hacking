# Ethical-hacking
We started by creating a “malicious” file. The file keeps on working forever in a while loop incrementing values. 
The executable file runs infinitely, thus increasing CPU utilization. Then, the file was hashed using MD% hash function and the “Signature” of the malicious file is added to the database file .
The first program starts by checking the files running on the computer, hashing the program and comparing it with the signature in the database. 
If it’s a match, the program kills the executable file terminating it and deletes the file from the computer.
The second program scans all the files on the computer by checking the home folder and all of its subdirectories and adds it to a list.Then it loops through the list and hash all the files in the list and compare it with the database.
If it’s a match, the program indicates that there’s a virus and states it’s path and deletes the file.
