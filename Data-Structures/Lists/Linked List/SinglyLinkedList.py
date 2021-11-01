

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class SLinkedList:

    def __init__(self) :
        self.head = None

    def empty(self):
        return True if (self.head  == None) else False

    def size(self):

        if(self.head == None) : return 0

        count = 0
        temp = self.head

        while(temp) :
            count += 1
            temp = temp.next

        return count

    def get(self, index) :

        if(index < 0) : return -1

        if(self.empty()) : return -1

        count = 0
        temp = self.head

        while(count != index) :
            if(temp.next == None) :
                return -1
            count += 1
            temp = temp.next

        return temp.data

    def indexOf(self, value) :
        if(self.empty()) : return -1

        count = 0
        temp = self.head

        while(temp) :
            if(temp.data == value) :
                return count 

            count += 1
            temp = temp.next

        return -1

    def erase(self, value) :
        
        if(self.empty()) : return

        temp = self.head

        if(temp.data == value) :
            self.head = temp.next
            temp = None     # Set equal to None for the garbage collector

        while(temp.next) :
            if(temp.next.data == value) :
                temp.next = temp.next.next
                break
            temp = temp.next

        return

    def insert(self, index, value):

        # insert Node if it is at the beginning
        if(index == 0) :
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            return

        count = 0
        temp = self.head

        # iterate until right before index
        while(temp != None and count != index) :

            if(count == index-1) :
                tp = temp.next
                temp.next = Node(value)
                temp.next.next = tp
                return

            temp = temp.next
            count += 1

        return

    def append(self, value) :
        
        if(self.empty()) :
            print("Empty")
            self.head = Node(value)

        temp = self.head
        while(temp != None) :
            
            if(temp.next == None) :
                temp.next = Node(value)
                return
            
            temp = temp.next

    def output(self) :

        temp = self.head
        while(temp) :
            print(str(temp.data) + " ")
            temp = temp.next

# Code execution starts here
if __name__=='__main__':

    # Start with the empty list
    sList = SLinkedList()
    print(sList.empty())
    print(sList.size())
    print(sList.get(0))
    print("~~~~~~~~~~~~~~~~~~~~~")

    sList.head = Node(1)
    second = Node(2)
    third = Node(3)

    sList.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node

    sList.output()
    print("--------- 1 ---------")
    sList.erase(4)
    sList.output()
    print("--------- 2 ---------")
    sList.insert(4, 6)
    sList.output()
    print("--------- 3 ---------")
    sList.append(20)
    sList.output()

