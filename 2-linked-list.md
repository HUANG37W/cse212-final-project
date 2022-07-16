# Linked List
## Jason Huang - CSE 212
---
## Introduction
A linked list is a linear data structure consisting of a group of nodes where each node point to the next node through a pointer. Each node is composed of data and a reference (in other words, a link) to the next node in the sequence.

![Introduction of a linked list](.//intro.png)

#### Linked lists are among the simplest and most common data structures. The principal benefits of a linked list over a conventional array are:
* The list elements can easily be inserted or removed without reallocation or reorganization of the entire structure because the data items need not be stored contiguously in memory. Simultaneously, an array has to be declared in the source code before compiling and running the program.

* Linked lists allow the insertion and removal of nodes at any point in the list. They can do so with a constant number of operations if the link to the previous node is maintained during the list traversal.

On the other hand, simple linked lists by themselves do not allow random access to the data or any form of efficient indexing. Thus, many basic operations – such as obtaining the last node of the list, finding a node containing a given data, or locating the place where a new node should be inserted – may require sequential scanning of most or all of the list elements.

---

## Linked List Representation
#### Linked list can be visualized as a chain of nodes, where every node points to the next node.

![Illustration of a linked list](.//linked_list.png)

#### As per the above illustration, following are the important points to be considered.

* Linked List contains a link element called first.

* Each link carries a data field(s) and a link field called next.

* Each link is linked with its next link using its next link.

* Last link carries a link as null to mark the end of the list.

---

## Search an Element in Linked List without Recursion
This is a Python program to search for an element in a linked list without using recursion.

#### Problem Description
The application shows the linked list's index and asks the user for a key to search it.

#### Problem Solution
1. Create a class Node.
2. Create a class LinkedList.
3. To append data and display the linked list, respectively, define the methods append and display inside the class LinkedList.
4. Define method find_index to search for the key.
5. find_index uses a loop to iterate over the nodes of the linked list to search for the key.
6. Create an instance of LinkedList, append data to it and display the list.
7. Request a search key from the user, then have them look for it.

#### Program Codes:

```python
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
    def find_index(self, key):
        current = self.head
 
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
 
        return -1

a_list = LinkedList()
for data in [4, -3, 1, 0, 9, 11]:
    a_list.append(data)
print('The linked list: ', end = '')
a_list.display()
print()
 
key = int(input('What data item would you like to search for? '))
index = a_list.find_index(key)
if index == -1:
    print(str(key) + ' was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')    
```

#### Program Explanation
1. A LinkedList object is constructed.
2. The list is supplemented with a few entries.
3. The shown linked list.
4. A key to start the search is requested of the user.
5. The find index function looks up the index. If the key cannot be located, it returns -1.
6. If the index is located, it is shown.

---

## Linked List Operation & Efficiency

| Operation     | Performance | Explanation                                                                                                                                                                                  |
| ------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| insert_head   | O(1)        | Only the head's pointers, both the new and old head nodes, need to be adjusted.                                                                                                                |
| insert_tail   | O(1)        | Only the tail's pointers, both the new and old tail nodes, need to be adjusted.                                                                                                                |
| insert_middle | O(n)        | Only needs to adjust the the pointers of the middle, the new and old nodes relating to the middle. O(n) performance comes with looping and finding the middle (targeted) insertion location. |
| remove_head   | O(1)        | Only needs to adjust the the pointer of the head, the new head node.                                                                                                                         |
| remove_tail   | O(1)        | Only needs to adjust the the pointer of the tail, the new tail node.                                                                                                                         |
| remove_middle | O(n)        | Only needs to adjust the the pointers of the middle, the nodes relating to the middle. O(n) performance comes with looping and finding the middle (targeted) deletion location.              |
| length        | O(1)        | Built-in python function                                                                                                                                                                     |
| empty         | O(1)        | Just check the length to see if it's 0                                                                                                                                                       |
---

## Example: Creating a Music Playlist

In computer science, linked lists are significant data structures. A linked list is a set of nodes that are organized in a linear fashion and each node in the list has a data value and a reference to the node after it. In this tutorial, we'll go through how to create a single linked list that corresponds to a playlist of music.

### Requirements:
Let’s get started!

First, we will define a class called ‘MusicNode’. In the argument of the ‘__init__’ method, we will initialize and define attributes ‘current_music’ and ‘next_music’ as ‘None’:

```python
class MusicNode:
    def __init__(self, current_music=None, next_music = None):
        self.current_music = current_music
        self.next_music = next_music
```

Now, let’s write a class that will allow us to build our linked music list. Let’s call this class ‘MusicList’:

```python
class MusicList:
    def __init__(self):  
        self.head = None
```

We will use the ‘MusicList’ class, which will contain a reference to the ‘MusicNode’ type, to initialize our music list object. Let’s write an instance of our music list class and print the result:

```python
if __name__=='__main__':
    #initialize linked list object
    linked_list = MusicList()
    print(linked_list)
```

Now let’s build a linked list of music for our playlist. Let’s select the top 3 music of all time by The Beatles according to Entertainment Weekly. To start let’s define the value of each node. (Note: The ‘…’ corresponds to omitted code):

```python
if __name__=='__main__':
    ... 
    #assign values to nodes 
    linked_list.head = MusicNode("A Hard Day's Night")
    second = MusicNode('A Day in the Life')
    third = MusicNode("Strawberry Fields Forever")
```

Now let’s define the ‘next music’ value of the head node (the first music):

```python
if __name__=='__main__':
    ...
    #link nodes
    linked_list.head.next_music = second
```


Then we define the ‘next song’ value of the second node:

```python
if __name__=='__main__':
    ...
    second.next_song = third
```

Next, let’s define a simple function that will allow us to traverse our linked music list. In a while loop we’ll print the value of the current music and redefine the current value as the next music until it reaches the tail of the linked list, which points to null:

```python
class MusicList:   
    ...
    def printMusic(self): 
        value = self.head 
        while (value): 
            print(value.current_music) 
            value = value.next_music
```

Next, let’s print our list of songs:

```python
if __name__=='__main__':
    ...
    linked_list.printMusic()
```

## Problem to Solve

