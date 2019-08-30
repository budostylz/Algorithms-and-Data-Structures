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


def checkTelemarketNumbers(calls):

    telemarketList = []
   
    for i, value in enumerate(calls):
        if not(' ') in str(value[0]) and str(value[0][0]) != '(':
            checkRepeats(str(value[0]), telemarketList)

    return telemarketList

def checkRepeats(incomingNumber, telemarketList):

    checkRepeats = False

    for i, value in enumerate(telemarketList):
        if incomingNumber == str(value):
            checkRepeats = True

    if checkRepeats == False:
        telemarketList.append(incomingNumber)

    return telemarketList


#Apply Bubble Sort pattern from Udacity Sorting Algorithm Section. Worst Case is O(n^2) 
def teleSort(sortedScamerNumbers):
    for iteration in range(len(sortedScamerNumbers)):
        for index in range(1, len(sortedScamerNumbers)):
            this = sortedScamerNumbers[index]
            prev = sortedScamerNumbers[index - 1]

            if prev <= this:
                continue

            sortedScamerNumbers[index] = prev
            sortedScamerNumbers[index - 1] = this

    return sortedScamerNumbers

#drivers
scamerNumbers = checkTelemarketNumbers(calls)
sortedScamerNumbers = teleSort(scamerNumbers)
print('These numbers could be telemarketers: ')
for i, value in enumerate(sortedScamerNumbers):
        print('\t' + str(value))
