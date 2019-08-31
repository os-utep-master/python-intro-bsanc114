import re
import sys
import string
outputFname = sys.argv[2]
inputFname = sys.argv[1]
file = open(inputFname, "r")
text = file.read().lower()
text = re.sub(r'[^\w]',' ',text).strip().split()
text.sort()
dictionary = {}
for w in text:
    if w not in dictionary.keys():
        dictionary[w]=1
    else:
        count = dictionary[w]
        dictionary[w]= count+1
output = open(outputFname,"w+")
for word in dictionary:
    output.write(word+" "+str(dictionary[word])+"\n")
output.close()
file.close()