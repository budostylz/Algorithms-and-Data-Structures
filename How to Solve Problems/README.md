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




Problem Solving Steps

        1. Map Inputs
        2. Map Outputs
        3. Work out Examples to Identify Relationships between Inputs and Outputs
        4. Write psuedocode
        5. Should we Implement the Psuedocode in Code
        6. Find a Simple Mechanical Solution
        7. What Should We Write First
