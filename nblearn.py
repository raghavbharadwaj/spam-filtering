import sys
import math
import json

f_model = open(sys.argv[2],'w+')

f_features = open(sys.argv[1],'r')
lines = f_features.readlines()
countspam=0
countham =0
labels = []

	
for line in lines:
	#if label not in labels:
	label= line.split()[0]
	if label not in labels: 
		labels.append(label)
wordfrequency = {}


def wordfrequencies():
	
	#wordfrequency = {}
	wordslabel={}
	labelcounts = {}
	
	for label in labels:
		wordfrequency = {}
		labelcounts[label]=0
	
		for line in lines:
			if line.split()[0]==label:
				labelcounts[label]+=1	
				words = line.split()[1:]
				for word in words:
					if word not in wordfrequency:
						wordfrequency[word]=1
					else:
						wordfrequency[word]+=1
					
		
		wordslabel[label]=wordfrequency
	wordslabel['_total_priors_']=labelcounts	
		#wordslabel[label].append(labelcounts)			
	json.dump(wordslabel,f_model)
	#print(wordslabel,file=f_model)
	
#labelcounts = len(labels)
	#print(labelcounts)
count={}
for label in labels:
	count[label]=0
	
for label in labels:
	for line in lines:
		if line.split()[0] == label:
			count[label] = count[label] + 1
	

wordfrequencies()
f_features.close()
f_model.close()
	
