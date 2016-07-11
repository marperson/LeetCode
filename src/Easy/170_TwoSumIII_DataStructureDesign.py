'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); 
add(3); 
add(5);
find(4) -> true
find(7) -> false

'''


class Solution:
    def __init__(self):
        data = []
    
    data=[]
    # @param v, integer value
    def add(self, v):
        self.data.append(v)
        print (self.data)
    
    # @param v, integer value
    # @return boolean
    def hasValue(self,v):
        lenData = len(self.data)
        print(lenData)
        if lenData<2:
            return False
        else:
            for x in range(lenData):
                if self.data.count(v-self.data[x])!=0:
                    return True
                else:
                    return False

if __name__ == "__main__":
    print ('main')
s = Solution()
s.add(1)
s.add(2)
s.add(4)
for i in (1,3,4,5,6,7,8):
    s.add(i)
for i in (23,1,3,5,67):
    print(i, s.hasValue(i))
