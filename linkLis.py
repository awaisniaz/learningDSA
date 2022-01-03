class Node(object):
    def __init__(self,data):
      self.data = data
      self.next = None
class LinkedList:

    def __init__(self):
        self.head = None
        self.next = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def pushNode(self,newNode):
        new_node = Node(newNode)
        new_node.next = self.head
        self.head = new_node

    def afterGiverNode(self,prevNode,nextNode,newNode):
        newNode = Node(newNode)
        prevNode.next = newNode
        newNode.next = nextNode
    def insetNodeatEnd(self,lastNode,nextNode):
        nextNode = Node(nextNode)
        lastNode.next = nextNode
        nextNode.next = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    three = Node(3)

    llist.head.next = second
    second.next = three
    three.next = None
    llist.pushNode(4)
    llist.printList()
    llist.afterGiverNode(second,three,7)
    llist.printList()




