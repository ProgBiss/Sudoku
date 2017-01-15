'''
Module qui contient des fonctions systèmes.

'''

import os
import sys
import msvcrt

def ActualiserEcran():  # Fonction qui rafraichit la console
    sys.stdout.flush()

def Attendre():       # Fonction qui attends qu'une touche soit appuyée
    msvcrt.getch()
    
def EffacerEcran():    # Fonction qui a pour but d'effacer le contenu de l'écran
    os.system("cls")
    
def Quitter():         # Fonction qui quitte la console
    quit()

    