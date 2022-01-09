class Node(object):
    def __init__(self,data):
        self.head = None
        self.data = data
    

class LinkedIn:
    def __init__(self):
        self.head = None
        self.next = None
    
    def findOccurance(self,node):
        counter = 0;
        temp = self.head
        while (temp):
            if(temp.data ==  node):
                counter = counter + 1
            temp = temp.next
            
        return counter

    

if __name__ == '__main__':
    ls = LinkedIn()
    ls.head = Node(2)
    seconda = Node(2)
    third = Node(2)

    ls.head.next = seconda
    seconda.next = third
    third.next = None

    print(ls.findOccurance(4))
