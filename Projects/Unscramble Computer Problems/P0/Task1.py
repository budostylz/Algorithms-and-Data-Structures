"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

texts = ''
calls = ''
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
   

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


print('texts', texts)
print('calls', calls)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""DESIGN
Outputs:
  1. Count of different types of telephone numbers in both texts and calls

Inputs:
   1. Incoming number for texts
   2. Answering number for texts
   3. Incoming number of calls
   4. Answering number for calls

Functions/Call Stack
    1. countList:
        inputs: <texts>,<calls>
        outputs: count

    2. getNumberType: 
        inputs: <number>
        outputs: numberType('fixed', mobile, telemarketer)
        
    3. mergeTextsAndCalls:
        inputs: <calls> and <texts>
        outputs: callTextList




Psuedocode:

mergeTextsAndCalls;

_calls = calls;
texts = texts;

_callTextList = callTextList;

for(var i = 0; i < _calls.length; i++){//add calls
  _callTextList.push(_calls[i]);
}

for(var i = 0; i < texts.length; i++){//add texts
  _callTextList.push(texts[i]);
}

return _callTextList;



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

countList;

texts = texts;
_calls = calls;

listIndex = 0;

fixedCount = 0;
mobileCount = 0;
teleCount = 0;


//try merging texts and calls
list = mergeTextsAndCalls(_calls, texts)


while(list.length < listIndex){//iterate list
  
  incomingNumber = list[0];
  answeringNumber = list[1];
  
  
  type = getNumberType(incomingNumber)[0];
  typeCount = getNumberType(incomingNumber)[1];
  
  if(type == 'fixed'){
    fixedCount += typeCount;
  }
  else if(type == 'mobile'){
    mobileCount += typeCount;
  }
  else if(type === 'telemarketer'){
    teleCount += typeCount;
  }

  listIndex += 1;
}

count = fixedCount + mobileCount + teleCount;

return "There are <count> different telephone numbers in the records.";



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


getNumberType;
number = number;
number.length = 13;


if(number.length ===  10){
  
  return 'telemarketer', 1;
  
}else if(number.length ===  11){
  
  return 'mobile', 1;
  
}else if(number.length ===  13){
  
  return 'fixed', 1;
  
}




"""
