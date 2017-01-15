'''
Module qui contient les fonctions permettant de sauvegarder une partie dans un fichier et charger cette même partie.

'''
import os
import time
from random import randint

def SauvegarderPartie(int_partie, cases, chronometre, str_difficulte): # Sauvegarde la partie dans un fichier
    j = 0
    
    ligne = []
    
    for i in range(9):
        ligne.append("")
        
    for i in range(len(ligne)):  # Séparer les cases
        for j in range(9):
            ligne[i] += cases[9*i+j][1]
            if cases[9*i+j][1] != " ":
                if int(cases[9*i+j][1]) < 10:
                    ligne[i] += ","
            else:
                ligne[i] += ","
                   
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Sauvegarde'+str(int_partie), 'w', encoding = "UTF8")  # Chemin pour sauvegarder dans le 
    #fichier = open('.\\Fichiers\\Sauvegarde'+str(partie), 'w', encoding = "UTF8")                                                 fichier du workspace
    
    if chronometre[2] >=0 and chronometre[2] <= 9: # Transformer le chronomètre en string
        str_secondes = "0" + str(chronometre[2])
    else:
        str_secondes = str(chronometre[2])
    
    if chronometre[1] >=0 and chronometre[1] <= 9:
        str_minutes = "0" + str(chronometre[1])
    else:
        str_minutes = str(chronometre[1])
        
    if chronometre[0] >=0 and chronometre[0] <= 9:
        str_heures = "0" + str(chronometre[0])
    else:
        str_heures = str(chronometre[0])
        
    fichier.write(str_difficulte+"\n")     # Sauvegarder la difficulté, le chronomètre et la grille
    fichier.write(str_heures+str_minutes+str_secondes+"\n")
    for i in range(len(ligne)):
        fichier.write(ligne[i]+"\n")
    fichier.close()
    
def ChargerPartie(int_partie): # Charge la partie à partir de la sauvegarde choisie
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Sauvegarde'+str(int_partie), 'r', encoding = "UTF8")
    i = 0
    casesTemp = []
    chronometre = [0,0,0]

    for ligne in fichier: # Charge les données (difficulté, chronomètre et grille)
        if i == 0:
            str_difficulte = ligne[:-1]
        elif i == 1:
            chronometreTemp = list(ligne[:-1])
        else:
            if ligne[-1:] == "\n":
                casesTemp.append(ligne[:-1])
            else:
                casesTemp.append(ligne)
        i += 1     
    fichier.close()
    lignes = i   
    if lignes > 0: 
        for i in range(3):  # Trouver l'heure de début
            chronometre[i] = int(chronometreTemp[i*2])*10 + int(chronometreTemp[(i*2)+1])
            
        heureActuel = time.localtime()[3:6]
        heureDebutListe = [heureActuel[0]-chronometre[0], heureActuel[1]-chronometre[1], heureActuel[2]-chronometre[2]]
        
        if heureDebutListe[2] < 0:  # Ajuster l'heure de début
            if heureDebutListe[1] > 0:
                heureDebutListe[2] += 60
                heureDebutListe[1] -= 1
            else:
                heureDebutListe[0] -= 1
                heureDebutListe[1] += 59
                heureDebutListe[2] += 60
        
        if heureDebutListe[1] < 0:
            heureDebutListe[1] += 60
            heureDebutListe[0] -= 1
                
        if heureDebutListe[0] < 0:
            heureDebutListe[0] += 24
            
        heureDebut = tuple(heureDebutListe)
        
        cases = []
           
        for i in range(81):  # Initialise "cases"
            cases.append([" "," "," "])
        
        for i in range(len(casesTemp)):  # Mets les cases dans le bon format
            for j in range(len(casesTemp[i])//2):
                if casesTemp[i][j*2+1] == ",":
                    cases[i*9+j][1] = casesTemp[i][j*2]
                else:
                    cases[i*9+j][1] = str(int(casesTemp[i][j*2+1])+10)
        return (str_difficulte, heureDebut, cases)
    else:
        return False
    
def CreerPartie(int_selection): # Génère une des 3 grilles préconconçus pour chaque niveau de difficulté, selon celle choisie
    if int_selection == 0:
        str_difficulte = "Debutant"
    elif int_selection == 1:
        str_difficulte = "Intermediaire"
    elif int_selection == 2:
        str_difficulte = "Difficile"
    else:
        str_difficulte = "Expert"
        
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Partie'+str_difficulte, 'r', encoding = "UTF8")
    
    casesTemp = []
    i = 0
    
    int_grille = randint(0,2)
    for ligne in fichier: # Mets les chiffres dans la grille
        if i >= int_grille * 10 and i <= int_grille * 10 + 8:          
            if ligne[-1:] == "\n":
                casesTemp.append(ligne[:-1])
            else:
                casesTemp.append(ligne)
        i += 1
            
    cases = []
       
    for i in range(81):  # Initialise "cases"
        cases.append([" "," "," "])
                
    for i in range(len(casesTemp)):  # Affiche correctement les chiffres dans la grille
        for j in range(len(casesTemp[i])):
            if int(casesTemp[i][j]) != 0:
                cases[i*9+j][1] = str(int(casesTemp[i][j])+10)
    return cases