# Attention les cas de fin/début et vide sont des cas a traiter

class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
    def printNode(self):
        print(self.data, end= " ")
        if self.next is not None:
            self.next.printNode()

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
     
    def addInTail(self, val):
        newtail = Node(val)
        if self.head is None:
            self.head = newtail
            self.head.next = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newtail
            newtail.next = None
        
    def reverseList(self):        
        myLinkedList2 = LinkedList()
        current = self.head
        
        while current is not None:
            myLinkedList2.addInHead(current.data)
            current = current.next
        
        return myLinkedList2
    
    def addSorted(self, val):
        newnode = Node(val)
        if self.head is None:
            self.addInHead(val)
        else:
            current = self.head #premier elmt de la liste
            while current.next is not None and current.next.data < val: #condition 1 : on ne depasse pas la fin de la liste et condition 2 : la valeur de l'element suivant est inferieur a la valeur a ajouter
                current = current.next #on avance dans la liste
            newnode.next = current.next #dans la liste [10[20[30[40]]] si on veut ajouter 25, on doit inserer 25 entre 20 et 30, donc 25 doit pointer vers 30
            current.next = newnode #20 doit pointer vers 25
            
    def remove(self, val):
        if self.head is not None:
            if self.head.data == val:
                self.head = self.head.next
            else:
                current = self.head
                while current.next is not None and current.next.data != val:
                    current = current.next
                if current.next is not None:
                    current.next = current.next.next
                else:
                    print("Element non trouvé")
        else:
            print("liste vide")
            
    def merge(self, liste2):
        liste_finale = LinkedList()
        if self.head is None:
            liste_finale = liste2
        else:
            current1 = self.head
            current2 = liste2.head
            while current1 is not None and current2 is not None:
                if current1.data < current2.data:
                    liste_finale.addInTail(current1.data)
                    current1 = current1.next
                else:
                    liste_finale.addInTail(current2.data)
                    current2 = current2.next
            if current1 is not None:
                while current1 is not None:
                    liste_finale.addInTail(current1.data)
                    current1 = current1.next
            if current2 is not None:
                while current2 is not None:
                    liste_finale.addInTail(current2.data)
                    current2 = current2.next
        return liste_finale
    
    def heads(self, N):
        current = self.head
        for i in range(0, N):
            if current is not None:
                print(current.data, end= " ")
                current = current.next
    
    def tails(self, N):
        current = self.head
        longueur = 0
        while current is not None:
            longueur += 1
            current = current.next
        if N > longueur:
            N = longueur
        current = self.head
        for i in range(longueur - N):
            current = current.next
        
        while current is not None:
            print(current.data, end= " ")
            current = current.next
        
        
   



   
def main():      
    #myNode = Node(10) 
    #print("The data in the node is:", myNode.data) 
    #print("The next attribute in the node is:", myNode.next)
    
    #Liste 1
    myLinkedList= LinkedList()
    myNode1 = Node(10)    
    myNode2 = Node(20)    
    myNode3 = Node(30)
    myNode4 = Node(40)
    myLinkedList.head = myNode1
    myNode1.next = myNode2
    myNode2.next = myNode3
    myNode3.next = myNode4
    
    #Liste 2
    myLinkedList2= LinkedList()
    myNode5 = Node(15)
    myNode6 = Node(35)
    myNode7 = Node(45)
    myLinkedList2.head = myNode5
    myNode5.next = myNode6
    myNode6.next = myNode7  


    print("Les éléments de la liste sont:")
    myLinkedList.printListRec()
    
    print("\n")
    print("La longueur de la liste est:")
    myLinkedList.printListCount()
    
    print("\n")
    print("Mélanger les listes ordonnées 1 et 2:")
    myLinkedList.merge(myLinkedList2).printListRec()
    
    print("\n")
    print("Retirer un élément inexistant (60) de la liste:")
    myLinkedList.remove(60)
    
    print("\n")
    print("Retirer un élément existant (30) de la liste:")
    myLinkedList.remove(30)
    myLinkedList.printListRec()
    
    print("\n")
    print("Ajout d'une valeur (25) dans une liste triée:")
    myLinkedList.addSorted(25)
    myLinkedList.printListRec() 
    
    print("\n")
    print("Ajout d'un élément en tête:")    
    myLinkedList.addInHead(333)
    myLinkedList.printListRec()
    
    print("\n")
    print("Ajout d'un élément en fin:")
    myLinkedList.addInTail(555)
    myLinkedList.printListRec()
    
    print("\n")
    print("Inversion de la liste:")    
    reverselist = myLinkedList.reverseList()
    reverselist.printListRec()
    
    print("\n")
    print("Les N heads éléments de la liste sont:")
    myLinkedList.heads(2)
    
    print("\n")
    print("Les N tails éléments de la liste sont:")
    myLinkedList.tails(2)
    
    
main()
