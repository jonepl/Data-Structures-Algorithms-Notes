from collections import deque

class Stack :

    def __init__(self) :
        self.stack = deque()

    def empty(self):
        return True if len(self.stack) == 0 else False 

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        return self.stack.append(value)

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
