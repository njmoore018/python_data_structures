# Queues Introduction

A queue follows a "First In, First Out" (FIFO) ordering principle, meaning that the first element added to the queue will be the first one to be removed from the queue. This is also known as "First Come, First Serve" in many real-world applications. A queue can be implemented in Python by using a list.
```python
# Creation of an empty list, this will act as our queue
my_list = []
```

## Common Functions and Performance

- `Enqueue`: Add an item to the end of the queue. This operation has an efficiency of O(1).
```python
# Empty list
my_list = []
# Item you want to enqueue
item = "me"
# Enqueue operation
my_list.append(item)
```


- `Dequeue`: Remove an item from the front of the queue. Because a list requires all items to be shifted forward after one is removed, this operation has an efficiency of O(n).
```python
# List with items in it
my_list = ["me","you"]
# Dequeue and save the item in a variable for further use
item = my_list.pop()
```


- `Size`: Check and return the length of the queue. Because python stores the length of a list in a separate variable automatically when a list is created or updated, this operation has an efficiency of O(1).
```python
# List with items in it
my_list = ["me","you"]
# Check the list size and save it in a variable for further use
size = len(my_list)
```


- `isEmpty`: Also involves checking the size of the queue and then comparing the value with 0 to return a boolean value. Since this is the same as the 'Size' function mentioned above, it also has an efficiency of O(1).
```python
# Empty list
my_list = []
# Check if the list size is equal to zero
if len(my_list) == 0:
    print("The list is empty.")
```

## Applications

- A real world example of a queue would be a line for tickets at a movie theater. The teller assists people to purchase their tickets one at a time, in the same order in which people arrived.

## Example

## Problem

[Back to Welcome Page](0-welcome.md)