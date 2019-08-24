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

 Functions/Call Stack
 1. getListData : 
        inputs: <texts> and <calls>
        return: textStr, _callStr 



Psuedocode:

getListData;

texts = texts;
_calls = _calls;

firstIncomingTextNumber = texts[0][0];
firstAnsweringTextNumber = texts[0][1];
firstIncomingTextTime = texts[0][2];

lastIncomingCallNumber = texts[0][0];
lastAnsweringCallNumber = texts[0][1];
lastIncomingCallTime = texts[0][3];

textStr = "First record of texts, <incoming number> texts <answering number> at time <time>";
_callStr = "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds";

 return textStr, _callStr





"""

