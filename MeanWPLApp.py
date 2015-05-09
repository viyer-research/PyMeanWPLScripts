import json
from pandas import to_datetime
import os
import fnmatch
import sys
import numpy as np
#Initilize globals
count_words_per_line = 0.0
running_median = 0.0
val = 0
dictWords = { }
lst_running_median = list()
output_file_object=None
input_file_object=None
curr_line_no = 0

def medianWPLfn(lstWordCount):
    return np.median(lstWordCount)

output_file_name = os.path.join(os.getcwd(),"wc_output","med_result.txt")
print "Processing dir:", os.path.join(os.getcwd(),"wc_input","....")

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

lstFileNames = []

for ltemFile in os.listdir(os.path.join(os.getcwd(),"wc_input")):
    if os.path.isfile(os.path.join(os.getcwd(),"wc_input",ltemFile)):
#       print "is a file path", ltemFile
        lstFileNames.append(ltemFile)
    else:
        print "not a file", ltemFile
    
print "Input file count:", len(lstFileNames) 
# print sorted list
lstFileNames.sort()
print lstFileNames 

curr_line_no = 0

for inputCurr in lstFileNames:
    input_file_object = open(os.path.join(os.getcwd(), "wc_input", inputCurr), 'rU')
    try:
        for line in input_file_object:
            try:
                line.decode('ascii')
            except Exception, error:
                continue # Skip blanks <CR><LF>
            count_words_per_line = 0
            for word in line.split():
                count_words_per_line = count_words_per_line + 1

            # end of line, print mean
            if (curr_line_no == 0):
                try:
                    lst_running_median.append(count_words_per_line)
                    running_median =  count_words_per_line
                    print running_median
                except Exception, error:
                    print error
                    sys.exit(1)
            elif  (curr_line_no > 0):
                try:
                    lst_running_median.append(count_words_per_line)
                    running_median = medianWPLfn(lst_running_median)
                    print running_median
                except Exception, error:
                   print error
                   sys.exit(1)
            else:
                print "error: line < 0"
            # write to file
       	    output_file_object.write(str(running_median)+"\n")
            curr_line_no = curr_line_no + 1

    finally:
        input_file_object.close()

print "Total lines processed:", curr_line_no
output_file_object.close()


