class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedListNode:
    def __init__(self):
        self.data = None
        self.next = None
    # def printList(self):
    #     temp = self.head
    #     counter = 0
    #     while(temp):
    #         counter = counter + 1
    #         temp = temp.next
    #     return counter
    def searchElement(self,key):
        self.found = False
        temp = self.head
        while(temp):
            if(temp.data == key):
                self.found = True
            temp = temp.next
        return self.found
if __name__ == '__main__':
    link = LinkedListNode()
    link.head = Node(10)
    second = Node(22)
    third = Node(23)
    fourth = Node(32)
    Fifth = Node(21)
    sixth = Node(3332)

    link.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = Fifth
    Fifth.next = sixth

    # print(link.printList())
    print(link.searchElement(3332))