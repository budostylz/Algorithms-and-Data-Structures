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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

"""

def mergeTextsAndCalls(texts, calls):

    callTextList = []

    for i, value in enumerate(texts):
        callTextList.append(value)
        
    for i, value in enumerate(calls):
        callTextList.append(value)
        
    return callTextList

def countList(callTextList):

    
    fixedCount = 0
    mobileCount = 0
    teleCount = 0

    for i, value in enumerate(callTextList):
        incomingNumber = value[0]
        answeringNumber = value[1]

        type = getNumberType(incomingNumber)[0]
        typeCount = getNumberType(incomingNumber)[1]

        if type == 'fixed':
            fixedCount += typeCount
        elif type == 'mobile':
            mobileCount += typeCount
        elif type == 'telemarketer':
            teleCount += typeCount


    count = str(fixedCount + mobileCount + teleCount)

    return "There are "+count+" different telephone numbers in the records."

def getNumberType(number):

    numberLength = len(number)
    
    if numberLength == 10:
        return 'telemarketer', 1
    elif numberLength == 11:
        return 'mobile', 1
    elif numberLength == 13:
        return 'fixed', 1
        
    

callTextList = mergeTextsAndCalls(texts, calls)
print(countList(callTextList))

