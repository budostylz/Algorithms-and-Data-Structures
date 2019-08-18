"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print('texts', texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


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

Functions:
    1. getFixedNumbersCount: 
        inputs: <number>
        outputs: <count>
    
    2. getMobileNumbersCount: 
        inputs: <number>
        outputs: <count>

    3. getTeleNumbersCount: 
        inputs: <number>
        outputs: <count>

    4. getNumberType: 
        inputs: <number>
        outputs: numberType('fixed', mobile, telemarketer)




Psuedocode:

getFixedNumbersCount;
number = number;
type = getNumberType(number);
type = 'fixed';


if(type == 'fixed'){
  return 1;
}
else if(type == 'mobile'){
  return 1;
}
else if(type === 'telemarketer'){
  return 1;
}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

getMobileNumbersCount;
number = number;
type = getNumberType(number);
type = 'mobile';


if(type == 'fixed'){
  return 1;
}
else if(type == 'mobile'){
  return 1;
}
else if(type === 'telemarketer'){
  return 1;
}


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

getTeleNumbersCount;
number = number;
type = getNumberType(number);
type = 'telemarketer';


if(type == 'fixed'){
  return 1;
}
else if(type == 'mobile'){
  return 1;
}
else if(type === 'telemarketer'){
  return 1;
}



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


getNumberType;
number = number;
number.length = 13;


if(number.length ===  10){
  
  return 'telemarketer';
  
}else if(number.length ===  11){
  
  return 'mobile';
  
}else if(number.length ===  13){
  
  return 'fixed';
  
}




"""
