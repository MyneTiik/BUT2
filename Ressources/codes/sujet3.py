# Attention les cas de fin/début et vide sont des cas a traiter

class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
    def printNode(self):
        print(self.data, end= " ")
        if self.next is not None:
            self.next.printNode()
            
    """ def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value """
    
    #def printNodeRecRev(self, liste=[]):
    #    if self.next is not None:
    #        liste.append(self.data)
    #        self.next.printNodeRecRev(liste)
    #    else:
    #        liste.append(self.data)
    #        print(liste.reverse())
    
    def printNodeRecRev(self):
        if self.next is not None:
            self.next.printNodeRecRev()
        return self.data
            
    def printNodeCount(self, cpt=1):
        if self.next is not None:
            cpt += 1
            self.next.printNodeCount(cpt)
        else:
            print('Longueur de la liste est de ',cpt)    
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    """ def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next """

    def printListRec(self):
        if self.head is not None:
            self.head.printNode()
        else:
            print("liste vide")
    
    def printListRecRev(self):
        if self.head is not None:
            self.head.printNodeRecRev()
        else:
            print("liste vide")
    
    def printListCount(self):
        if self.head is not None:
            self.head.printNodeCount()
        else:
            print("liste vide")
        
    def addInHead(self, val):
        newhead = Node(val)
        newhead.next = self.head
        self.head = newhead
        
        
    def reverseList(self):
        print("\n")
        
        myLinkedList2 = LinkedList()
        current = self.head
        
        while current is not None:
            myLinkedList2.addInHead(current.data)
            current = current.next
        
        return myLinkedList2
   



   
def main():      
    #myNode = Node(10) 
    #print("The data in the node is:", myNode.data) 
    #print("The next attribute in the node is:", myNode.next)
    
    myLinkedList= LinkedList()
    myNode1 = Node(10)    
    myNode2 = Node(20)    
    myNode3 = Node(30)
    myNode4 = Node(40)
    myLinkedList.head = myNode1
    myNode1.next = myNode2
    myNode2.next = myNode3
    myNode3.next = myNode4

    #myLinkedList.printListRecRev()
    #myLinkedList.printListCount()
    #print("The elements in the linked list are:") 
    myLinkedList.printListRec()

    #root = Node(10)

    #root.left = Node(20)
    #root.right = Node(30)
    #root.left.left = Node(40)
    #root.left.right = Node(50)
    
    myLinkedList.addInHead(333)
    #myLinkedList.printListRec()    
    
    reverselist = myLinkedList.reverseList()
    reverselist.printListRec()
    
main()