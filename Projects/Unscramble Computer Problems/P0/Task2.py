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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import datetime

def getSeptemberDates(calls):

    septList = []
  

    for i, value in enumerate(calls):
        dateStr = str(value[2])
        septDate = testSeptDate(dateStr)

<<<<<<< HEAD
        if(septDate == True):
           septList.append(value)
=======
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
>>>>>>> 32d4fba0728cd6fa976ac0b34e11fbaec2f9f08c

    return septList

def testSeptDate(dateStr):

<<<<<<< HEAD
   dayTest = int(dateStr.split('-')[0])
   month = 0;

   if dayTest > 12:
       dateObj =  datetime.datetime.strptime(dateStr, '%d-%m-%Y %H:%M:%S')
       month = dateObj.month
   else:
       dateObj =  datetime.datetime.strptime(dateStr, '%m-%d-%Y %H:%M:%S')
       month = dateObj.month

   if month == 9:
       return True
   else:
       return False

=======
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
>>>>>>> 32d4fba0728cd6fa976ac0b34e11fbaec2f9f08c

def getHighTime(sortedSeptemberList):


    item = sortedSeptemberList[len(sortedSeptemberList)-1]
    answeringNumber = item[1]
    totalTime = str(int(item[3])+1)# Add one second for answering call

    return answeringNumber + " spent the longest time, "+totalTime+" seconds, on the phone during September 2016."


septemberList = getSeptemberDates(calls)


#Applied Bubble Sort function from Udacity Sorting Algorithm Section
def septemberSort(septemberList):
    for iteration in range(len(septemberList)):
        for index in range(1, len(septemberList)):
            this = int(septemberList[index][3])
            prev = int(septemberList[index - 1][3])

            if prev <= this:
                continue

            septemberList[index] = septemberList[index - 1]
            septemberList[index - 1] = septemberList[index]

    return septemberList

<<<<<<< HEAD
print('Sorting September List Using Bubble Sort...')
sortedSeptemberList = septemberSort(septemberList)
print(getHighTime(sortedSeptemberList))
=======
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import datetime

def getSeptemberDates(calls):

    septList = []
  

    for i, value in enumerate(calls):
        dateStr = str(value[2])
        septDate = testSeptDate(dateStr)

        if(septDate == True):
           septList.append(value)

    return septList

def testSeptDate(dateStr):

   dayTest = int(dateStr.split('-')[0])
   month = 0;

   if dayTest > 12:
       dateObj =  datetime.datetime.strptime(dateStr, '%d-%m-%Y %H:%M:%S')
       month = dateObj.month
   else:
       dateObj =  datetime.datetime.strptime(dateStr, '%m-%d-%Y %H:%M:%S')
       month = dateObj.month

   if month == 9:
       return True
   else:
       return False


def getHighTime(sortedSeptemberList):


    item = sortedSeptemberList[len(sortedSeptemberList)-1]
    answeringNumber = item[1]
    totalTime = str(int(item[3])+1)# Add one second for answering call

    return answeringNumber + " spent the longest time, "+totalTime+" seconds, on the phone during September 2016."


septemberList = getSeptemberDates(calls)


#Applied Bubble Sort function from Udacity Sorting Algorithm Section
def septemberSort(septemberList):
    for iteration in range(len(septemberList)):
        for index in range(1, len(septemberList)):
            this = int(septemberList[index][3])
            prev = int(septemberList[index - 1][3])

            if prev <= this:
                continue

            septemberList[index] = septemberList[index - 1]
            septemberList[index - 1] = septemberList[index]
>>>>>>> 32d4fba0728cd6fa976ac0b34e11fbaec2f9f08c

    return septemberList

print('Sorting September List Using Bubble Sort...')
sortedSeptemberList = septemberSort(septemberList)
print(getHighTime(sortedSeptemberList))
