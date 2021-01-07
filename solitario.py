# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time


class Carta:
    
    def __init__(self,seme,valore,coperta=True):
        self.seme=seme
        self.valore=valore
        self.coperta=coperta
        
class Mazzo:
    
    def __init__(self,lista_carte):
        self.lista_carte=lista_carte
        
    def mischia(self):
        random.shuffle(self.lista_carte)
    
    def prima_carta(self):
        pass
    
        

mazzo=Mazzo(lista_carte=[])

semi = ['B', 'C', 'D', 'S']
for seme in semi:
    for valore in range(1, 11, 1):
        mazzo.lista_carte.append(Carta(seme,valore))

#check se tutto sia in ordine
# for carta in mazzo.lista_carte:
#     print(carta.seme, carta.valore)
#     time.sleep(1)
        
mazzo.mischia()

#check se sia stato mischiato
for carta in mazzo.lista_carte:
    print(carta.seme, carta.valore)
    time.sleep(1)



        
   