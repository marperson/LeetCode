'''
Created on Jun 2, 2016

@author: frank.he
'''

class LinkedList(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
        
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setDate(self,data):
        self.data = data
        
    def setNext(self,next):
        self.next = next
    
    def printList(self, head):
        while head:
            print (head.getData())
            head = head.next
            
        
'''
node1 = LinkedList('5')
node2 = LinkedList('2')
node3 = LinkedList('3')

node1.next = node2
node2.next = node3

Node().printList(node1)
#print (node2.getNext().getData())
'''