'''
Contient les fonctions qui permettent d'afficher la grille de jeu ainsi que d'afficher correctectement le temps et
de permettre de sa déplacer dans la grille.

'''
from Colorama.colorama import *
from Fonctions import FinPartie
from Fonctions.Fonctions import *

def FormaterLigne(cases, ligne):  # Afficher les lignes de la grille pour pouvoir se déplacer dedans
    for i in range(len(ligne)):   # Empêche le joueur de modifier les chiffres qui servent à former la grille principal et
        for j in range(9):        # les distingue en étant d'une autre couleur
            if cases[9*i+j][1] != " ":
                if int(cases[9*i+j][1]) < 10:
                    ligne[i] += cases[9*i+j][0]
                    ligne[i] += cases[9*i+j][1]
                    ligne[i] += cases[9*i+j][2]
                    if j == 2 or j == 5:
                        ligne[i] += "║"
                    elif j == 8:
                        pass
                    else:
                        ligne[i] += "│"
                else:
                    ligne[i] += cases[9*i+j][0]
                    
                    ligne[i] += Fore.YELLOW+str(int(cases[9*i+j][1])-10)+Fore.RESET
                    
                    ligne[i] += cases[9*i+j][2]
                    if j == 2 or j == 5:
                        ligne[i] += "║"
                    elif j == 8:
                        pass
                    else:
                        ligne[i] += "│"
            else:
                ligne[i] += cases[9*i+j][0]
                ligne[i] += cases[9*i+j][1]
                ligne[i] += cases[9*i+j][2]
                if j == 2 or j == 5:
                    ligne[i] += "║"
                elif j == 8:
                    pass
                else:
                    ligne[i] += "│"

def FormaterHeure(chronometre): 
    # Mettre un 0 devant les chiffres entre 0 et 9 pour les secondes, les minutes et les heures
    # et les transforment par la suite en "string"    
    if chronometre[2] >=0 and chronometre[2] <= 9:
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
    return (str_heures, str_minutes, str_secondes)

def FormaterDifficulte(str_difficulte): # Afficher la difficulté et faire en sorte que le nombre d'espaces soit correct pour bien fermer le contour de l'écran
    while len(str_difficulte) < 16:
        str_difficulte = str_difficulte + " "  
    return str_difficulte
              
def AfficherGrillePartie(str_difficulte, chronometre, cases, int_selection, str_chiffre):   # Fonction qui affiche la grille de jeu
    
    str_sauvegarder = "  Sauvegarder  "
    str_quitter = "  Quitter  "
    
    ligne = []
    
    for i in range(9): # Initier la liste "ligne"
        ligne.append("")
    
    strDifficulte = FormaterDifficulte(str_difficulte) 
    
    str_heures, str_minutes, str_secondes = FormaterHeure(chronometre)
    if int_selection == 81:
        str_sauvegarder = "> Sauvegarder <"
    elif int_selection == 82:
            str_quitter = "> Quitter <"
    else:
        cases[int_selection][0] = "["   # Marqueur pour indiquer notre position
        cases[int_selection][2] = "]" 
    
    if str_chiffre != " " and str_chiffre != "-" and str_chiffre != "": # Affiche le chiffre qui est appuyé
        if cases[int_selection][1] != " ":
            if int(cases[int_selection][1]) < 10:
                cases[int_selection][1] = str_chiffre
        else:
            cases[int_selection][1] = str_chiffre
    elif str_chiffre == "-":   # Permet d'effacer le chiffre dans la case
        if cases[int_selection][1] != " ":
            if int(cases[int_selection][1]) < 10:
                cases[int_selection][1] = " "
        else:
            cases[int_selection][1] = " "
        
    for i in range(len(cases)): # Montrer la position
        if i != int_selection and cases[i][0] == "[" and cases[i][2] == "]":
            cases[i][0] = " "
            cases[i][2] = " " 
      
    FormaterLigne(cases, ligne)
    if FinPartie.VerifierGrille(cases) == False:   
        # Grille de jeu (difficulté, chronometre, contrôles, options (sauvegarder, quitter))
        print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
        print(Fore.GREEN+"█                                               █                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"                    Sudoku                     "+Fore.GREEN+"█"+Fore.RESET+"  Difficulté: "+strDifficulte+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█                                               █                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗     "+Fore.GREEN+"█"+Fore.RESET+"  Temps:  H: "+str_heures+"  M: "+str_minutes+"  S: "+str_secondes+" "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[0]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[1]+"║     "+Fore.GREEN+"█"+Fore.RESET+"  Contrôles:                  "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█"+Fore.RESET+"       Flèches: Mouvement     "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[2]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣     "+Fore.GREEN+"█"+Fore.RESET+"       Retour: Effacer        "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[3]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█"+Fore.RESET+"       Entrée: Sélectionner   "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[4]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█"+Fore.RESET+"       Espace: Sélectionner   "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[5]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣     "+Fore.GREEN+"█"+Fore.RESET+"       Chiffres: Insérer ce   "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[6]+"║     "+Fore.GREEN+"█"+Fore.RESET+"                   chiffre    "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[7]+"║     "+Fore.GREEN+"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╠───┼───┼───╬───┼───┼───╬───┼───┼───╣     "+Fore.GREEN+"█"+Fore.RESET+"        "+str_sauvegarder+"       "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ║"+ligne[8]+"║     "+Fore.GREEN+"█                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"     ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝     "+Fore.GREEN+"█"+Fore.RESET+"          "+str_quitter+"         "+Fore.GREEN+"█", end = "")   
        print(Fore.GREEN+"█                                               █                              █", end = "") 
        print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
        return False
    else:                      # Menu losqu'on gagne
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
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"                                  Félicitation!                               "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"              Vous avez réussi ce sudoku de difficulté "+strDifficulte+"       "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█"+Fore.RESET+"                   En "+str_heures+" heures, "+str_minutes+" minutes et "+str_secondes+" secondes!                   "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "")  
        print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
        print(Fore.GREEN+"█                                                                              █", end = "") 
        print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
        str_chronometreFinal = "H: "+str_heures+"  M: "+str_minutes+"  S: "+str_secondes+"."
        Attendre()
        return True


# Belle grille qui ne fonctionne pas... RIP
#         ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗     
#         ║   │   │   ║   │   │   ║   │   │   ║    
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢   
#         ║   │   │   ║   │   │   ║   │   │   ║    
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢    
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢     
#         ║   │   │   ║   │   │   ║   │   │   ║     
#         ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝     