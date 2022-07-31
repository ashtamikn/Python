from asyncio.windows_events import NULL
import math
import os
import random
import re
import sys
class sllNode:
    def __init__(self, node_data):
        self.data=node_data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def insert(self,node_data):
        node=sllNode(node_data)
        if not self.head:
                self.head = node
        else:
            ptr=self.head
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=node
        
    def print_doubly_linked_list(self,node):
        ptr=self.head
        while(self.ptr!=None):
            print(ptr.data)
        print(ptr.data)

if __name__ == '__main__':
    s=sll()
    for i in range(1,11):
     if i%2==0:
        s.insert(i)
    
    

        
            

