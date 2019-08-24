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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""DESIGN
Outputs:
  1. List of telemarketing numbers

Inputs:
   1. Incoming number of calls

    Functions/Call Stack
    
        1. checkTelemarketNumbers
            inputs: list
            outputs: teleMarketList

        2. setTeleMarketList
            inputs: incoming number, teleMarketList
            outputs: teleMarketList
        
        3. outputTeleMarketNumbers
            inputs: teleMarketList
            outputs: "These numbers could be telemarketers:"<list of numbers>




Psuedocode:

checkTelemarketNumbers;
list = list;
teleMarketList = teleMarketList;
for(var i = 0; i < list.length; i++){
  
   var incomingNumber = list[i][0];
   
   if(incomingNumber[9] === '0'  AND incomingNumber[8] === '4' AND incomingNumber[7] === '1' )
   {        
          teleMarketList = setTeleMarketList(incomingNumber, teleMarketList) 
   }
   
}
return teleMarketList;


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

setTeleMarketList;

incomingNumber = inComingNumber;
teleMarketList = teleMarketList
checkRepeats = false

for(var i = 0; i < teleMarketList.length; i++){
  
    if(incomingNumber === teleMarketList[i]){
        checkRepeats = true;
    }
  
}

if(checkRepeats === false){
  teleMarketList.push(incomingNumber)
}

return teleMarketList;


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

outputTeleMarketNumbers;

teleMarketList = teleMarketList;


for(var i = 0; i < teleMarketList.length; i++){
  
  var code = teleMarketList[i];
  var str = "These numbers could be telemarketers: <list of numbers>";
  
  return str;
  
  
}





"""




