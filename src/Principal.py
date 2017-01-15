'''
Contient la boucle principal qui permet de changer de menu et de se déplacer dans ceux-ci.

Table des matières (Fonctions)

Modules : -Menu : -AfficherMenuPrincipal
                  -AfficherMenuJouer
                  -AfficherMenuCredits
                  -AfficherMenuQuitter
                  -AfficherMenuDifficulte
                  -AfficherMenuReglements
                  -AfficherMenuValidation
                  -AfficherMenuPartie
                  -AfficherMenuPartieInexistante
                  
          -Grille : -FormaterLigne
                    -FormaterHeure
                    -FormaterDifficulte
                    -AfficherGrillePartie

          -Partie : -SauvegarderPartie
                    -ChargerPartie
                    -CreerPartie
          -HighScores : -AfficherMenuInscription
                        -AfficherMenuHighScores
                        -SauvegarderScores
                        -TrierScores
                        -ChargerScores

          -Temps : -DonnerHeureDebut
                   -DonnerTemps

          -Fonctions : -ActualiserEcran
                       -Attendre
                       -EffacerEcran
                       -Quitter

          -FinPartie : -VerifierCases
                       -VerifierGrille

          -EntreeClavier : -EntreeClavier
'''

from Fonctions.EntreeClavier import *
from Fonctions.Fonctions import *
from Fonctions.Menu import *
from Fonctions.Temps import *
from Colorama.colorama import *
from Fonctions.Temps import *
from Fonctions.Grille import *
from Fonctions.Partie import *
from Fonctions.FinPartie import *
from Fonctions.HighScores import *

init(autoreset=True)  # Initialisation des couleurs

# Initialisation des variables
int_menu = 0
int_selection = 0
int_ancienneSelection = -1
str_chiffre = ""
str_ancienChiffre = ""
nom = []
ancienNom = []
char = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", " ", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", " ", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "OK",)
bool_changement = False
str_ancienChoix = ""

