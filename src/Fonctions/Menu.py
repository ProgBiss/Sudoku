'''
Module qui contient tous les menus du jeu.

'''

from Colorama.colorama import * 

#Fore: BLACK, RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
#print(Fore.RESET + Back.RESET + Style.RESET_ALL)


def AfficherMenuPrincipal(int_selection):    # Fonction pour le menu principal
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         █", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                      > Jouer <            Règlements                         "+Fore.GREEN+"█", end = "")
    elif int_selection == 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                        Jouer            > Règlements <                       "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                        Jouer              Règlements                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                   > High Scores <          Crédits                           "+Fore.GREEN+"█", end = "")
    elif int_selection == 3:
        print(Fore.GREEN+"█"+Fore.RESET+"                     High Scores          > Crédits <                         "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                     High Scores            Crédits                           "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 4:
        print(Fore.GREEN+"█"+Fore.RESET+"                                 > Quitter <                                  "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   Quitter                                    "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"              Contrôles : - Entrée/Espace : Sélectionner                      "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                          - Flèches Haut/Bas : Déplacements                   "+Fore.GREEN+"█", end = "")   
    print(Fore.GREEN+"█"+Fore.RESET+"                          - Échap : Retour/Quitter                            "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuJouer(int_selection):  # Fonction pour le menu de sélection de partie
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
    if int_selection == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                             > Nouvelle partie <                              "+Fore.GREEN+"█", end = "")   
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                               Nouvelle partie                                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                             > Reprendre partie <                             "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                               Reprendre partie                               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  > Retour <                                  "+Fore.GREEN+"█", end = "")     
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                    Retour                                    "+Fore.GREEN+"█", end = "")    
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuCredits():        # Fonction pour le menu qui affiche les crédits
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
    print(Fore.GREEN+"█"+Fore.RESET+"                                Projet session                                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                                  Jeu Sudoku                                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"              Librairie externe Colorama par Jonathan Hartley 2013            "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                     Par Jessee Lefebvre et Nicolas Bisson                    "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                                 Automne 2014                                 "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")  
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")

    
def AfficherMenuQuitter():      # Fonction qui affiche le menu de fin, lorsqu'on quitte le jeu
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         █", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               █", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               █", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               █", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                             Merci d'avoir jouer!                             "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                         Au revoir et à la prochaine!                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")   
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuDifficulte(int_selection):     # Fonction qui affiche le menu de sélection de difficultés
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         █", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               █", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               █", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               █", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                                 > Débutant <                                 "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   Débutant                                   "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                               > Intermédiaire <                              "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                 Intermédiaire                                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                                 > Difficile <                                "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   Difficile                                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 3:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  > Expert <                                  "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                    Expert                                    "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    if int_selection == 4:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  > Retour <                                  "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                    Retour                                    "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")   
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuReglements():            # Fonction qui affiche le menu qui explique les règlements
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         █", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               █", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               █", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               █", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                                   Règlements                                 "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                  Pas 2 chiffres identiques dans la même colonne              "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                  Pas 2 chiffres identiques dans la même rangée               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                  Pas 2 chiffres identiques dans le même carré                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")   
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuValidation(int_selection):  # Fonction pour le menu de validation quand on quitte la partie en cours
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█"+Fore.RESET+"                 Souhaitez-vous sauvegarder avant de quitter?                 "+Fore.GREEN+"█", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   > Oui <                                    "+Fore.GREEN+"█", end = "")   
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                     Oui                                      "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   > Non <                                    "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                     Non                                      "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                                 > Annuler <                                  "+Fore.GREEN+"█", end = "")     
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                   Annuler                                    "+Fore.GREEN+"█", end = "")    
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")


# Fonction pour le menu qui demande dans quel sauvegarde on veut enregistrer ou laquelle charger selon l'option qui est sélectionner lorsque l'ont veut
def AfficherMenuPartie(int_selection, int_action):        # sauvegarder ou charger une partie
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_action == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"              Dans quelle sauvegarde souhaitez-vous sauvegarder?              "+Fore.GREEN+"█", end = "") 
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                   Quelle sauvegarde souhaitez-vous charger?                  "+Fore.GREEN+"█", end = "")         
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 0:
        print(Fore.GREEN+"█"+Fore.RESET+"                                > Sauvegarde 1 <                              "+Fore.GREEN+"█", end = "")   
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  Sauvegarde 1                                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 1:
        print(Fore.GREEN+"█"+Fore.RESET+"                                > Sauvegarde 2 <                              "+Fore.GREEN+"█", end = "")
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  Sauvegarde 2                                "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    if int_selection == 2:
        print(Fore.GREEN+"█"+Fore.RESET+"                                > Sauvegarde 3 <                              "+Fore.GREEN+"█", end = "")     
    else:
        print(Fore.GREEN+"█"+Fore.RESET+"                                  Sauvegarde 3                                "+Fore.GREEN+"█", end = "")    
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+"█                                                                              █", end = "") 
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")
    
    
def AfficherMenuPartieInexistante():      # Fonction qui affiche le menu lorsque l'on charge une partie qui n'existe pas
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████ ", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                 ▄▄▄▄                                                         █", end = "")
    print(Fore.GREEN+"█                █      █     █  █▀▀▀▄    ▄▀▀▀▄   █  ▄▀  █     █               █", end = "")
    print(Fore.GREEN+"█                ▀▄▄▄   █     █  █    █  █     █  █▄▀    █     █               █", end = "")
    print(Fore.GREEN+"█                    █  █     █  █    █  █     █  █▀▄    █     █               █", end = "")
    print(Fore.GREEN+"█                ▄▄▄▄▀   ▀▄▄▄▀   █▄▄▄▀    ▀▄▄▄▀   █  ▀▄   ▀▄▄▄▀                █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                            Il n'y a pas de partie                            "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                        Veuillez en charger une autre                         "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█"+Fore.RESET+"                    Appuyez sur une touche pour continuer...                  "+Fore.GREEN+"█", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")
    print(Fore.GREEN+"█                                                                              █", end = "")   
    print(Fore.GREEN+" ██████████████████████████████████████████████████████████████████████████████", end = "")