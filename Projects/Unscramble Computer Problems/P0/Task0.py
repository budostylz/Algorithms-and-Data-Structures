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

 Functions/Call Stack
 1. getListData : 
        inputs: <texts> or <calls>
        return: string 



Psuedocode:

getListData;

list = list

incomingNumber = '';
answeringNumber = '';
time = '';
dataTag = 'text';



if(list.length > 0){
  
  
  if(dataTag === 'text'){
    
    incomingNumber = list[0][0];
    answeringNumber = list[0][1];
    time = list[0][2];
    return "First record of texts, <incoming number> texts <answering number> at time <time>"
    
  }else{
    
    incomingNumber = list[list.length - 1][0];
    answeringNumber = list[list.length - 1][1];
    time = list[list.length - 1][2];
    during = list[list.length - 1][3];
    return "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
  }
  
  
}


"""

