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


#Apply Bubble Sort pattern from Udacity Sorting Algorithm Section
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



#Apply QuickSort pattern from Udacity Sorting Algorithm Section
def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = int(items[pivot_index][3])

    while (pivot_index != left_index):

        item = int(items[left_index][3])
        itemCache = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = items[pivot_index]
        items[pivot_index] = itemCache
        pivot_index -= 1
    
    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    
septemberList = getSeptemberDates(calls)
quicksort(septemberList)
print(getHighTime(septemberList))




