class Etudiant:
    
    def __init__(self, nom, prenom) :
        self.nom = nom
        self.prenom = prenom
        self.note = []
        
    def ajouterNote(self, note, coef):
        self.note.append((note, coef))
        
    def nbNotes(self):
        print(f'Nombre de notes de {self.nom} {self.prenom} -> {len(self.note)}')
        return len(self.note)
    
    def afficher(self):
        print("Nom : ", self.nom)    
        print("Prenom : ", self.prenom)    
        print("Note : ", self.note)
        print("\n")    

    def moyenne(self):
        sum_notes = 0
        coef_tot = 0
        for elt in self.note:
            coef_tot += elt[1]
            sum_notes += (elt[0]*elt[1])
        print(f'Moyenne des notes de {self.nom} {self.prenom} -> {sum_notes/coef_tot}')        
        return (sum_notes/coef_tot)

    
##########

class Promotion(Etudiant):
    
    def __init__(self):  
        
        self.etudiants = []
        
    def ajouterEtudiants(self, etud):
        self.etudiants.append(etud)
        
    def nbEtudiants(self):
        print(f'{len(self.etudiants)} étudiants dans la promo.')
       
    def promo_moyenne(self):
        moy = 0
        nb_etud = len(self.etudiants)
        for etud in self.etudiants:
            moy += Etudiant.moyenne(etud)
        print(f'Moyenne de la promo -> {moy/nb_etud}')    
        
    def afficher(self):
        for etud in self.etudiants:
            print("Nom : ", etud.nom, "Prenom : ", etud.prenom, "Note : ", etud.note)


def main():
    
    etudiant1 = Etudiant("parnaudeau", "alexandre")
    etudiant2 = Etudiant("claudel","noah")
    #etudiant1.afficher()
    
    etudiant1.ajouterNote(18, 1)
    etudiant1.ajouterNote(16, 3)
    etudiant1.ajouterNote(11, 2)
    
    etudiant2.ajouterNote(15, 1)
    etudiant2.ajouterNote(11, 2)
    
    etudiant1.afficher()
    etudiant2.afficher()
    
    etudiant1.nbNotes()
    etudiant2.nbNotes()
    
    etudiant1.moyenne()
    etudiant2.moyenne()
    
    
    ######### TEST PROMOTION
    
    BUT2 = Promotion()

    BUT2.ajouterEtudiants(etudiant1)
    BUT2.ajouterEtudiants(etudiant2)
    
    BUT2.nbEtudiants()
    
    BUT2.promo_moyenne()
    
    BUT2.afficher()
    
    
main()
