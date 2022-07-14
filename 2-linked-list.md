# Linked List
## Jason Huang - CSE 212
---
## Introduction
#### A linked list is a sequence of data structures, which are connected together via links.
#### Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array. Following are the important terms to understand the concept of Linked List.
* Link − Each link of a linked list can store a data called an element.

* Next − Each link of a linked list contains a link to the next link called Next.

* LinkedList − A Linked List contains the connection link to the first link called First.

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

## Search within a Linked List



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

First, we will define a class called ‘MusicNode’. In the argument of the ‘__init__’ method, we will initialize attributes ‘current_music’ and ‘next_music’ as ‘None’:

Next we define the class attributes, ‘current_music’ and ‘next_music’:

Now, let’s write a class that will allow us to build our linked music list. Let’s call this class ‘MusicList’:

We will use the ‘MusicList’ class, which will contain a reference to the ‘MusicNode’ type, to initialize our music list object. Let’s write an instance of our music list class and print the result:

Now let’s build a linked list of music for our playlist. Let’s select the top 3 music of all time by The Beatles according to Entertainment Weekly. To start let’s define the value of each node. (Note: The ‘…’ corresponds to omitted code):

Now let’s define the ‘next music’ value of the head node (the first music):

Then we define the ‘next song’ value of the second node:

Next, let’s define a simple function that will allow us to traverse our linked music list. In a while loop we’ll print the value of the current music and redefine the current value as the next music until it reaches the tail of the linked list, which points to null:

Next, let’s print our list of songs:



```python
class MusicNode:
    def __init__(self, current_music=None, next_music = None):

class MusicNode:
    def __init__(self, current_music=None, next_music = None):
        self.current_music = current_music
        self.next_music = next_music

class MusicList:
    def __init__(self):  
        self.head = None

if __name__=='__main__':
    #initialize linked list object
    linked_list = MusicList()
    print(linked_list)

if __name__=='__main__':
    ... 
    #assign values to nodes 
    linked_list.head = MusicNode("A Hard Day's Night")
    second = MusicNode('A Day in the Life')
    third = MusicNode("Strawberry Fields Forever")

if __name__=='__main__':
    ...
    #link nodes
    linked_list.head.next_music = second

if __name__=='__main__':
    ...
    second.next_song = third

class MusicList:   
    ...
    def printMusic(self): 
        value = self.head 
        while (value): 
            print(value.current_music) 
            value = value.next_music

if __name__=='__main__':
    ...
    linked_list.printMusic()













## Problem to Solve