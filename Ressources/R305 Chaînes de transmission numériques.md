
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


#############

# Chapitre 2 – Concepts fondamentaux pour les transmissions numériques

## I. Définition du débit binaire

On considère une liaison pour laquelle les bits sont codés comme suit :  
- « 1 » → +A volts  
- « 0 » → -A volts  

La cadence d’émission est régie par une horloge `He` de fréquence `fe`.  


- `TB` : Durée d'un bit [en bits/s]  
- `BT` : Bande passante du canal  

## II. Limitation du débit

### II.1 Transmission dans un canal parfait

Si le canal est parfait (bande passante infinie, absence de bruit), le signal reçu est identique à celui émis.

0100 1011 Émetteur → Récepteur 0100 1011 Canal parfait

### II.2 Transmission dans un canal à bande passante limitée

Dans un canal à bande passante limitée, celui-ci agit comme un filtre passe-bas, dégradant le signal. L'instant de décision doit être pris quand le signal est interprétable, dans la **plage de décision** `Td`, qui est inférieure à la durée d’un bit `TB`.

### II.3 Interférence inter-symbole

Quand un canal se comporte comme un passe-bas, les impulsions s’élargissent et se superposent, générant une **interférence inter-symbole** (IIS). Si la bande passante est réduite ou si le débit binaire augmente, cette interférence peut rendre les données ininterprétables.

### II.4 Analyse de l’interférence inter-symbole – Effet du bruit – Diagramme de l’œil

#### Signal non bruité
- Si le signal est au-dessus ou en dessous des seuils, il est interprétable.  
- Si le signal est dans la zone d'incertitude, il ne peut pas être interprété.

#### Signal légèrement bruité
- Avec du bruit, la plage de décision se réduit.

#### Signal fortement bruité
- Si le bruit devient trop important, les niveaux deviennent indiscernables, l'œil se ferme.


## III. Notions de rapidité de modulation : Critère de Nyquist

La bande passante du canal limite la rapidité de modulation `R` (en baud ou symboles par seconde). Selon Nyquist :

1. `R ≤ 2 × BP` (premier critère, difficile en milieu bruité)
2. `R ≤ BP` (deuxième critère, plus facile)
3. `R ≈ 1,25 × BP` (critère pratique)

### Exemple : Application à l’ADSL
- Bande passante d’une ligne téléphonique : 1,1 MHz  
- Utilisation pour la voix et les données.

## IV. Utilisation des codages multi-symboles

### IV.1 Qu’est-ce qu’un symbole ?

Le **débit des symboles** `M` est défini par :

M = 1/Ts

`Ts` : durée d’un symbole. La rapidité de modulation correspond au débit maximal des symboles dans une bande passante donnée, mais pas au débit binaire.

#### Exemple : Codage NRZ

- "1" : +A
- "0" : -A

Le signal présente 2 symboles (±A), chaque symbole codant 1 bit. La largeur de bande dépend uniquement du débit des symboles :

Lb = M

### IV.2 Utilisation d’un codage multi-symbole pour augmenter le débit binaire

Avec le codage **2B1Q** (4 symboles), chaque symbole code 2 bits, doublant ainsi le débit binaire pour une même largeur de bande.

### IV.3 Utilisation d’un codage multi-symbole pour diminuer la largeur de spectre

Pour un débit binaire constant, le codage 2B1Q divise par deux la largeur de bande par rapport au codage NRZ.

### IV.4 Valence d’un signal

La **valence** `v` correspond au nombre d’états significatifs (niveaux ou symboles) que peut prendre le signal :

v = 2 pour NRZ v = 4 pour 2B1Q

Le débit binaire `D` s’exprime par la formule suivante :
D = M × log2(v)


### IV.5 Conclusion

Pour un canal à bande passante limitée :
- On peut augmenter le débit binaire en augmentant la valence tout en maintenant constant le débit des symboles (et donc la largeur de bande).
- On peut diminuer la largeur de bande en augmentant la valence tout en gardant le débit binaire constant.

Toutefois, on ne peut pas augmenter indéfiniment la valence, car les niveaux deviennent difficilement discernables en présence de bruit.

## V. Transmission en milieu bruité

### V.1 Prise en compte du bruit

Le rapport signal/bruit (S/N) mesure la qualité d’un canal vis-à-vis du bruit :

[S/N]dB = 10 × log(PS/PN)

### V.2 Capacité d’un canal bruité, relation de Shannon

Shannon a établi que dans un canal bruité, le nombre maximal d’états discernables `vn` est donné par :

vn = 1 + PS/PN

D’où la **capacité** d’un canal (débit binaire maximal) :

C = BP × log2(1 + PS/PN)


---
**Fin du chapitre 2 – Concepts fondamentaux pour les transmissions numériques.**
