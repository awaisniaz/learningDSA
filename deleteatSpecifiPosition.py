class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.data = None
        self.next = None
    def printLinkList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def DeleteNode(self,key):
          temp = self.head
          prev = None
          while(temp):
              if(temp.data == key):
                  prev.next  = temp.next
                  break
              else:
                  print("Key is Not Present")
              prev = temp
              temp = temp.next





if __name__ == '__main__':
    link = LinkedList()
    link.head = Node(4)
    second = Node(5)
    third = Node(6)
    fourth = Node(9)
    link.head.next = second
    second.next = third
    third.next = fourth
    link.DeleteNode(7)
    link.printLinkList()

