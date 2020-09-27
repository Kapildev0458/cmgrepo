#!/usr/bin/python3
print('content-type: text/html \n')
import cgi
import subprocess
a = cgi.FieldStorage()
b = a.getvalue('airports')
output = subprocess.getstatusoutput(b)
if output[0]==0 :
	print("hello i am happy to see you again")
	print('and the command you want to run :')
	print(output)
else :
	print(output[1])
