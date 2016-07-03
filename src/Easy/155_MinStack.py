'''
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''


class Solution:

    def __init__(self):
        self.stack=[]
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[len(self.stack)-1]
    
    def getMin(self):
        return min(self.stack)
            


x = Solution()
x.push(-2)
x.push(0)
x.push(-3)
print (x.getMin())
x.pop()
print(x.top())
print (x.getMin())
        
    
        