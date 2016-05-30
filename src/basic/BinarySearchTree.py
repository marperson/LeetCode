'''
Created on Apr 23, 2016

@author: marpe
'''
class BinarySearchTree(object):
    '''
    classdocs
    '''
    def __init__(self, root):
        '''
        Constructor
        '''
        self.root = root
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, root):
        '''
        Build Binary Search Tree
        '''
        if root < self.root:
            if self.leftChild is None:
                self.leftChild = BinarySearchTree(root)
            else:
                self.leftChild.insert(root)
        if root > self.root:    
            if self.rightChild is None:
                self.rightChild = BinarySearchTree(root)
            else:
                self.rightChild.insert(root)
    
                
    def preorder(self):
        '''
        Pre Order: root, left, right
        '''
        if self.root is None:
            print ("Empty BST!")
            # return
        else:
            print (self.root)
            if not self.leftChild is None:
                self.leftChild.preorder()
            if not self.rightChild is None:
                self.rightChild.preorder()
            
    def inorder(self):
        '''
        In order: left, root, right
        '''
        if self.root is None:
            print ('Empty BST')
        else:
            if not self.leftChild is None:
                self.leftChild.inorder()
            print (self.root)
            if not self.rightChild is None:
                self.rightChild.inorder()
    
    def postorder(self):
        '''
        Post order: left, right, root
        '''
        if self.root is None:
            print ('Empty tree')
        
        else:
            if not self.leftChild is None:
                self.leftChild.postorder()
            if not self.rightChild is None:
                self.rightChild.postorder()
            print (self.root)
    
    def searchBST(self, root):
        '''
        Search BST
        '''
        if self.root is None:
            print ('Tree is Empty')
        else:
            if root < self.root:
                if not self.leftChild is None:
                    self.leftChild.searchBST(root)
                    
            elif root > self.root:
                if not self.rightChild is None:
                    self.rightChild.searchBST(root)
            else:
                print (self.root)
                return self.root
                
    def deleteBSTNode(self, root):
        '''
        1. Call SearchBST method to find the node
        2. Node has three possibilities, 
            a. Node has no children
            b. Node has leftChild
            c. Node has rightChild
        '''
        if self.root is None:
            print('Tree is empty')
        else:
            myNode = self.searchBST(root)
            if (self.leftChild is None) and (self.rightChild is None):
                print (self.searchBST(root))
                #self.searchBST(root) = None
            elif (not self.leftChild is None) and (self.rightChild is None):
                self.leftChild.deleteBSTNode(root)
            elif (self.leftChild is None) and (not self.rightChild is None):
                self.root = self.rightChild
                
                
                
                
                
root = BinarySearchTree(6)
root.insert(2)
root.insert(7)
root.insert(4)
root.insert(3)
root.insert(5)
root.insert(11)
root.insert(8)
root.insert(13)

print ('BST:...')
root.preorder()


#root.preorder()
#root.inorder()
#root.postorder()
print ('pre order bst:')
root.searchBST(11)
print ('delte one node')
root.deleteBSTNode(2)
root.preorder()