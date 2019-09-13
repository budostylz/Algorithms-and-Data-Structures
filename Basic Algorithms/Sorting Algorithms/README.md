# Sorting Algorithms

## Intro to Sorting
https://youtu.be/Z6yuIen71zM

## Bubble Sort
https://youtu.be/h_osLG3GmjE

## Efficiency of Bubble Sort
https://youtu.be/KddkHygi7is

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort1.PNG "Bubble Sort")

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort2.PNG "Bubble Sort")

![Bubble Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/bubblesort3.PNG "Bubble Sort")



## Bubble Sort Exercises
Now that you know how about bubble sort works, you'll implement bubble sort for two exercises.

### Exercise 1
Sam records when they wake up every morning. Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest.

```python

def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this
    print(l)

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")



```

### Exercise 2
Sam doesn't always go to sleep in the same hour. Given the following times Sam has gone to sleep, sort the times from latest to earliest.

```python

def bubble_sort_2(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)
    print(l)

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")

```

## Merge Sort
https://youtu.be/K916wfSzKxE

## Efficiency of Merge Sort
https://youtu.be/HKiK5Y-YSkks

![Merge Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/mergesort.PNG "Merge Sort")

![Merge Sort](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/mergesort2.PNG "Merge Sort")


## QuickSort
![New Tweet View](https://github.com/budostylz/Algorithms-and-Data-Structures/blob/master/Basic%20Algorithms/Sorting%20Algorithms/quickSort.PNG "New Tweet View")


