import json
from pandas import to_datetime
import os
import fnmatch
import os
import numpy

#Initilize globals
count = 0
val = 0
dictWords = { }

#############################################
output_file_name = os.path.join(os.getcwd(),"wc_output","wc_result.txt")
print "Processing dir:", os.path.join(os.getcwd(),"wc_input","....")

###### Check btach environment ##########
#####################################
try:
    for item in os.listdir(os.path.join(os.getcwd(),"wc_input")):
        print item
except Exception, error:
       print error
       sys.exit(1)

try:
       output_file_object = open(output_file_name, 'w')
       print item
except Exception, error:
       print error
       sys.exit(1)
######## Environment OK ########################
# Process ALL 
#
################################################
for item in os.listdir(os.path.join(os.getcwd(),"wc_input")):
    print item

lstFileNames = []

for ltemFile in os.listdir(os.path.join(os.getcwd(),"wc_input")):
    if os.path.isfile(os.path.join(os.getcwd(),"wc_input",ltemFile)):
#       print "is a file path", ltemFile
        lstFileNames.append(ltemFile)
    else:
        print "not a file", ltemFile
    
print "Input file count:", len(lstFileNames) 

#    for line in open('D:/Python-2-7-6/NEWS.txt'):
for inputCurr in lstFileNames:
    file_object = open(os.path.join(os.getcwd(), "wc_input", inputCurr), 'rU')
    try:
        for line in file_object:
            try:
                line.decode('ascii')
            except Exception, error:
                continue ## skip blanks
            for word in line.split():
            #print word
                count = count + 1
                if word in dictWords: 
#                   print 'found', d1[word]
                    val = dictWords[word]
                    dictWords[word] = val + 1
                else:
#                   print 'not found'
                    dictWords[word] = 1
    finally:
        file_object.close()
    
print "Total words:", count
keys = dictWords.keys()
keys.sort()

output_file_object = open(output_file_name, 'w')
try:
    for skey in keys:
	    print skey, "\t", dictWords[skey]

	    output_file_object.write(str(skey)+"\t"+str(dictWords[skey])+"\n")
finally:
    output_file_object.close()


