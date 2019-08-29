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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""DESIGN

    Outputs:
        1. List of codes called by people in Bangalore with no duplicates
        2. Percentage of fixed to fixed calls from and to Bangalore

    Inputs:
        1. Incoming Number
        2. Answering Number
      


    Functions/Call Stack
    
        1. checkBangaloreAreaCodes
            inputs: incoming number, list
            outputs: bangaloreList, percentageOfFixedToFixed

        2. setBangaloreAreaCodeList
            inputs: incoming number, bangaloreList
            outputs: bangaloreList
        
        3. outputAreaCodes
            inputs: bangaloreList
            outputs: "The numbers called by people in Bangalore have codes:"<list of codes>
        




Psuedocode:


checkBangaloreAreaCodes;

list = list;
bangaloreList = bangaloreList;
whole = 0;
part = 0;
percentage = 0;

for(var i = 0; i < list.length; i++){
  
   var incomingNumber = list[i][0];
   var answeringNumber = list[i][1];
   
   if((incomingNumber[0] === '0'  AND incomingNumber[1] === '8' AND incomingNumber[2] === '0') AND (answeringNumber[0] === '0'  AND answeringNumber[1] === '8' AND answeringNumber[2] === '0') )
   { 
          bangaloreList = setBangaloreAreaCodeList(incomingNumber, bangaloreList)
          whole += 1;
          part += 1;
   
   }
  
}
percentage = (part/whole);
percentageStr = "<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore.";

return bangaloreList, percentageStr;


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

setBangaloreAreaCodeList;

incomingNumber = inComingNumber;
bangaloreList = bangaloreList
checkRepeats = false

for(var i = 0; i < bangaloreList.length; i++){
  
    if(incomingNumber === bangaloreList[i]){
        checkRepeats = true;
    }
  
}

if(checkRepeats === false){
  bangaloreList.push(incomingNumber)
}

return bangaloreList;


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


outputAreaCodes;

bangaloreList = bangaloreList;


for(var i = 0; i < bangaloreList.length; i++){
  
  var code = bangaloreList[i];
  var str = "The numbers called by people in Bangalore have codes:<code>"";
  
  return str;
  
  
}




"""


def checkBangaloreAreaCodes(calls):

    bangaloreList = []
    whole = 0
    part = 0
    percentage = ''
    count = 0

    
    for i, value in enumerate(calls):
     
     incomingNumber =  str(value[0])
     answeringNumber = str(value[1])


     if(
         (incomingNumber[0] == '(' and incomingNumber[1] == '0' and incomingNumber[2] == '8' and incomingNumber[3] == '0')#fixed 
                                                or 
         (incomingNumber[0] == '7'  and incomingNumber[1] == '8' and incomingNumber[2] == '9')#mobile
                                                or
         (incomingNumber[0] == '1'  and incomingNumber[1] == '4' and incomingNumber[2] == '0') ):#tele  
             #print(incomingNumber)
             bangaloreList = setBangaloreAreaCodeList(incomingNumber, bangaloreList)


     if(incomingNumber[0] == '(' and incomingNumber[1] == '0' and incomingNumber[2] == '8' and incomingNumber[3] == '0'):#fixed incoming
              whole += 1
              if(answeringNumber[0] == '(' and answeringNumber[1] == '0' and answeringNumber[2] == '8' and answeringNumber[3] == '0'):#fixed answering
               part += 1
    
    return bangaloreList, part, whole


def setBangaloreAreaCodeList(incomingNumber, bangaloreList):

    checkRepeats = False

    for i, value in enumerate(bangaloreList):
        #print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))
        #print('-------------------------------------')
        if incomingNumber == str(value):
            checkRepeats = True

    if checkRepeats == False:
        bangaloreList.append(incomingNumber)

    return bangaloreList



#Apply Bubble Sort pattern from Udacity Sorting Algorithm Section. Worst Case is O(n^2) 
def bangaloreSort(bangaloreList):
    for iteration in range(len(bangaloreList)):
        for index in range(1, len(bangaloreList)):
            this = bangaloreList[index]
            prev = bangaloreList[index - 1]

            if prev <= this:
                continue

            bangaloreList[index] = prev
            bangaloreList[index - 1] = this

    return bangaloreList

def outputA(sortedCodes):

    for i, value in enumerate(sortedCodes):
        print( "The numbers called by people in Bangalore have codes:" + str(value))
        print('-------------------------------------')

        
def outputB(part, whole):


    #percentage =  [(fixedIncoming to (fixedAnswering)) / (fixedIncoming to (fixedAnswering + mobileAnswering + teleAnswering))] * 100
    rawPercent = str((part / whole) * 100)
    percentageStr = ''

    i = 0
    while(i < 5):
     percentageStr += rawPercent[i]
     i += 1

    print(percentageStr +  " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." )
         

#drivers
bangaloreResults = checkBangaloreAreaCodes(calls)
sortedCodes = bangaloreSort(bangaloreResults[0])
outputA(sortedCodes)
outputB(bangaloreResults[1], bangaloreResults[2])



