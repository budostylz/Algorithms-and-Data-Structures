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
    
        1. sortList
            inputs: list
            outputs: sortedCalls
            
        2. getSeptemberDates
            inputs: sortedCalls
            output: list: septDates
           
        2. testSeptDate
             inputs: date
             output: boolean
        
        4. getHighTime
            inputs: sortedCalls
            outputs: "<telephone number> spent the longest time, <total time> seconds, on the phone during

Psuedocode:

getSeptemberDates;

_calls = _calls;
septList = [];

for(var i =0; i < _calls.length; i++){
  
    test1 = testSeptDate(_calls[2])
    test2 = testSeptDate(_calls[2])
    
    if(test1 OR test2)
      septList.push(_calls);
      
  
}

return septList;


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
testSeptDate;

dateStr = dateStr;

newDate = new Date(dateStr)

checkSept = newDate.month

if(checkSept.month === 9){
    return true;
}else{
    return false;
}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sortList;

_calls = _calls;

sortedCalls = sort(_calls);

return soretedCalls;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
getHighTime;

_calls = _calls;
highTimeRecord = _calls[_calls.length -1];

return "highTimeRecord[1] spent the longest time, highTimeRecord[3] seconds, on the phone during September 2016."



"""
