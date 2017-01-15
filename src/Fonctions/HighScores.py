'''
Module contenant les fonctions relatives aux scores (Menus, sauvegarder et charger).

'''

from Colorama.colorama import *
import os
from Fonctions.Grille import *

def AfficherMenuInscription(int_selection, nom):     # Fonction pour le menu qui demande le nom du joueur, et qui permet de se déplacer.    
    ligne = []
    char = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "<-", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "__", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "OK",)
    str_charNom = ""
    for i in range(len(nom)):
        str_charNom += nom[i]
        if i != 4:
            str_charNom += " "
            
    while len(str_charNom) < 9:
        if len(str_charNom)%2 == 1:
            str_charNom += " "
        else:
            str_charNom += "_"
    #selection 0 -> 35
    for i in range(3):  # Permet d'afficher le marqueur de position, les lettres/chiffres et de bien fermer le menu.
        for j in range(13):
            if i*13+j == int_selection:
                ligne.append("[")
            elif i*13+j == int_selection + 1:
                if j != 0:
                    ligne.append("]")
                else:
                    ligne.append(" ")
            else:
                ligne.append(" ")
            if j != 12:
                ligne.append(char[i*13+j])
            else:
                if int_selection == i*13+j:
                    ligne.append(char[i*13+j] + "]")
                else:
                    ligne.append(char[i*13+j] + " ")
                      
        

    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                               Quel est ton nom?                              "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                                   "+"".join(str_charNom)+"                                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                                                                              "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                           "+"".join(ligne[0:26])+"                       "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                           "+"".join(ligne[26:52])+"                       "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                           "+"".join(ligne[52:78])+"                       "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")  
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    

def AfficherMenuHighScores(str_difficulte):        # Fonction pour le menu qui affiche les meilleurs str_scores
    str_scores = ChargerScores(str_difficulte)
    while len(str_difficulte) < 18:
        str_difficulte = str_difficulte + " "  
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                              High Scores "+str_difficulte+"                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if len(str_scores) > 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1. "+str_scores[0][0]+" "+str_scores[0][1][0:2]+" H "+str_scores[0][1][2:4]+" M "+str_scores[0][1][4:6]+" S                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1.                                              "+Fore.GREEN+"█", end = "")     
    print(Fore.GREEN+"█                                                                              █", end = "")
    if len(str_scores) > 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1. "+str_scores[1][0]+" "+str_scores[1][1][0:2]+" H "+str_scores[1][1][2:4]+" M "+str_scores[1][1][4:6]+" S                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                              2.                                              "+Fore.GREEN+"█", end = "")     
        
    print(Fore.GREEN+"█                                                                              █", end = "")
    if len(str_scores) > 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1. "+str_scores[2][0]+" "+str_scores[2][1][0:2]+" H "+str_scores[2][1][2:4]+" M "+str_scores[2][1][4:6]+" S                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                              3.                                              "+Fore.GREEN+"█", end = "")     
        
    print(Fore.GREEN+"█                                                                              █", end = "")
    if len(str_scores) > 3:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1. "+str_scores[3][0]+" "+str_scores[3][1][0:2]+" H "+str_scores[3][1][2:4]+" M "+str_scores[3][1][4:6]+" S                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                              4.                                              "+Fore.GREEN+"█", end = "")     
        
    print(Fore.GREEN+"█                                                                              █", end = "")
    if len(str_scores) > 4:
        print(Fore.GREEN+"█"+Fore.RESET+"                              1. "+str_scores[4][0]+" "+str_scores[4][1][0:2]+" H "+str_scores[4][1][2:4]+" M "+str_scores[4][1][4:6]+" S                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                              5.                                              "+Fore.GREEN+"█", end = "")     
        
    print(Fore.GREEN+"█                                                                              █", end = "")  
    print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
def SauvegarderScores(nom, chronometre, str_difficulte): # Sauvegarder le nom et le temps du scores
    if str_difficulte == "Débutant":
        str_difficulte = "Debutant"
    elif str_difficulte == "Intermédiaire":
        str_difficulte = "Intermediaire"
    
    str_charNom = ""
    for i in range(len(nom)): # Mets en string le nom du joueur
        str_charNom += nom[i]
    heures, minutes, secondes = FormaterHeure(chronometre)
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Scores'+str(str_difficulte), 'a', encoding = "UTF8")
    while len(str_charNom) < 5:
        str_charNom += " "    
    fichier.write(str_charNom+" "+heures+minutes+secondes+"\n")
    fichier.close

def TrierScores(str_difficulte):  # Trier les sscores du plus petit temps au plus grand
    if str_difficulte == "Débutant":
        str_difficulte = "Debutant"
    elif str_difficulte == "Intermédiaire":
        str_difficulte = "Intermediaire"
        
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Scores'+str(str_difficulte), 'r', encoding = "UTF8")
    str_scores = []
    for ligne in fichier:
        str_scores.append([ligne[0:5], ligne[6:12]])   # Prends seulement la partie du temps pour trier
    fichier.close
    
    for i in range(len(str_scores)):
        for j in range(len(str_scores)-1):
            if int(str_scores[j][1]) > int(str_scores[j+1][1]):
                temporaire = str_scores[j]
                str_scores[j] = str_scores[j+1]
                str_scores[j+1] = temporaire
                
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Scores'+str(str_difficulte), 'w', encoding = "UTF8")
    for i in range(5):
        fichier.write(str_scores[i][0]+" "+str_scores[i][1]+"\n")
    fichier.close    
    
def ChargerScores(str_difficulte): # Charge les scores pour l'afficher dans le menu
    if str_difficulte == "Débutant":
        str_difficulte = "Debutant"
    elif str_difficulte == "Intermédiaire":
        str_difficulte = "Intermediaire"
        
    fichier = open(os.path.dirname(os.path.abspath(__file__))+'/../Fichiers/Scores'+str(str_difficulte), 'r', encoding = "UTF8")
    str_scores = []
    for ligne in fichier:
        str_scores.append([ligne[0:5], ligne[6:12]])    
    fichier.close
    return str_scores