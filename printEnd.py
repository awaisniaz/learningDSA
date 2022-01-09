class Node(object):
    def __init__(self,data):
        self.data = data
        self.next  =  None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def reverseOrder(self,key):
        temp = self.head
        # counter = 0 
        # while(temp):
        #     counter = counter+1
        #     temp = temp.next
        # print(counter)
        index = 5
        while(temp):
            print(index)
            print(key)
            print(temp.data)
            if(key == index):
               return temp.data
            
            index = index-1
            temp = temp.next
    def printMiddleOfElement(self):
        fastPointer = self.head
        slowPointer = self.head

        while (fastPointer and fastPointer.next):
               slowPointer = slowPointer.next
               fastPointer = fastPointer.next.next  
        return slowPointer.data

if __name__ == '__main__':
    linked = LinkedList()
    linked.head = Node(10)
    second = Node(12)
    third = Node(2120)
    fourth = Node(2000)
    fifth = Node(223)
    sixth = Node(22122122121)

    linked.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = None
    # print(linked.reverseOrder(3))
    print(linked.printMiddleOfElement())
