
cours :

- [R308-MM-2024](pdf/R308-MM-2024.pdf)

### **Introduction à la POO**

- **Définition** : La programmation orientée objet est un paradigme qui organise le code en objets plutôt qu’en fonctions.
- **Pourquoi l’utiliser** :
    - Réutilisation du code
    - Facilite la maintenance
    - Approche plus intuitive pour modéliser des systèmes complexes
- **Langages supportant la POO** : Java, C++, Python, etc.

---

### **Les Concepts de Base de la POO**

- **Classes** : Modèles définissant les objets.
- **Objets** : Instances de classes.
- **Attributs** : Propriétés des objets (variables).
- **Méthodes** : Comportements des objets (fonctions).

---

### **Exemple de Classe en Python**

python

Copier le code

`class Voiture:     def __init__(self, marque, modèle):         self.marque = marque         self.modèle = modèle      def démarrer(self):         print(f"La {self.marque} {self.modèle} démarre.")`

- **Explication** :
    - `__init__` est le constructeur qui initialise l'objet.
    - `self` représente l'instance courante de l'objet.
    - `démarrer` est une méthode qui simule le démarrage de la voiture.

---

### **L’Héritage en POO**

- **Définition** : L'héritage permet de créer de nouvelles classes basées sur des classes existantes.
- **Avantages** : Réutilisation et extension des fonctionnalités existantes.

#### Exemple :

python

Copier le code

`class Véhicule:     def __init__(self, marque):         self.marque = marque  class Moto(Véhicule):     def rouler(self):         print(f"La moto {self.marque} roule.")`

---

### **Le Polymorphisme**

- **Définition** : Capacité à traiter des objets de différentes classes via une interface commune.
- **Exemple** :

python

Copier le code

`class Animal:     def parler(self):         pass  class Chien(Animal):     def parler(self):         print("Le chien aboie.")  class Chat(Animal):     def parler(self):         print("Le chat miaule.")  def faire_parler(animal):     animal.parler()  faire_parler(Chien())  # Le chien aboie faire_parler(Chat())   # Le chat miaule`

---

### **L’Encapsulation**

- **Définition** : Cacher les détails internes d'un objet et fournir une interface pour interagir avec lui.
- **Avantages** : Protéger les données, améliorer la modularité.

#### Exemple :

python

Copier le code

`class CompteBancaire:     def __init__(self, solde):         self.__solde = solde  # Variable privée      def afficher_solde(self):         print(f"Solde: {self.__solde}€")  compte = CompteBancaire(1000) compte.afficher_solde()`

---

### Diapositive 8 : **L'Abstraction**

- **Définition** : Processus de simplification d'un système en cachant les détails complexes et en exposant uniquement l'essentiel.
- **Utilisation** : Utilisation de classes abstraites pour définir des interfaces.

---

### Diapositive 9 : **Avantages de la POO en Python**

- Code plus propre et organisé
- Facilité de maintenance et d'évolution
- Gestion intuitive des objets du monde réel

---

### Diapositive 10 : **Conclusion**

- **Résumé des concepts** : Classes, objets, héritage, polymorphisme, encapsulation, abstraction.
- **Bénéfices à long terme** : La POO favorise la réutilisation du code, la modularité et la scalabilité dans les grands projets logiciels.