while True:
    str_touche = EntreeClavier()
    if int_menu == 0: # Afficher le menu Principal
        chronometre = [0,0,0]
        ancienChronometre = [0,0,0]
        str_difficulte = ""
        cases = []
        for i in range(81):
            cases.append([" "," "," "])
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuPrincipal(int_selection)
            ActualiserEcran()
            
        if str_touche == "echap":   # Se déplacer dans le menu principal
            int_menu = 3
        elif str_touche == "bas":
            if int_selection == 0 or int_selection == 1:
                int_selection += 2
            elif int_selection == 2:
                int_selection += 2
                str_ancienChoix = "gauche"
            elif int_selection == 3:
                int_selection += 1
                str_ancienChoix = "droite"
            else:
                if str_ancienChoix == "droite":
                    int_selection -= 3
                else:
                    int_selection -= 4
        elif str_touche == "haut":
            if int_selection == 2 or int_selection == 3:
                int_selection -= 2
            elif int_selection == 0:
                int_selection += 4
                str_ancienChoix = "gauche"
            elif int_selection == 1:
                int_selection += 3
                str_ancienChoix = "droite"
            else:
                if str_ancienChoix == "gauche":
                    int_selection -= 2
                else:
                    int_selection -= 1
                    
        elif str_touche == "droite":
            if int_selection == 0 or int_selection == 2:
                int_selection += 1
            elif int_selection == 1:
                int_selection = 0
            elif int_selection == 3:
                int_selection = 2
        elif str_touche == "gauche":
            if int_selection == 1 or int_selection == 3:
                int_selection -= 1
            elif int_selection == 0:
                int_selection = 1
            elif int_selection == 2:
                int_selection = 3
        elif str_touche == "entree" or str_touche == "espace":
            if int_selection == 0: # Menu Jouer
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 1
            elif int_selection == 1: # Menu Règlements
                int_menu = 6
            elif int_selection == 2: # Menu High Scores
                int_ancienneSelection = -1
                int_selection = 0      
                int_menu = 12 # Difficulté des High Scores
            elif int_selection == 3: # Menu Crédits
                int_menu = 2    
            else : # Quitter
                int_menu = 3
            
    elif int_menu == 1: # Pour aller dans le menu Jouer
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuJouer(int_selection)
            ActualiserEcran()        
            
        if str_touche == "echap":    # Se déplacer dans le menu Jouer
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 0   
        elif str_touche == "bas":
            if int_selection != 2:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 2
        elif str_touche == "entree" or str_touche == "espace":
            if int_selection == 0: # Débuter nouvelle partie --> Menu Difficulté
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 4
            elif int_selection == 1: # Reprendre la partie sauvegarder
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 9
            else: # Retour au menu précédent
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 0

    elif int_menu == 2: # Pour aller dans le menuCredits
        EffacerEcran()
        AfficherMenuCredits()
        ActualiserEcran()
        Attendre()
        int_ancienneSelection = -1
        int_selection = 0
        int_menu = 0
        
    elif int_menu == 3: # Pour aller dans le menu Quitter
        EffacerEcran()
        AfficherMenuQuitter()
        ActualiserEcran()
        Attendre()
        Quitter()
        
    elif int_menu == 4: # Pour aller dans le menu Difficulté (de partie)
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuDifficulte(int_selection)
            ActualiserEcran()        
            
        if str_touche == "echap":   # Se déplacer dans le menu Difficulté
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 1   
        elif str_touche == "bas":
            if int_selection != 4:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 4
        elif str_touche == "entree" or str_touche == "espace":
            if int_selection == 0: # Difficulté Débutant choisi
                int_ancienneSelection = -1
                str_difficulte = "Débutant"
                heureDebut = DonnerHeureDebut()
                cases = CreerPartie(int_selection)
                int_selection = 0
                int_menu = 5
            elif int_selection == 1: # Difficulté Intermédiaire choisi
                int_ancienneSelection = -1
                str_difficulte = "Intermédiaire"
                heureDebut = DonnerHeureDebut()
                cases = CreerPartie(int_selection)
                int_selection = 0
                int_menu = 5
            elif int_selection == 2: # Difficulté Difficile choisi
                int_ancienneSelection = -1
                str_difficulte = "Difficile"
                heureDebut = DonnerHeureDebut()
                cases = CreerPartie(int_selection)  
                int_selection = 0              
                int_menu = 5
            elif int_selection == 3: # Difficulté Expert choisi
                int_ancienneSelection = -1
                str_difficulte = "Expert"
                heureDebut = DonnerHeureDebut()
                cases = CreerPartie(int_selection)
                int_selection = 0                
                int_menu = 5     
            else: # Retour au menu précédent
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 1
            
    elif int_menu == 5: # Pour aller dans le menu Grille 
        chronometre = DonnerTemps(heureDebut)  # Mettre à jour le chronomètre
        if int_ancienneSelection != int_selection or ancienChronometre != chronometre or str_chiffre != str_ancienChiffre:
                ancienChronometre = chronometre
                int_ancienneSelection = int_selection
                EffacerEcran()
                if AfficherGrillePartie(str_difficulte, chronometre, cases, int_selection, str_chiffre) == True:
                    int_ancienneSelection = -1
                    int_selection = 0
                    int_menu = 10
                ActualiserEcran()
                str_chiffre = " "
                str_ancienChiffre = str_chiffre
                
        #Selection 0 - 82         
        if str_touche == "echap":    # Pour se déplacer dans la grille de jeu
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 7
        
        elif str_touche == "gauche":
            if int_selection <= 80 and int_selection%9 != 0:
                int_selection -= 1
            elif int_selection <= 62 and int_selection%9 == 0:
                int_selection += 8
            elif int_selection == 63:
                int_selection = 81
            elif int_selection == 72:
                int_selection = 82
            elif int_selection == 81:
                int_selection = 71
            elif int_selection == 82:
                int_selection = 80
                
        elif str_touche == "droite":
            if int_selection%9 != 8 and int_selection <= 79:
                int_selection += 1
            elif int_selection <= 62 and int_selection%9 == 8:
                int_selection -= 8
            elif int_selection == 80: 
                int_selection = 82
            elif int_selection == 71:
                int_selection = 81
            elif int_selection == 81:
                int_selection = 63
            elif int_selection == 82:
                int_selection = 72
        elif str_touche == "haut":
            if int_selection >= 0 and int_selection <= 8:
                int_selection += 72
            elif int_selection >= 9 and int_selection <= 80:
                int_selection -= 9
            elif int_selection == 81:
                int_selection = 82
            elif int_selection == 82:
                int_selection = 81
        elif str_touche == "bas":
            if int_selection <= 71:
                int_selection += 9
            elif int_selection >= 72 and int_selection <= 80:
                int_selection -= 72
            elif int_selection == 81:
                int_selection = 82
            elif int_selection == 82:
                int_selection = 81
        
            
        elif str_touche == "entree" or str_touche == "espace":  
            if int_selection == 82:   # Quitter la partie
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 7
            if int_selection == 81:  # Sauvegarder la partie
                int_ancienneSelection = -1
                int_selection = 0
                int_action = 1
                int_menu = 8
                
        if int_selection <= 80:    # Inscrire les chiffres dans la grille
            if str_touche == "1":
                str_chiffre = "1"
            
            elif str_touche == "2":
                str_chiffre = "2" 
                  
            elif str_touche == "3":
                str_chiffre = "3"  
                  
            elif str_touche == "4":
                str_chiffre = "4" 
                 
            elif str_touche == "5":
                str_chiffre = "5" 
                 
            elif str_touche == "6":
                str_chiffre = "6"  
                
            elif str_touche == "7":
                str_chiffre = "7"  
             
            elif str_touche == "8":
                str_chiffre = "8"   
            
            elif str_touche == "9":
                str_chiffre = "9"
            
            elif str_touche == "retour":
                str_chiffre = "-"
                
    elif int_menu == 6: # Pour aller dans le menu Règlements 
        EffacerEcran()
        AfficherMenuReglements()
        ActualiserEcran()
        Attendre()
        int_ancienneSelection = -1
        int_selection = 0
        int_menu = 0
        
    elif int_menu == 7:  # Pour aller dans le menu Validation
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuValidation(int_selection)
            ActualiserEcran()        
                   
        if str_touche == "bas":   # Se déplacer dans le menu Validation
            if int_selection != 2:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 2
        elif str_touche == "entree" or str_touche == "espace":
            if int_selection == 0: # Sauvegarder et quitter
                int_ancienneSelection = -1
                int_selection = 0
                int_action = 0
                int_menu = 8
            elif int_selection == 1: # Quitter sans sauvegarder
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 0               
            else: # Retour à la partie et ne pas sauvegarder
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 5
                
    elif int_menu == 8: # Pour choisir où Sauvergarder
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuPartie(int_selection, 0)
            ActualiserEcran()
            
        if str_touche == "bas": # Se déplacer pour choisir où sauvegarder
            if int_selection != 2:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 2    
        elif str_touche == "entree" or str_touche == "espace":
            SauvegarderPartie(int_selection + 1, cases, chronometre, str_difficulte)
            int_ancienneSelection = -1
            int_selection = 0
            if int_action == 0:  # Choisir où sauvegarder
                int_menu = 0   
            elif int_action == 1: # Choisir quelle partie charger
                int_menu = 5
        elif str_touche == "echap": # Retour à la partie
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 5
            ActualiserEcran()
            
    elif int_menu == 9: # Pour choisir quelle partie Charger
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuPartie(int_selection, 1)
            ActualiserEcran()
            
        if str_touche == "bas": # Se déplacer pour choisir la sauvegarde à charger
            if int_selection != 2:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 2    
        elif str_touche == "entree" or str_touche == "espace": # Affiche la grille de jeu avec les renseignements sauvegarder (temps, difficulté, chiffre inscrits)
            if ChargerPartie(int_selection + 1) != False:
                str_difficulte, heureDebut, cases = ChargerPartie(int_selection + 1)             
                int_selection = 0
                int_ancienneSelection = -1    
                int_menu = 5
            else:
                int_menu = 13
        elif str_touche == "echap": # Retour au menu précédent
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 1
            ActualiserEcran()
        
    elif int_menu == 10:  # Pour entrer son nom pour les scores
        if int_ancienneSelection != int_selection or bool_changement == True:
            bool_changement = False
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuInscription(int_selection, nom)
            ActualiserEcran()
             
        if str_touche == "haut": # Se déplacer pour choisir les lettres/chiffres à écrire
            if int_selection <= 12:
                int_selection += 26
            else: 
                int_selection -= 13
                
        elif str_touche == "bas":
            if int_selection >= 26:
                int_selection -= 26
            elif int_selection == 38:
                int_selection -= 2
            else:
                int_selection += 13
            
        elif str_touche == "droite":
            int_selection += 1
            if int_selection == 13 or int_selection == 26:
                int_selection -= 13
            elif int_selection == 39:
                int_selection -= 13
                
        elif str_touche =="gauche":
            int_selection -=1
            if int_selection == -1 or int_selection == 12 or int_selection == 25:
                int_selection += 13
                
        elif str_touche == "entree" or str_touche == "espace": # Écrire la lettre/chiffre
            if int_selection == 38:
                SauvegarderScores(nom, chronometre, str_difficulte)
                TrierScores(str_difficulte)
                int_menu = 11
            elif int_selection == 12:
                if len(nom) > 0:    
                    nom.pop()
                    bool_changement = True
            else:
                if len(nom) == 5:
                    nom.pop()
                nom.append(char[int_selection])
                bool_changement = True

        
        elif str_touche == "retour": # Effacer la lettre/chiffre
            if len(nom) > 0:    
                nom.pop()
                bool_changement = True
        
        elif str_touche == "echap": # Retour au menu principal
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 0
        
    elif int_menu == 11:  # Menu des 5 meilleurs scores de la difficulté choisie 
        EffacerEcran()
        AfficherMenuHighScores(str_difficulte)
        ActualiserEcran()
        Attendre()
        int_ancienneSelection = -1
        int_selection = 0
        int_menu = 0    
            
    elif int_menu == 12: # Pour aller dans le menu Difficulté (des high scores)
        if int_ancienneSelection != int_selection:
            int_ancienneSelection = int_selection
            EffacerEcran()
            AfficherMenuDifficulte(int_selection)
            ActualiserEcran()        
            
        if str_touche == "echap":   # sSe déplacer dans le menu Difficulté
            int_ancienneSelection = -1
            int_selection = 0
            int_menu = 0   
        elif str_touche == "bas":
            if int_selection != 4:
                int_selection += 1
            else:
                int_selection = 0
        elif str_touche == "haut":
            if int_selection != 0:
                int_selection -= 1
            else:
                int_selection = 4
        elif str_touche == "entree" or str_touche == "espace":
            if int_selection == 0: # Difficulté Débutant choisi
                str_difficulte = "Débutant"
                int_menu = 11
            elif int_selection == 1: # Difficulté Intermédiaire choisi
                str_difficulte = "Intermédiaire"
                int_menu = 11
            elif int_selection == 2: # Difficulté Difficile choisi
                str_difficulte = "Difficile"
                int_menu = 11
            elif int_selection == 3: # Difficulté Expert choisi
                str_difficulte = "Expert"
                int_menu = 11
            else: # Retour au menu précédent
                int_ancienneSelection = -1
                int_selection = 0
                int_menu = 0
    elif int_menu == 13: # Menu qui dit qu'il n'y a pas de partie dans la sauvegarde
        EffacerEcran()
        AfficherMenuPartieInexistante()
        ActualiserEcran()
        Attendre()
        int_ancienneSelection = -1
        int_selection = 0
        int_menu = 9 