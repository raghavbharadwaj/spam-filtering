import sys
import os
training = sys.argv[1]
#f_op = open(training,'r')
ftraining=open(sys.argv[2],'w+')
for eachfile in sorted(os.listdir(training)):
	#if os.path.splitext(eachfile)[0] == 'SPAM':
	ftraining.write(eachfile.split('.')[0]+ ' ')
	#filecontents = eachfile.readlines().split()
	#filecontents = eachfile.read()
	eachopen = open(training +'/'+eachfile,'r',errors='ignore')
	filecontents = eachopen.read()
	words = filecontents.split()
	for word in words:
		ftraining.write(word+' ')
	ftraining.write('\n')
	eachopen.close()
ftraining.close()
#ftraining.close()
		

