"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print('calls', calls)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


"""DESIGN

    Outputs:
        1. Telephone number that spent longest time in September 2016
        2. Longest time in seconds in September 2016

    Inputs:
        1. Answering Number
        2. Time
        3. Seconds

    Functions/Call Stack
        1. getSeptemberDates
            inputs: calls
            output: list: list of September dates
        
        2. getHighTime
            inputs: calls: list with September dates
            output: "<telephone number> spent the longest time, <total time> seconds, on the phone during

Psuedocode:

getSeptemberDates;

_calls = _calls;
highTime = 0;
septArr = [];

for(var i =0; i < _calls.length; i++){
  
    test1 = _calls[2]:TestRegEx('15-09-2016 13:17:58');
    test2 = _calls[2]:TestRegEx('9/9/2016  5:38:13 PM');
    
    if(test1 OR test2)
      septArr.push(_calls);
      
  
}

return septArr;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
getHighTime;

_calls = _calls;
sort(_calls);
highTimeRecord = _calls[_calls.length -1];

return "highTimeRecord[1] spent the longest time, highTimeRecord[3] seconds, on the phone during September 2016."













"""



