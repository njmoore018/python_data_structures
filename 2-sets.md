# Sets Introduction
A set is an unordered collection of unique elements in Python. It can be implemented in Python using the set() function or using curly braces {}.
Here's how to create an empty set:
```python
# Creation of an empty set
my_set = set()
```

## Common Functions and Performance
-`Add`: Add an element to the set. This operation has an efficiency of O(1).
```python
# Empty set
my_set = set()
# Element you want to add
item = "apple"
# Add operation
my_set.add(item)
```

-`Remove`: Remove an element from the set. This operation has an efficiency of O(1).
```python
# Set with elements in it
my_set = {"apple", "banana", "cherry"}
# Remove an element
my_set.remove("banana")
```

-`Membership`: Check if an item is in the set. This operation has an efficiency of O(1).
```python
# Set with items in it
my_set = {"me","you"}
# Check if an item is in the set
if "me" in my_set:
    print("me is in the set")
```

-`Size`: Check and return the length of the set. This operation has an efficiency of O(1).
```python
# Set with items in it
my_set = {"me","you"}
# Check the set size and save it in a variable for further use
size = len(my_set)
```

-`Union`: Return the union of two sets as a new set. This operation has an efficiency of O(n), where n is the total size of the sets being unioned.
```python
# Two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "mango", "banana"}
# Union of two sets
set3 = set1.union(set2)
```

-`Intersection`: Return the intersection of two sets as a new set. This operation has an efficiency of O(n), where n is the total size of the sets being intersected.
```python
# Two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "mango", "banana"}
# Intersection of two sets
set3 = set1.intersection(set2)
```

## Applications
Sets can be used in a wide variety of applications. Some examples include:

- `Checking for duplicates`: Since sets only allow unique elements, they can be used to quickly and easily check for duplicates in a collection of data.
- `Finding unique elements`: Sets can be used to find unique elements in a collection of elements.
- `Data processing`: Sets can be used to perform operations such as union, intersection, and difference on collections of data.
- `Filtering`: Sets can be used to filter out unwanted data from a collection.

## Example
Suppose you are building a program to track the winners of a contest. You want to ensure that each winner only appears once in your records, so you decide to use a set.
```python
# Create an empty set to hold the winners
winners = set()

# Add the winners to the set
winners.add("John")
winners.add("Jane")
winners.add("Mike")

# Check if a winner is in the set
if "John" in winners:
    print("John is a winner!")

# Remove a winner from the set
winners.remove("Mike")

# Check the size of the set
print(len(winners))
```

## Problem
Suppose you are working on a project where you are analyzing the frequency of words in a set of documents. You have a set of keywords that you are interested in tracking, and you want to count the number of occurrences of each keyword in the documents.

Your goal is to write a Python program that takes in a set of keywords and a list of documents, and outputs a dictionary that maps each keyword to the total number of occurrences across all the documents.

For example, suppose you have the following set of keywords:
```python
keywords = {"apple", "banana", "orange"}
```

And you have the following list of documents:
```python
documents = [
    "I ate an apple for breakfast this morning",
    "I prefer bananas to oranges",
    "Oranges are high in vitamin C"
]
```

Your program should output the following dictionary:
```python
{
    "apple": 1,
    "banana": 1,
    "orange": 2
}
```

This is because "apple" appears once, "banana" appears once, and "orange" appears twice across all the documents.

[View Solution](solutions/2-sets.py)

[Back to Welcome Page](0-welcome.md)