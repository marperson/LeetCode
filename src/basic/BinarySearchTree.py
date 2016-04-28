'''
Created on Apr 23, 2016

@author: marpe
'''
class BinarySearchTree(object):
    '''
    classdocs
    '''
    def __init__(self, data):
        '''
        Constructor
        '''
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        '''
        Build Binary Search Tree
        '''
        if data < self.data:
            if self.leftChild is None:
                self.leftChild = BinarySearchTree(data)
            else:
                self.leftChild.insert(data)
        if data > self.data:    
            if self.rightChild is None:
                self.rightChild = BinarySearchTree(data)
            else:
                self.rightChild.insert(data)
    
                
    def preorder(self):
        '''
        Pre Order: root, left, right
        '''
        if self.data is None:
            print ("Empty BST!")
            # return
        else:
            print (self.data)
            if not self.leftChild is None:
                self.leftChild.preorder()
            if not self.rightChild is None:
                self.rightChild.preorder()
            
    def inorder(self):
        '''
        In order: left, root, right
        '''
        if self.data is None:
            print ('Empty BST')
        else:
            if not self.leftChild is None:
                self.leftChild.inorder()
            print (self.data)
            if not self.rightChild is None:
                self.rightChild.inorder()
    
    def postorder(self):
        '''
        Post order: left, right, root
        '''
        if self.data is None:
            print ('Empty tree')
        
        else:
            if not self.leftChild is None:
                self.leftChild.postorder()
            if not self.rightChild is None:
                self.rightChild.postorder()
            print (self.data)
    
    def searchBST(self, data):
        '''
        Search BST
        '''
        if self.data is None:
            print ('Tree is Empty')
        else:
            if data < self.data:
                if not self.leftChild is None:
                    self.leftChild.searchBST(data)
                    
            elif data > self.data:
                if not self.rightChild is None:
                    self.rightChild.searchBST(data)
            else:
                print (self.data)
                
    def DeleteBSTNode(self, data):
        if self.data is None:
            print('Tree is empty')
        else:
            if (self.leftChild is None) and (self.rightChild is None):
                self.data
                
    
root = BinarySearchTree(6)
root.insert(2)
root.insert(7)
root.insert(4)
root.insert(3)
root.insert(5)
root.insert(11)
root.insert(8)
root.insert(13)



# root.preorder()
# root.inorder()
#root.postorder()
root.searchBST(12)

    
