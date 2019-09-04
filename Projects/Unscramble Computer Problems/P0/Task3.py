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


# returns complete list of Bangalore numbers, part and whole percent values
def checkBangaloreAreaCodes(calls):

    bangaloreList = []
    whole = 0
    part = 0
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
             bangaloreList = setBangaloreAreaCodeList(incomingNumber, bangaloreList)


     if(incomingNumber[0] == '(' and incomingNumber[1] == '0' and incomingNumber[2] == '8' and incomingNumber[3] == '0'):#fixed incoming
              whole += 1
              if(answeringNumber[0] == '(' and answeringNumber[1] == '0' and answeringNumber[2] == '8' and answeringNumber[3] == '0'):#fixed answering
               part += 1
    
    return bangaloreList, part, whole

#returns partial Bangalore list
def setBangaloreAreaCodeList(incomingNumber, bangaloreList):

    checkRepeats = False

    for i, value in enumerate(bangaloreList):
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

 # returns output for requirement A
def outputA(sortedCodes):

    for i, value in enumerate(sortedCodes):
        print( "The numbers called by people in Bangalore have codes:" + str(value))
        print('-------------------------------------')

# returns output for requirement B        
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



