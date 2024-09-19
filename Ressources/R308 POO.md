
*paradigme fonctionnel : [Sujet 1 de TP/TD](Ressources/sujet1.py)
#### **PDF de Cours**
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


```python
class Point: #Définition d'un point
	def __init__(self,a,b): 
		self.x = a 
		self.y = b 
		
	def deplacer(self, dx, dy): 
		self.x = self.x+dx 
		self.y = self.y+dy
```

- **Explication** :
    - `__init__` est le constructeur qui initialise l'objet.
    - `self` représente l'instance courante de l'objet.
    - `deplacer` est une méthode qui simule le déplacement du point.

[Sujet 2 de TP/TD](codes/sujet2.py)

---

### **L’Héritage en POO**

- **Définition** : L'héritage permet de créer de nouvelles classes basées sur des classes existantes.
- **Avantages** : Réutilisation et extension des fonctionnalités existantes.

### Exemple d'Héritage :

```python
class Personne(): # Constructeur 
	def __init__(self, nom, prenom): 
		self.nom = nom 
		self.prenom = prenom 
		
	def afficher(self): 
		print("Nom : ",self.nom) 
		print("Prénom : ",self.prenom) 
		
class Employe(Personne): # Constructeur 
	
	def __init__(self, nom, prenom, job): # appel du constructeur de la classe mère (Personne) 
		Personne.__init__(self, nom, prenom) # ajout d'un attribut 
	
	self.job = job 
	
	def afficher(self): 
		Personne.afficher(self) print("Job : ",self.job)
```

*Ici on cherche a utiliser les fonction de la classe `Personne()` dans la classe `Employe()`, on ajoute dans le `__init__` de la classe  `Employe()` qui s'additionne au  `__init__` de `Personne()` pour ajouter un nouvel attribut.*

[Sujet 3 de TP/TD](codes/sujet3.py)
[Sujet 3Bis de TP/TD](codes/sujet3bis.py)

---
### **Le Polymorphisme**

Le **polymorphisme** permet d'utiliser des méthodes de même nom sur des objets de différentes classes, chaque classe pouvant avoir sa propre implémentation de la méthode.

### Exemple de Polymorphisme :


```python
class Animal:     
	def parler(self):         
		pass  
		
class Chien(Animal):     
	def parler(self):         
		print("Le chien aboie.")  
		
class Chat(Animal):     
	def parler(self):         
		print("Le chat miaule.")  
		
def faire_parler(animal_var):     
	animal_var.parler()  
	
faire_parler(Chien())  # Le chien aboie 
faire_parler(Chat())   # Le chat miaule
```

*Ici on ré-utilise la classe `Animal()` avec l'héritage comme vu précédemment.  En utilisant la fonction `faire_parler` on appelle la classe `Chat()` ou `Chien()` qui eux même appellent la classe `Animal()`*

[Sujet 5 de TP/TD](codes/sujet5.py)

---
### **Avantages de la POO en Python**

- Code plus propre et organisé
- Facilité de maintenance et d'évolution
- Gestion intuitive des objets du monde réel

---

### **Conclusion**

- **Résumé des concepts** : Classes, objets, héritage, polymorphisme, encapsulation, abstraction.
- **Bénéfices à long terme** : La POO favorise la réutilisation du code, la modularité et la scalabilité dans les grands projets logiciels.