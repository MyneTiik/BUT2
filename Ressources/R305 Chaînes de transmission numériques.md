
Cours :

- [Chapitre 1 - Notions sur les télécommunications](pdf/Chapitre%201%20-%20Notions%20sur%20les%20télécommunications.pdf)
- [Chapitre 2 - Concepts fondamentaux pour les transmissions numériques](pdf/Chapitre%202%20-%20Concepts%20fondamentaux%20pour%20les%20transmissions%20numériques.pdf)


# Module R305 : Chaînes de transmission numériques

## Chapitre 1 : Notions sur les télécommunications

### I. Problématiques en télécommunications

#### I.1. L’idée de départ
L'objectif est de permettre à au moins deux terminaux de communiquer afin que les utilisateurs puissent échanger ou consulter des informations.

Pour cela, il faut :
- **Des informations à échanger** : symboles, texte, images, son, vidéos, etc.
- **Un signal** pour véhiculer ces informations : signal électrique, radioélectrique ou optique.
- **Un support** pour transporter ces signaux : câbles en cuivre, fibres optiques, ou l'air.

Pour un échange d'informations fiable, il faut :
- Un **codage et un décodage** compréhensibles par les entités.
- Un **signal adapté** au support de transmission.
- Un **protocole d'échange** respecté.

Le module R305 se concentre sur le **signal adapté** et le **support de transmission**.

#### I.2. Organisation d’un système de communication
- **Équipements proches** : Moins de 100 m, connectés directement via Ethernet, USB, etc.
- **Équipements éloignés** : Plus de 100 m, nécessitent des équipements intermédiaires pour adapter le signal (ETCD).

#### I.3. Conclusion
Les performances des réseaux doivent constamment être améliorées, et cela dépend des **signaux** et des **caractéristiques des supports de transmission**.

---

### II. Chaîne de transmission numérique – Schéma synoptique

- **Source** : Entité émettant l'information.
- **Codage source** : Compression de l'information (JPEG, MP3).
- **Codage canal** : Protection des données contre les parasites (redondance).
- **Codage en ligne** : Transformation en signal physique pour transmission.
- **Canal** : Support physique (câbles, air, fibres optiques).
- **Bruit** : Parasites se superposant au signal.
- **Décodage** : Inverse des étapes de codage.
- **Destinataire** : Entité recevant l'information.

---

### III. Supports de transmission

#### III.1. Définition
Le support de transmission est le milieu physique où transite le signal :
- **Conducteurs** : Paires torsadées, coaxial (courant et tension).
- **Fibres optiques** : Véhicule des ondes lumineuses.
- **Espace libre** : Air ou vide, propice aux ondes électromagnétiques.

#### III.2. Sources de distorsions
Les distorsions peuvent provenir de :
- **Affaiblissement**
- **Interférences**
- **Bande passante limitée**

---

### IV. Notions de niveau de puissance

#### IV.1. Affaiblissement et gain
- **Gain** : Positif si la puissance en sortie est supérieure à l'entrée (Ps > Pe).
- **Affaiblissement** : Négatif si Ps < Pe.
- On utilise les échelles logarithmiques (dB) pour
