# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: Leonardo Furia - Lorenzo Marcoccia
"""

import random
import time
import matplotlib.pyplot as plt
import argparse
import json
from tqdm import tqdm
from sys import exit
from abc import ABC, abstractmethod

#------------------------------------------------------------------------------------------------------------------------#

class Carta:
    
    
    def __init__(self,seme=None,valore=None,coperta=True):
        self.seme = seme
        self.valore = valore
        self.coperta = coperta
     
        
    def is_carta(self,elem):
        
        '''Se la riga considerata ha la sintassi richiesta, viene creata una carta e restituito un valore logico True.
           Altrimenti, viene segnalata con un valore logico False e ignorata.'''
        
        flag=False
        if ',' in elem:
            elem=elem.strip().split(',')
            if len(elem)==2 and elem[1] in 'BSDC' and elem[0].isnumeric():
                if int(elem[0]) > 0  and int(elem[0]) <= 10:
                    self.seme=elem[1]
                    self.valore=int(elem[0])
                    flag=True
                    
        return flag
  
#------------------------------------------------------------------------------------------------------------------------#
    
class Mazzo:
    
    
    def __init__(self,lista_carte=[]):
        self.lista_carte=lista_carte
        
        
    def carica_mazzo(self,path):
        
        '''Viene preso in entrata il path del file di testo contenente il mazzo e ,tramite l'ausilio della funzione 
           is_carta, viene creato un oggetto mazzo. Viene comunicato poi all'utente se il mazzo è utilizzabile (non ci
           sono nè duplicati nè errori di qualsiasi genere) o meno.'''
        
        #lettura file di testo
        with open(path,'r') as infile:
            contenuto=infile.readlines()
            for elem in contenuto:
                carta=Carta()
                
                #check se la riga può diventare una carta
                if carta.is_carta(elem):
                    flag=True
                    for i in self.lista_carte:
                        if i.valore == carta.valore and i.seme==carta.seme:
                            flag=False
                    
                    #se la carta è buona e non duplicata, la includo nel mazzo    
                    if flag==True:
                        self.lista_carte.append(carta)#Carta(elem[1],elem[0])) 
            
        #comunicazione all'utente sulla natura del mazzo                
        if len(self.lista_carte) != 40:
            print('il mazzo non è completo')
            return False
        else:
            print('il mazzo è completo')
            return True
        
            
    def genera_mazzo_ordinato(self):
        
        '''Viene generato un mazzo ordinato (1-2-3...10B, 1-2-3...10C, ecc...).'''
        
        semi = ['B', 'C', 'D', 'S']
        for seme in semi:
            for valore in range(1, 11, 1):
                self.lista_carte.append(Carta(seme,valore)) 
                
        
    def mischia(self):
        
        '''Viene mischiato il mazzo.'''
        
        random.shuffle(self.lista_carte)
    
    
    def prima_carta(self):
        
        '''Viene pescata la prima carta dal mazzo.'''
        
        if len(self.lista_carte)!=0:
            prima_carta=self.lista_carte.pop(-1)
        else:
            prima_carta=None
        
        return prima_carta
    
    
    def vuoto(self):
        
        '''Vengono controllate le carte ancora presenti nel mazzetto.'''
        
        return len(self.lista_carte) == 0
        
    
#------------------------------------------------------------------------------------------------------------------------#    
     
class Strategia:
    
    def __init__():
        pass
    
    
    def stabilisci_seme_per_riga():
        
        '''Viene stabilita una corrispondenza casuale seme-riga per il posizionamento delle carte.'''
        
        semi = ['B', 'C', 'D', 'S']
        indici = list(range(4))
        righe = {}
        
        for seme in semi:
            length = len(indici)
            r = random.randrange(length)
            righe[seme] = indici[r]
            indici.pop(r)
            
        return righe 
    
    
    def seme_prefissato():
        
        '''Viene stabilita una corrispondenza fissa seme-riga per il posizionamento delle carte.'''
        
        semi = ['B', 'C', 'D', 'S']
        righe = {}
        
        indice = 0
        for seme in semi:
            righe[seme] = indice
            indice += 1
            
        return righe 
    
#------------------------------------------------------------------------------------------------------------------------#    
                          
class Giocatore:
    
    
    def __init__(self, vittoria = True):
        self.vittoria = vittoria
    
    def vinto(self, tavolo, righe):
        
        '''Viene controllato l'esito della partita (Vittoria = True, Sconfitta = False)'''
        
        #check se ogni carta è posizionata correttamente
        for k, riga in enumerate(tavolo.tavolo):
            for i, carta in enumerate(riga):
                if k != righe[carta.seme] or carta.valore != i + 1 :
                    self.vittoria = False
                    
        return self.vittoria            
                

   
#------------------------------------------------------------------------------------------------------------------------#        
             
class TavoloDaGioco:
    
    
    def __init__(self, tavolo=[]):
        self.tavolo=tavolo
        
    
    def sostituisci_carta(self, carta_in, mazzo, tavolo, righe):
        
        '''Viene presa una carta in entrata, posizionata nello slot in base al suo seme e valore e successivamente
           viene prelevata la carta che era presente nello slot. La carta prelevata diventa così la nuova carta da
           posizionare.'''
        
        if carta_in.valore != 10:
           riga = righe[carta_in.seme]
           carta_out = self.tavolo[riga][carta_in.valore - 1]
           carta_in.coperta=False
           self.tavolo[riga][carta_in.valore - 1] = carta_in
           return carta_out
        #se ho un dieci, prendo direttamente un'altra carta dal mazzetto        
        else:
           return mazzo.prima_carta()
       
    
    def disponi_carte(self, mazzo):
        
        '''Vengono disposte le carte sul tavolo per righe di 9.'''
        
        for i in range(4):
            riga=[]
            for j in range(9):
                carta=mazzo.prima_carta()
                riga.append(carta)
            self.tavolo.append(riga)

#------------------------------------------------------------------------------------------------------------------------#        

def calcola_probabilità_vittoria(numero_partite):
    partite_vinte = 0 
    for partita in tqdm(range(numero_partite)):
        
        #definisco la classe giocatore, mazzo (che viene anche mischiato), tavolo
        giocatore = Giocatore()  
            
        mazzo = Mazzo()  
        mazzo.genera_mazzo_ordinato()
        mazzo.mischia()
        
        tavolo=TavoloDaGioco(tavolo=[])
    
        #sistemo le carte sul tavolo e genero le corrispondenze riga-seme
        tavolo.disponi_carte(mazzo)
        righe = Strategia.stabilisci_seme_per_riga()
        
        #inizio a giocare
        carta_in = mazzo.prima_carta()    
        while not carta_in == None:
            carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
        
        #controllo se ho vinto o perso, e aumento il contatore di conseguenza    
        if giocatore.vinto(tavolo, righe): 
           partite_vinte += 1 
           
    return partite_vinte
    
    
def gioca_partita(args):
    
    #definisco i path da utilizzare per l'importazione di un mazzo singolo
    load_test_path = args.test + 'Text_Test_Files/mazzo1_sconfitta.txt'    
    combination_test_path = args.test + '/righe1_sconfitta.json'  
    partita_vinta = False
    
    mazzo = Mazzo()
    
    #importo il mazzo dal file di testo
    if not mazzo.carica_mazzo(load_test_path):
       print('\nNon posso giocare con un mazzo non valido')
       exit()
    
    
    # with open(load_test_path, 'rb') as apri_mazzo_di_test:
    #     mazzo_importato_di_prova = pickle.load(apri_mazzo_di_test)
    
    giocatore = Giocatore()
    
    tavolo = TavoloDaGioco(tavolo=[]) 
    
    tavolo.disponi_carte(mazzo) 
    
    #importo la combinazione vincente
    with open(combination_test_path, 'r') as combinazioni_delle_righe:
        righe = json.load(combinazioni_delle_righe)
    
    carta_in = mazzo.prima_carta()    
    while not carta_in == None:
        carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)    
        
    if giocatore.vinto(tavolo, righe):
        partita_vinta = True
        print('partita vinta !!')
    else:
        print('partita persa !!')
        
        
    #stampo la configurazione del tavolo per il controllo dell'utente   
    print('\nconfigurazione tavolo a partita conclusa: ')
    cont=1
    for riga in tavolo.tavolo:
        print(f'\n  riga {cont}')
        cont+=1
        for carta in riga:
            print(carta.valore,carta.seme,carta.coperta)
    
    return partita_vinta
    
#========================================================================================================================#    

#dichiarazione degli arguments
parser = argparse.ArgumentParser()

parser.add_argument("-i1", "--modalità", help = "Modalità di esecuzione",
                type = str, default = 'Partita Singola')

parser.add_argument("-i2", "--test", help = "Directory dei Casi di Test",
                type = str, default = "./Custom_Test_Cases/")

args = parser.parse_args()


#start del contatore prestazionale
start = time.perf_counter()    


#Di default voglio fare una sola partita con un mazzo importato; altrimenti posso fare il calcolo della probabilità
if args.modalità != 'Partita Singol':
    
    #P = []
    
    #for _ in tqdm(range(300)):
        
    numero_partite = 10000
    
    partite_vinte = calcola_probabilità_vittoria(numero_partite)
    #calcolo la probabilità di vittoria
    probabilità_vittoria=partite_vinte/numero_partite
    #P.append(probabilità_vittoria)
    
    print('\n\nPartite Giocate:', numero_partite)
    print('\nPartite Vinte:  ',partite_vinte)
    print('\nProbabilità Vittoria:  ',probabilità_vittoria)
    
    #grafico l'andamento della probabilità    
    #plt.plot(P) 
    
else:
    
    vittoria = gioca_partita(args)

    
elapsed = time.perf_counter() - start       

print('\nTempo di Esecuzione:  ', elapsed)