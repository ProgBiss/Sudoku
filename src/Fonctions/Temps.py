'''
Fonctions qui permettent de calculer le temps de la partie.

'''

import time

def DonnerHeureDebut():  # Donne l'heure local (14:58:19) (15:00:00) (01:-58:-19)
    return time.localtime()[3:6] #(heure, min, sec)

def DonnerTemps(heureDebut):    # Permet de faire avancer le temps du chronomètre
    heureActuel = DonnerHeureDebut()
    chronometre = [heureActuel[0]-heureDebut[0], heureActuel[1]-heureDebut[1], heureActuel[2]-heureDebut[2]]
    if chronometre[2] < 0:
        if chronometre[1] > 0:
            chronometre[1] -= 1
            chronometre[2] += 60
        else:
            chronometre[0] -= 1
            chronometre[1] += 59
            chronometre[2] += 60
    if chronometre[1] < 0:
        chronometre[0] -= 1
        chronometre[1] += 60
    if chronometre[0] >= 99:
        chronometre[0] = 99
    return chronometre
    