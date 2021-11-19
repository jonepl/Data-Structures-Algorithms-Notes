"""
The following representation can be written using deque from python's collection library
"""

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class Stack :

    def __init__(self) :
        self.stack = None

    def empty(self):
        return True if self.stack == None else False 

    def size(self):

        count = 0
        currNode = self.stack

        while(currNode != None) :
            count += 1
            currNode = currNode.next

        return count

    def top(self):
        return self.stack.data

    def pop(self):

        if(self.stack == None):
            raise Exception("Stack is empty")

        item = self.stack
        self.stack = self.stack.next

        return item.data

    def push(self, value):

        if(self.stack == None):
            self.stack = Node(value)
        else :
            tmp = self.stack
            self.stack = Node(value)
            self.stack.next = tmp

if __name__ == "__main__" :

    stack = Stack()
    print(stack.size())
    print(stack.empty())

    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.size())
    print(stack.empty())

    print(stack.top())
    print(stack.pop())
    print(stack.pop())

    print(stack.size())
    print(stack.empty())
