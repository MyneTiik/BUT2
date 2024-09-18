def creeetud(nom, prenom):
    etud = {}
    etud['nom'] = nom
    etud['prenom'] = prenom
    etud['notes'] = []
    
    return etud

def ajouter_note(etudiant, note, coef):
    etudiant['notes'].append((note,coef))
    
def nb_notes(etudiant):
    return len(etudiant['notes'])    
    
def moyenne(etudiant):
    sum_notes = 0
    coef_tot = 0
    for elt in etudiant['notes']:
        coef_tot += elt[1]
        sum_notes += (elt[0]*elt[1])
    return sum_notes/coef_tot
     
##################################################  
        
def creepromo():
    promo = {}
    promo['etudiant'] = []
    
    return promo

def ajout_promo(promo, etudiant):
    promo['etudiant'].append(etudiant)
     
def taille_promo(promo):
    return len(promo['etudiant'])

def moyenne_promo(promo):
    notes_moy = 0
    nb_etud = taille_promo(promo)
    for elt in promo['etudiant']:
        notes_moy += moyenne(elt)
    return notes_moy/nb_etud
   
def main():
    
    etud1 = creeetud('alexandre', 'parnaudeau')
    ajoutnote = ajouter_note(etud1, 10, 2)
    ajoutnote = ajouter_note(etud1, 20, 1)

    etud2 = creeetud('noah', 'claudel')
    ajoutnote = ajouter_note(etud2, 14, 2)
    ajoutnote = ajouter_note(etud2, 1, 1)

    print(etud1)
    print(etud2)
    
    #print(nb_notes(etud1))
    #print(moyenne(etud1))
    
    #####
    
    promoA = creepromo()
    ajout_promo(promoA, etud1)
    ajout_promo(promoA, etud2)

    print(promoA)
    
    print(taille_promo(promoA))
    
    print(moyenne_promo(promoA))
    
main()