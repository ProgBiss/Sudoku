'''
Module qui contient les fonctions qui placent chaque ligne, colonne et carrée (9x9) pour ensuite les vérifiés et détermier s'il y a une victoire.

'''
def VerifierCases(cases): # Vérifie chaque ligne, colonne et carrée (9x9) pour qu'il n'y ait pas 2 (ou plus) chiffres identiques.
    int_nombre = 0
    for i in range(0,len(cases),9):
        for chiffres in range(1,10):
            if cases[i:i+9].count(str(chiffres)) == 1:
                int_nombre += 1
                
    if int_nombre == 81:
        return True
    else:
        return False

def VerifierGrille(cases):
                
    casesHorizontal = []       # Place les lignes pour la vérification  
    for i in range(9):
        for j in range(9):
            if cases[i*9+j][1] != " " and cases[i*9+j][1] != "-":
                if int(cases[i*9+j][1]) > 10:
                    casesHorizontal.append(str(int(cases[i*9+j][1])-10))
                else:
                    casesHorizontal.append(cases[i*9+j][1])  
            else:
                casesHorizontal.append(cases[i*9+j][1])  
                  
    casesVertical = []         # Place les colonnes pour la vérification
    for i in range(9):
        for j in range(9):
            if cases[i+9*j][1] != " " and cases[i+9*j][1] != "-":
                if int(cases[i+9*j][1]) > 10:
                    casesVertical.append(str(int(cases[i+9*j][1])-10))
                else:
                    casesVertical.append(cases[i+9*j][1])
            else:
                casesVertical.append(cases[i+9*j][1])  
            
    casesCarree = []          # Place les carrées (9x9) pour la vérification
    debutCarree = (0,3,6,27,30,33,54,57,60)
    for i in range(9):
        for j in range(9):
            if debutCarree.count(i*9+j) == 1:
                for k in range(3):
                    for l in range(3):
                        if cases[(i+k)*9+j+l][1] != " " and cases[(i+k)*9+j+l][1] != "-":
                            if int(cases[(i+k)*9+j+l][1]) > 10:
                                casesCarree.append(str(int(cases[(i+k)*9+j+l][1])-10))
                            else:
                                casesCarree.append(cases[(i+k)*9+j+l][1])  
                        else:
                            casesCarree.append(cases[(i+k)*9+j+l][1])  

    if VerifierCases(casesHorizontal) == True and VerifierCases(casesVertical) == True and VerifierCases(casesCarree) == True:
        return True  # Si les 3 vérifications n'ont pas trouver 2 chiffres (ou plus), le joueur gagne.
    else:
        return False # Sinon il retourne à la grille pour trouver son(ses) erreur(s).