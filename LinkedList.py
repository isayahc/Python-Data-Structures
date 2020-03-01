#! /usr/bin/env python

class Node(object):
    def __init__ (self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.cur_node = None 

    def add_node (self, data):
        new_node = Node() # create a new node
        new_node.data = data 
        new_node.next = self.cur_node
        self.cur_node = new_node 

    def list_print(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next

    def size(self):
        node = self.cur_node
        size = 0
        while node:
            size +=1 
            node = node.next
        return size

    def InsertInX(self,data,pos):
        #add assertion
        #create new node 
        new_node = Node()
        new_node.data = data
        #get head ;)
        node = self.cur_node 
        size = 0
        while node:
            if(size == pos):
                new_node.next = node.next
                node.next = new_node
            node = node.next
            size +=1 
    
    def DeleteInX(self,pos):
        #get head
        node = self.cur_node
        size = 0
        while node:
            if(size == pos-1):
                node.next = node.next.next

            node = node.next
            size +=1 





                


if __name__ == '__main__':
    ll = LinkedList()
    x = list(range(10))
    for i in x:
        ll.add_node(i)

    # ll.list_print()
    # ll.InsertInX(10,3)
    # print()
    # ll.list_print()
    # print()
    # ll.DeleteInX(3)
    # ll.list_print()
    ll.DeleteInX(3)
    ll.list_print()