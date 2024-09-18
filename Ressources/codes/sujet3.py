# Attention les cas de fin/début et vide sont des cas a traiter

class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
    def printNode(self): #récursif, permet d'afficher chaque elmt de la liste chainée
        print(self.data, end= " ")
        if self.next is not None:
            self.next.printNode() #appel recursif sur le prochain terme
    
    def printNodeRecRev(self): # comment ça marche ? on parcours toute la liste chainee puis on resoud/affiche chaque terme, on a donc parcouru la liste a l'envers
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

    def printListRec(self):
        if self.head is not None:
            self.head.printNode() #appel de la fonction de la classe Node
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
