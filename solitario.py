# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time
import numpy as np

class Carta:
    
    def __init__(self,seme,valore,re = False):
        self.seme = seme
        self.valore = valore
        self.re = re 
         
class Mazzo:
    
    def __init__(self,lista_carte=[]):
        self.lista_carte=lista_carte
    
    def genera_mazzo_ordinato(self):
        semi = ['B', 'C', 'D', 'S']
        for seme in semi:
            for valore in range(1, 11, 1):
                if valore == 10:
                   self.lista_carte.append(Carta(seme,valore,True))
                else:
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
    
    def stabilisci_seme_per_riga():
        semi = ['B', 'C', 'D', 'S']
        indici = list(range(4))
        righe = {}
        
        for seme in semi:
            length = len(indici)
            r = random.randrange(length)
            righe[seme] = indici[r]
            indici.pop(r)
            
        return righe    
            
    
                
            
class Giocatore:
    def __init__():
        pass
    
    def vittoria():
        #controlla ordinamento carte
        pass
    
    def mazzetto_vuoto(mazzo):
        if len(mazzo.lista_carte) != 0:
           return False
        else:
           return True 
   
        
        
        
class TavoloDaGioco:
    def __init__(self,tavolo=[]):
        self.tavolo=tavolo
        
    
    def sostituisci_carta(self,carta_in,mazzo,tavolo,righe):
        
        if carta_in.valore != 10:
           riga = righe[carta_in.seme]
           carta_out = self.tavolo[riga][carta_in.valore - 1]
           self.tavolo[riga][carta_in.valore - 1] = carta_in
           return carta_out
        else:
           mazzo.lista_carte.remove(carta_in)
           carta_out = mazzo.prima_carta() 
           return carta_out
       

    
    
    
    
    
    

mazzo=Mazzo()
mazzo.genera_mazzo_ordinato()



#check se tutto sia in ordine
# for carta in mazzo.lista_carte:
#     print(carta.seme, carta.valore)
#     time.sleep(1)
        
mazzo.mischia()

tavolo=TavoloDaGioco()
Strategia.disponi_carte(mazzo,tavolo.tavolo)
righe = Strategia.stabilisci_seme_per_riga()
#check se sia stato mischiato
# for carta in mazzo.lista_carte:
carta_in = mazzo.prima_carta()    
while (Giocatore.mazzetto_vuoto(mazzo) == False):
    carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
     
          
       
    
    
#     print(carta.seme, carta.valore)
#     time.sleep(0.1)

# print('\n\n\n')

# while len(mazzo.lista_carte) != 0:
#     prima=mazzo.prima_carta()
#     print(prima.seme, prima.valore)
#     time.sleep(0.5)



        
   