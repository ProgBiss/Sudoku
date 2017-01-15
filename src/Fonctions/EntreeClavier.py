'''
Contient la fonction qui lit les touches appuyés pour se déplacer dans les menus, la grille et inscrire les chiffres.

'''

import msvcrt as m

def EntreeClavier():   # Fonction qui prend les entrées clavier lorsqu'une touche est appuyée et retourne un string qui contient cette touche
    if m.kbhit():
        int_touche = ord(m.getch()) #enter = 13 space = 32 0 = 48, 1 = 49...
        if int_touche == 224: # Special 
            pass
        elif int_touche == 75: # Gauche
            return "gauche"
        elif int_touche == 77: # Droite
            return "droite"
        elif int_touche == 72: # Haut
            return "haut"
        elif int_touche == 80: # Bas
            return "bas"
        elif int_touche == 27: # Echap
            return "echap"
            print("echap")
        elif int_touche == 49: 
            return "1"
        elif int_touche == 50: 
            return "2"
        elif int_touche == 51: 
            return "3"
        elif int_touche == 52: 
            return "4"
        elif int_touche == 53: 
            return "5"
        elif int_touche == 54: 
            return "6"
        elif int_touche == 55: 
            return "7"
        elif int_touche == 56: 
            return "8"
        elif int_touche == 57: 
            return "9"
        elif int_touche == 13:   
            return "entree" 
        elif int_touche == 32:   
            return "espace"
        elif int_touche == 8:
            return "retour"
        else:
            return str(int_touche)
    else:
        return None