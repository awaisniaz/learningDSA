class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None;
        self.next = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
          print(temp.data)
          temp = temp.next
    def nthNode(self,index):
       counter = 0
       temp = self.head
       while (temp):
           if(index == counter):
               return temp.data
           counter = counter + 1;
           temp = temp.next



if __name__ == '__main__':
  link = linkedList()
  link.head = Node(2)
  second = Node(10)
  third = Node(30)
  fourth = Node(3233)
  link.head.next = second
  second.next = third
  third.next = fourth
  fourth.next = None

#   link.printLinkedList()
  print(link.nthNode(0))


