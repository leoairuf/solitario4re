# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import statistics


class Carta:
    
    def __init__(self,seme=None,valore=None,coperta=True):
        self.seme = seme
        self.valore = valore
        self.coperta = coperta
        
    def is_carta(self,elem):
        flag=False
        if ',' in elem:
            elem=elem.strip().split(',')
            if len(elem)==2 and elem[1] in 'BSDC' and elem[0].isnumeric():
                if int(elem[0]) > 0  and int(elem[0]) <= 10:
                    self.seme=elem[1]
                    self.valore=elem[0]
                    flag=True
                    
        return flag
         
class Mazzo:
    
    def __init__(self,lista_carte=[]):
        self.lista_carte=lista_carte
        
    def carica_mazzo(self,path):
        #mazzo_temp={}
        with open(path,'r') as infile:
            contenuto=infile.readlines()
            mazzo_temp=[]
            for elem in contenuto:
                carta=Carta()
                
                if carta.is_carta(elem) == True:
                    flag=True
                    for i in mazzo.lista_carte:
                        if i.valore == carta.valore and i.seme==carta.seme:
                            flag=False
                        
                    if flag==True:
                        self.lista_carte.append(carta)#Carta(elem[1],elem[0])) 
                        
            if len(mazzo.lista_carte) != 40:
                print('il mazzo non è completo')
                return False
            else:
                return True
            
        
                              
                    
                            
                
            
            
    
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

mazzo=Mazzo()

mazzo.carica_mazzo("C:\\Users\\leona\\OneDrive\\Documenti\\pyprogram\\mazzo_test.txt")

for carta in mazzo.lista_carte:
    print(carta.valore,carta.seme)


'''
numero_partite=100
probabilità_vittoria=[]

for j in range(100):
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
        while Giocatore.mazzetto_vuoto(mazzo) != True:
            
            carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
              
         
        if (giocatore.vinto(tavolo, righe) == True):
           partite_vinte += 1    

    numero_partite+=100
    
    probabilità_vittoria.append(partite_vinte/numero_partite)
    

media_probabilità=statistics.mean(probabilità_vittoria)
    

plt.plot(probabilità_vittoria)
    
    #     print(carta.seme, carta.valore)
    #     time.sleep(0.1)
    
    # print('\n\n\n')
    '''
# while len(mazzo.lista_carte) != 0:
#     prima=mazzo.prima_carta()
#     print(prima.seme, prima.valore)
#     time.sleep(0.5)
    
    
  #  stampo il tavolo a gioco cncluso
    
    # print('  \n\n  Se False la carta è scoperta \n') 
    # cont=0
    # for riga in tavolo.tavolo:
    #     print(f'\n  riga {cont}')
    #     cont+=1
    #     for carta in riga:
    #         print(carta.valore,carta.seme,carta.coperta)
            
elapsed = time.perf_counter() - start       