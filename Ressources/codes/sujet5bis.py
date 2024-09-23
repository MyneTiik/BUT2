class Node:
    def __init__(self,valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
    def affichage(self):
        if self.gauche:
            self.gauche.affichage()
        print(self.valeur, end=" ")
        if self.droit:
            self.droit.affichage()
            
    def insert(self, ins):
        current = self.valeur
        if current is not None:
            if ins < current:
                if self.gauche is None:
                    self.gauche = Node(ins)
                else:
                    self.gauche.insert(ins)
            elif ins > current:
                if self.droit is None:
                    self.droit = Node(ins)
                else:
                    self.droit.insert(ins)
            if current == ins:
                print("La valeur existe déjà dans l'arbre")
        else:
            self.valeur = ins
            
            
    def find(self, val):
        if val < self.valeur:
            if self.gauche is None:
                return f"{val} n'est pas dans l'arbre"
            return self.gauche.find(val)
        elif val > self.valeur:
            if self.droit is None:
                return f"{val} n'est pas dans l'arbre"
            return self.droit.find(val)
        else:
            return "La valeur est dans l'arbre"
        
    def height(self):
        if self.gauche is None and self.droit is None:
            return 1
        elif self.gauche is None:
            return 1 + self.droit.height()
        elif self.droit is None:
            return 1 + self.gauche.height()
        else:
            return 1 + max(self.gauche.height(), self.droit.height())
        
           
 

def main():    
    
    print("\n")
    print("Arbre 1")
    arbre1 = Node(10, 
                Node(5,
                    Node(2),
                    Node(8)),
                Node(12,
                    Node(11),
                    Node(15)))
    print(
        """
                10
               /  \\
              5    12
             / \   / \\
            2   8 11  15
        """
    )

    print("\n")
    print("Affichage de l'arbre 1")
    arbre1.affichage()
    
    print("\n")
    print("Insertion de 7 dans l'arbre 1")
    arbre1.insert(7)
    
    print("On devrait obtenir:")
    print(
        """
                10
               /  \\
              5    12
             / \   / \\
            2   8 11  15
               /
              7
        """
    )
    
    print("Vérification de l'insertion de 7 dans l'arbre 1")
    arbre1.affichage()
    
    print("\n")
    print("Insertion de 15 dans l'arbre 1")
    arbre1.insert(15)
    
    print("\n")
    print("Insertion de 1 dans l'arbre 1")
    arbre1.insert(1)
    
    print("On devrait obtenir:")
    print(
        """
                10
               /  \\
              5    12
             / \   / \\
            2   8 11  15
           /   /
          1   7
        """
    )
    print("Vérification de l'insertion de 1 dans l'arbre 1")
    arbre1.affichage()
    
    print("\n")
    print("Isertion de 20 dans l'arbre 1")
    arbre1.insert(20)
    
    print("On devrait obtenir:")
    print(
        """
                10
               /  \\
              5    12
             / \   / \\
            2   8 11  15
           /   /       \\
          1   7         20
        """
    )
    
    print("Vérification de l'insertion de 20 dans l'arbre 1")
    arbre1.affichage()
    
    print("\n")
    print("Recherche de 8 dans l'arbre 1 \t ->", end=" ")
    print(arbre1.find(8))
    
    print("\n")
    print("Recherche de 20 dans l'arbre 1 \t ->", end=" ")
    print(arbre1.find(20))
    
    print("\n")
    print("Recherche de 100 dans l'arbre 1 \t ->", end=" ")
    print(arbre1.find(100))
    
    print("\n")
    print("Hauteur de l'arbre 1")
    print(arbre1.height())
    
    
main()