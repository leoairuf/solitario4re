# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm


class Carta:
    
    def __init__(self,seme,valore,coperta=True):
        self.seme = seme
        self.valore = valore
        self.coperta = coperta
         
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
    
    def __init__(self, vittoria = True):
        self.vittoria = vittoria
    
    def vinto(self, tavolo, righe):
        for k, riga in enumerate(tavolo.tavolo):
            for i, carta in enumerate(riga):
                if k != righe[carta.seme] or carta.valore != i + 1 :
                    self.vittoria = False
                    
        return self.vittoria            
                
        
    
    def mazzetto_vuoto(mazzo):
        if len(mazzo.lista_carte) == 0:
           return True
        else:
           return False 
   
        
        
        
class TavoloDaGioco:
    def __init__(self,tavolo=[]):
        self.tavolo=tavolo
        
    
    def sostituisci_carta(self,carta_in,mazzo,tavolo,righe):
        
        if carta_in.valore != 10:
           riga = righe[carta_in.seme]
           carta_out = self.tavolo[riga][carta_in.valore - 1]
           carta_in.coperta=False
           self.tavolo[riga][carta_in.valore - 1] = carta_in
           return carta_out
       
        else:
           return mazzo.prima_carta()
       

    
start = time.perf_counter()    

numero_partite=100
probabilità_vittoria=[]

for j in tqdm(range(200)):
    partite_vinte = 0 
    for _ in range(numero_partite):
        
        giocatore = Giocatore()  
            
        mazzo=Mazzo()  
        mazzo.genera_mazzo_ordinato()
        mazzo.mischia()
        tavolo=TavoloDaGioco(tavolo=[])
    
        Strategia.disponi_carte(mazzo,tavolo.tavolo)
        righe = Strategia.stabilisci_seme_per_riga()
        carta_in = mazzo.prima_carta()    
        while len(mazzo.lista_carte) != 0:
            
            carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
              
         
        if (giocatore.vinto(tavolo, righe) == True):
           partite_vinte += 1    

    numero_partite += 50
    
    probabilità_vittoria.append(partite_vinte/numero_partite)
    

plt.plot(probabilità_vittoria)

elapsed = time.perf_counter() - start       