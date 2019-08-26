"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


#print('texts', texts)
#print('calls', calls)

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def getListData(texts, calls):

    
    firstIncomingTextNumber = texts[0][0]
    firstAnsweringTextNumber = texts[0][1]
    firstIncomingTextTime = texts[0][2]

    lastIndex = len(calls)-1

    lastIncomingCallNumber = calls[lastIndex][0]
    lastAnsweringCallNumber = calls[lastIndex][1]
    lastIncomingCallTime = calls[lastIndex][2]
    lastIncomingCallSeconds = calls[lastIndex][3]

  


    str = 'First record of texts, ' +firstIncomingTextNumber+  ' texts ' +firstAnsweringTextNumber+ ' at time ' + firstIncomingTextTime +'\n Last record of calls, '+lastIncomingCallNumber+' calls '+lastAnsweringCallNumber+' at time '+lastIncomingCallTime+', lasting '+lastIncomingCallSeconds+' seconds'

    return str

print(getListData(texts, calls))
