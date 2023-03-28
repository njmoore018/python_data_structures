# Queues Introduction

A queue follows a "First In, First Out" (FIFO) ordering principle, meaning that the first element added to the queue will be the first one to be removed from the queue. This is also known as "First Come, First Serve" in many real-world applications. A queue can be implemented in Python by using a list.
```python
# Creation of an empty list, this will act as our queue
my_list = []
```

## Common Functions and Performance

- `Enqueue`: Add an item to the end of the queue. This operation has an efficiency of O(1).
```python
# Empty queue
my_queue = []
# Item you want to enqueue
item = "me"
# Enqueue operation
my_queue.append(item)
```

- `Dequeue`: Remove an item from the front of the queue. Because a python list requires all items to be shifted forward after one is removed, this operation has an efficiency of O(n).
```python
# Queue with items in it
my_queue = ["me","you"]
# Dequeue and save the item in a variable for further use
item = my_queue.pop()
```

- `Size`: Check and return the length of the queue. Because python stores the length of a list in a separate variable automatically when a list is created or updated, this operation has an efficiency of O(1).
```python
# Queue with items in it
my_queue = ["me","you"]
# Check the queue size and save it in a variable for further use
size = len(my_queue)
```

- `isEmpty`: Also involves checking the size of the queue and then comparing the value with 0 to return a boolean value. Since this is the same as the 'Size' function mentioned above, it also has an efficiency of O(1).
```python
# Empty queue
my_queue = []
# Check if the queue size is equal to zero
if len(my_queue) == 0:
    print("The list is empty.")
```

## Applications

Queues can be used in a wide variety of applications. Some examples include:
- `Scheduling Tasks`: In task scheduling applications, queues can be used to manage the order in which tasks are executed. Each task can be added to the queue, and the tasks can be executed in the order that they were added.
- `Event-driven programming`: In event-driven programming, queues can be used to manage events and callbacks. When an event occurs, it can be added to the queue, and the callbacks associated with that event can be executed in order.
- `Web server requests`: In web server applications, requests from clients can be added to a queue to be processed by the server. This allows the server to handle a large number of requests simultaneously without overwhelming the system.

## Example
- Suppose you are building a program to simulate a printing queue for a printer. The printer can only print one document at a time, so if multiple documents are waiting to be printed, they must be queued up and printed in order.

```python
# Create the empty queue
print_queue = []

# Add a few documents to the printing queue
print_queue.append("homework.pdf")
print_queue.append("grocery_list.pdf")
print_queue.append("tax_return.pdf")

# Dequeue a document from the list to simulate completion of printing
print_queue.pop()

# Check the size of our queue to verify the homework document was removed
print(len(print_queue))
```

## Problem

Suppose you are building a program to simulate a customer service queue for a call center. The call center has multiple customer service representatives, but when all representatives are busy, incoming calls must be queued up and handled in order.

If multiple representatives become available at the same time, the call should be assigned to the representative who has been idle for the longest amount of time.

Your program should keep track of the call queue using a Python list implemented as a queue.

`Hint`: Using a queue for the representatives would easily allow you to determine who has been idle the longest, as they will be first in the queue.

[View Solution](solutions/1-queues.py)

[Back to Welcome Page](0-welcome.md)