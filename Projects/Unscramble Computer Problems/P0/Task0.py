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

print('False2',False)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""DESIGN

Outputs:
 1. First record of texts
 2. Last records of calls
 3. Time of first record of texts
 4. Time of last record of calls
 5. Duration of last record of calls in seconds

 Inputs:
 1. Incoming Number
 2. Answering Number
 3. Time of First Record of Texts
 4. Time of last call
 5. Seconds of last call

 Functions:
 1. getFirstRecord : 
        inputs: <incoming number>, <answering number>, <time>
        return "First record of texts, <incoming number> texts <answering number> at time <time>"

 2. getSecondRecord : 
        inputs: <incoming number>, <answering number>, <time>, <during>
        return "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

 3. getTextData : 
        inputs: texts:list
        return <incoming number>, <answering number>, <time>

 4. getCallData : 
        inputs: calls:list
        return <incoming number>, <answering number>, <time>, <during>


Psuedocode:

GetFirstRecord(<incomingNumber>,<answeringNumber>,<time>)
 return "First record of texts, <incoming number> texts <answering number> at time <time>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GetSecondRecord(<incoming number>, <answering number>, <time>, <during>)
 return "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

getTextData(list)

if(list.length > 0){
  
  incomingNumber = list[0][0];
  answeringNumber = list[0][1];
  time = list[0][2];
  
  return incomingNumber, answeringNumber, time
}

return False

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
getCallData;

if(list.length > 0){
  
  incomingNumber = list[0][0];
  answeringNumber = list[0][1];
  time = list[0][2];
  during = list[0][2];
  
  return incomingNumber, answeringNumber, time, during
}

return False


"""

