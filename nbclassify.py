import sys
import os
import json
import math
import operator

fmodel=open(sys.argv[1],'r')
fdev = open (sys.argv[2],'r')
model_dictionary={}
model_dictionary = json.load(fmodel)
labels=model_dictionary.keys()
priors={}
priors=model_dictionary['_total_priors_']
prior_probs={}
totaldocs=0
for label in priors:
	totaldocs+=priors[label]
for label in priors:
	prior_probs[label]=math.log(priors[label]) - math.log(totaldocs)

new_dict={}
#new_dict = model_dictionary.pop('_total_priors_',None)
new_dict = model_dictionary

################################CODE FOR DENOMINATOR#########################################

words_in_label={}
if '_total_priors_'in new_dict:
	del new_dict['_total_priors_']
for label in new_dict:
	words_in_label[label]=0

for key in new_dict:
	for key1 in new_dict[key]:
		words_in_label[key]+=new_dict[key][key1]
total_vocab={}
words = []
for key in new_dict:
	words |= new_dict[key].keys()
vocab_size=len(words)
denom_label = {}
for label in priors:
	denom_label[label] = math.log(words_in_label[label] + vocab_size)

###############################CODE FOR DENOMINATOR ENDS#########################################
p_doc = {}
count=0
success_count=0
for line in fdev:
	for label in priors:
		p_doc[label]=0
		words = line.split()[1:]
		for word in words:
			if word not in new_dict[label]:
				p_doc[label]+= math.log(1) -  denom_label[label]
			else:
				p_doc[label]+=math.log(1 + new_dict[label][word]) - denom_label[label]
		p_doc[label]+=prior_probs[label]
		
	doc_class = max(p_doc,key=p_doc.get)
	print(doc_class)
		#print(doc_class)
	if line.split()[0] == doc_class:
		success_count+=1
	count+=1		



#print(words_in_label)		
#print(total_vocab)
#print(new_dict.keys())
fmodel.close()
fdev.close()
