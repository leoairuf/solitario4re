# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time
import numpy as np

class Carta:
    
    def __init__(self,seme,valore,coperta=True):
        self.seme=seme
        self.valore=valore
        self.coperta=coperta
         
class Mazzo:
    
    def __init__(self,lista_carte=[]):
        self.lista_carte=lista_carte
    
    def genera_mazzo_ordinato(self):
        semi = ['B', 'C', 'D', 'S']
        for seme in semi:
            for valore in range(1, 11, 1):
                self.lista_carte.append(Carta(seme,valore))
                
        
    def mischia(self):
        random.shuffle(self.lista_carte)
    
    
    def prima_carta(self):
        if len(self.lista_carte)!=0:
            prima_carta=self.lista_carte.pop(-1)
        else:
            prima_carta=None
        
        return prima_carta
    
     
class Strategia:
    
    def __init__():
        pass
    
    def disponi_carte(mazzo,tavolo):
        
        for i in range(4):
            riga=[]
            for j in range(9):
                carta=mazzo.prima_carta()
                riga.append(carta)
            tavolo.append(riga)
    
    def controlla_riga(carta):
        pass
        
        
        
                
            
class Giocatore:
    def __init__():
        pass
    
    def vittoria():
        #controlla ordinamento carte
        pass
    
    def mazzetto_vuoto():
        pass
        
        
        
class TavoloDaGioco:
    def __init__(self,tavolo=[]):
        self.tavolo=tavolo
        
    
    def sostituisci_carta(self,mazzo,tavolo):
        carta=mazzo.prima_carta()
        riga=controlla_riga(carta)
        tavolo[carta.valore-1][riga]
        pass

    
    
    
    
    
    

mazzo=Mazzo()
mazzo.genera_mazzo_ordinato()



#check se tutto sia in ordine
# for carta in mazzo.lista_carte:
#     print(carta.seme, carta.valore)
#     time.sleep(1)
        
mazzo.mischia()

tavolo=TavoloDaGioco()
Strategia.disponi_carte(mazzo,tavolo.tavolo)

#check se sia stato mischiato
# for carta in mazzo.lista_carte:
  
#     print(carta.seme, carta.valore)
#     time.sleep(0.1)

# print('\n\n\n')

# while len(mazzo.lista_carte) != 0:
#     prima=mazzo.prima_carta()
#     print(prima.seme, prima.valore)
#     time.sleep(0.5)



        
   