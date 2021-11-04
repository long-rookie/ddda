import base64
import sys
if len(sys.argv)<2:
	print "Usage:b64.py target.txt"
	exit()
filename=sys.argv[1]
fp=open(filename)
fp1=open(filename+".base64.txt","a+")
if not fp or not fp1:
	print "Error!"
	exit()
while True:
	content=fp.readline()
	if not content:
		break
	if not content.replace("\n",""):
		continue
	content=base64.b64encode(content)+"\n"
	fp1.write(content)
fp.close()
fp1.close()