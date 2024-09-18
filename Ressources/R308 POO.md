
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

```python
class Véhicule:     
	def __init__(self, marque):         
		self.marque = marque  class Moto(Véhicule):     
		
	def rouler(self):         
		print(f"La moto {self.marque} roule.")`
```


---

### **Avantages de la POO en Python**

- Code plus propre et organisé
- Facilité de maintenance et d'évolution
- Gestion intuitive des objets du monde réel

---

### **Conclusion**

- **Résumé des concepts** : Classes, objets, héritage, polymorphisme, encapsulation, abstraction.
- **Bénéfices à long terme** : La POO favorise la réutilisation du code, la modularité et la scalabilité dans les grands projets logiciels.