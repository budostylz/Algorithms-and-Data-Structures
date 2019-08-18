## Online Psuedocode Editor
https://code2flow.com/app

## How to Solve Problems
https://youtu.be/E6t0oGRXXh8

https://youtu.be/uJ4bfRfuSjE

## Understand the Problem
https://youtu.be/N8dKtrrCZ7U

## Find Inputs and Outputs of a Problem
https://youtu.be/hkspB2e0S9A

## 1. What are the Inputs
https://youtu.be/yh00phtQ-vE

## Ask questions about the inputs
https://youtu.be/cAr-unfe-mg

## Encode the Inputs
https://youtu.be/kG94A6xHqZk

## 2. What are the Outputs
https://youtu.be/5vjhu_cssNQ
      
## Take the Next Step
https://youtu.be/L4vB8eu6Wo8

## Steps
https://youtu.be/NZq4vDooURs

## Work Out Examples
https://youtu.be/3XiisY0IPPU

## Work Out Examples2
https://youtu.be/trokjJravhc

## Try an Example
https://youtu.be/X29RjzKHsWU

## Harder Example
https://youtu.be/-eAKNo9cA6Y

## Algorithm Psuedocode
https://youtu.be/Ei91QeYiG_E

## Should We Implement the Psuedocode
https://youtu.be/osHXLCQ9TKE

## Different Approach
https://youtu.be/czjMsAXjWVg

## Simple Mechnaical Algorithm
https://youtu.be/gPfkboHV3QA

## Don't Optimize Prematurely
https://youtu.be/uQDk8euwyDI

## What Should We Write First
https://youtu.be/HRepefDqkDM

  
## Step Two Helper Function
https://youtu.be/lpprz4op11k

```python
#Solution : https://youtu.be/Qttkfhh3I5s

### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:

## Test Next Day
## Test case nextDay(2012, 1, 1) : good
## Test case nextDay(2012, 12, 1): good

## Test Next Month
## Test case nextDay(2012, 4, 30) is not correct!

## Test Next Year
## Test case nextDay(1999, 12, 30) is not correct!
## Test case nextDay(2012, 12, 30) is not correct!

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    if(day < 30):
       return year, month, day + 1
    else:
        if(month < 12):
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
    
            
print(nextDay(2012, 12, 30))

```

## Making Progress is Good
https://youtu.be/cUFZPid3yVw

## What Should We Do Next?
https://youtu.be/ZETmw5tFcFU

## Step One Pseudocode
https://youtu.be/hJzpU5qC3hs

## Step Three daysBetweenDates
https://youtu.be/DOkkOsraobw

```python

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
   
   
    # YOUR CODE HERE!
    numberOfDays=0
    daysInYears = (year2 - year1) * 360
    daysInMonths = (month2 - month1) * 30
    days = (day2 - day1)
    numberOfDays = (daysInYears+daysInMonths+days)

    # INSTRUCTOR'S CODE
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

    
    return numberOfDays
        

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
       
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """ Returns True if year1-month1-day1 is before
        year2-month2-day2. Otherwise, returns False."""

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

```
## Test for Valid Inputs
https://video.udacity-data.com/topher/2016/September 57d09523_test-for-valid-inputs-intro-to-computer-science/test-for-valid-inputs-intro-to-computer-science_720p.mp4

```python

# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#  

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

     

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print "Test case passed!"
            else:
                print "Test with data:", args, "failed"
    
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)            
test()

```

## Real World Problem
https://video.udacity-data.com/topher/2016/September/57d163a7_real-world-problem-intro-to-computer-science/real-world-problem-intro-to-computer-science_720p.mp4

## Best Strategy
https://video.udacity-data.com/topher/2016/September/57d13903_best-strategy-intro-to-computer-science/best-strategy-intro-to-computer-science_720p.mp4

A stub is a dummy implementation of the method. It can be used for testing before you code the whole function.

In order to answer this question, you should think about the dependencies between the various steps, but also about what order of implementing and testing them will be most likely to efficiently lead to a correct solution.

It's definitely a subjective question, and there are many reasonable answers to this question. Because of this, your answer will not be graded. But watching the instructor explain his solution will help you evaluate your solution.

## Assert Statements in Python
https://dbader.org/blog/python-assert-tutorial

Problem Solving Steps

        1. Map Inputs
        2. Map Outputs
        3. Work out Examples to Identify Relationships between Inputs and Outputs
        4. Write psuedocode
        5. Should we Implement the Psuedocode in Code
        6. Find a Simple Mechanical Solution
        7. What Should We Write First
