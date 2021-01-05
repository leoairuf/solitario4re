# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""

class Carta:
    
    def __init__(self,seme,valore,coperta=True):
        self.seme=seme
        self.valore=valore
        self.coperta=coperta
        
class Mazzo:
    def __init__(self,lista_carte):
        self.lista_carte=lista_carte
        
    def mischia(self):
        pass
    
    def prima_carta(self):
        pass
    
        

mazzo=Mazzo(lista_carte=[])
mazzo.lista_carte.append(Carta('denari', 1))
mazzo.lista_carte.append(Carta('bastoni', 4))





        
   