class Node:
    def __init__(self, valeur, gauche=None, droit=None):  # Initialisation du noeud avec une valeur et des enfants gauche et droit optionnels
        self.valeur = valeur  # Assignation de la valeur du noeud
        self.gauche = gauche  # Assignation de l'enfant gauche
        self.droit = droit  # Assignation de l'enfant droit
        
    def affichage(self):
        if self.gauche:  # Si l'enfant gauche existe
            self.gauche.affichage()  # Affichage de l'enfant gauche
        print(self.valeur, end=" ")  # Affichage de la valeur du noeud
        if self.droit:  # Si l'enfant droit existe
            self.droit.affichage()  # Affichage de l'enfant droit
            
    def insert(self, ins):
        current = self.valeur  # Récupération de la valeur actuelle du noeud
        if current is not None:  # Si la valeur actuelle n'est pas None
            if ins < current:  # Si la valeur à insérer est inférieure à la valeur actuelle
                if self.gauche is None:  # Si l'enfant gauche n'existe pas
                    self.gauche = Node(ins)  # Création d'un nouveau noeud à gauche
                else:
                    self.gauche.insert(ins)  # Insertion récursive à gauche
            elif ins > current:  # Si la valeur à insérer est supérieure à la valeur actuelle
                if self.droit is None:  # Si l'enfant droit n'existe pas
                    self.droit = Node(ins)  # Création d'un nouveau noeud à droite
                else:
                    self.droit.insert(ins)  # Insertion récursive à droite
            if current == ins:  # Si la valeur à insérer est égale à la valeur actuelle
                print("La valeur existe déjà dans l'arbre")  # Message indiquant que la valeur existe déjà
        else:
            self.valeur = ins  # Assignation de la valeur au noeud
            
    def find(self, val):
        if val < self.valeur:  # Si la valeur recherchée est inférieure à la valeur du noeud
            if self.gauche is None:  # Si l'enfant gauche n'existe pas
                return f"{val} n'est pas dans l'arbre"  # Retourne que la valeur n'est pas dans l'arbre
            return self.gauche.find(val)  # Recherche récursive à gauche
        elif val > self.valeur:  # Si la valeur recherchée est supérieure à la valeur du noeud
            if self.droit is None:  # Si l'enfant droit n'existe pas
                return f"{val} n'est pas dans l'arbre"  # Retourne que la valeur n'est pas dans l'arbre
            return self.droit.find(val)  # Recherche récursive à droite
        else:
            return "La valeur est dans l'arbre"  # Retourne que la valeur est dans l'arbre
        
    def height(self):
        if self.gauche is None and self.droit is None:  # Si le noeud n'a pas d'enfants
            return 1  # Retourne 1 (hauteur d'un noeud sans enfants)
        elif self.gauche is None:  # Si le noeud n'a pas d'enfant gauche
            return 1 + self.droit.height()  # Retourne 1 + hauteur de l'enfant droit
        elif self.droit is None:  # Si le noeud n'a pas d'enfant droit
            return 1 + self.gauche.height()  # Retourne 1 + hauteur de l'enfant gauche
        else:
            return 1 + max(self.gauche.height(), self.droit.height())  # Retourne 1 + la hauteur maximale entre les enfants gauche et droit
        
    def countNode(self):
        if self.gauche is None and self.droit is None:  # Si le noeud n'a pas d'enfants
            return 1  # Retourne 1 (un seul noeud)
        elif self.gauche is None:  # Si le noeud n'a pas d'enfant gauche
            return 1 + self.droit.countNode()  # Retourne 1 + nombre de noeuds de l'enfant droit
        elif self.droit is None:  # Si le noeud n'a pas d'enfant droit
            return 1 + self.gauche.countNode()  # Retourne 1 + nombre de noeuds de l'enfant gauche
        else:
            return 1 + self.gauche.countNode() + self.droit.countNode()  # Retourne 1 + nombre de noeuds des enfants gauche et droit
 

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
    print("Hauteur de l'arbre 1 \t ->", end=" ")
    print(arbre1.height())
    
    print("\n")
    print("Nombre de noeuds dans l'arbre 1 \t ->", end=" ")
    print(arbre1.countNode())
    
main()
