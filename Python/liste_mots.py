# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:43:58 2015

@author: Ricco
"""


#***** PROGRAMME PRINCIPAL ****

#on va utiliser une structure de dictionnaire
#matéralisée par les accolades
dico = {}

#saisie et comptage à la volée
while True:
    
    mot = "tt"
    mot = mot.upper()
    #est-ce le mot stop ?
    if (mot == "STOP"):
        #on sort de la boucle
        break
    else:
        #présent dans le dico ?
        if (mot in dico):
            #incrémentation
            dico[mot] = dico[mot] + 1
        else:
            #initialisation
            dico[mot] = 1
        #end if 
    #end if
#end while

#affichage
for (k,v) in dico.items():
    print(k,v)


#***** FIN DU PROG. PRINCIPAL ****
