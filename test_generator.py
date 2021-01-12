# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: leona
"""
import random
import time
from tqdm import tqdm
import os
import pickle
import argparse
import copy
import json


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
       



def salva_mazzo_txt_csv(mazzo, num_partita, esito, dir_txt_path):
    
    with open(dir_txt_path + f'/mazzo{num_partita}_{esito}.txt', 'w+') as outfile:
        for carta in mazzo.lista_carte:
            line = str(carta.valore) + ',' + carta.seme + '\n'
            outfile.writelines(line)



            
def crea_directories(args, dir_obj_path, dir_txt_path):   
    
    if not os.path.exists(args.test): 
       os.makedirs(args.test)      
    
    if not os.path.exists(dir_obj_path):
        os.makedirs(dir_obj_path) 
    if not os.path.exists(dir_txt_path):
        os.makedirs(dir_txt_path)         
 
           
#=========================================================================================================================#


#definisco una directory per immagazzinare i casi di test generati 
parser = argparse.ArgumentParser()

parser.add_argument("-i1", "--test", help = "Directory dei Casi di Test",
                type = str, default = "./Test_Cases/")

args = parser.parse_args()

start = time.perf_counter()    

dir_obj_path = args.test + 'Object_Test_Files'
dir_txt_path = args.test + 'Text_Test_Files'

#creo la directory e le sub-directories se non esistono  
crea_directories(args, dir_obj_path, dir_txt_path) 
         
p_vinte = 0
p_perse = 0    
numero_partite_da_giocare = 500

#ciclo di generazione dei mazzi    
for _ in tqdm(range(numero_partite_da_giocare)):

    giocatore = Giocatore() 
                
    mazzo=Mazzo()  
    mazzo.genera_mazzo_ordinato()
    
    mazzo.mischia()
    
    mazzo_temp = copy.deepcopy(mazzo)
    
    tavolo=TavoloDaGioco(tavolo=[])
    
    Strategia.disponi_carte(mazzo,tavolo.tavolo)
    
    righe = Strategia.stabilisci_seme_per_riga()
    righe_temp = copy.deepcopy(righe)
    
    carta_in = mazzo.prima_carta()    
    while Giocatore.mazzetto_vuoto(mazzo) != True:
        carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
    

    #voglio avere a disposizione 3 casi di test perdenti e 3 casi di test vincenti
    if (giocatore.vinto(tavolo, righe) != True):
        if p_perse < 3:
            p_perse += 1
            esito = 'sconfitta'
            salva_mazzo_txt_csv(mazzo_temp, p_perse, esito, dir_txt_path)
            with open(dir_obj_path + f'/mazzo{p_perse}_{esito}', 'wb') as mazzo_di_test_sconfitto:
                pickle.dump(mazzo_temp, mazzo_di_test_sconfitto)
            with open(args.test + f'righe{p_perse}_{esito}.json', 'w') as outfile:
                json.dump(righe_temp, outfile)    
    else:
        if p_vinte < 3:
            p_vinte += 1
            esito = 'vittoria'
            salva_mazzo_txt_csv(mazzo_temp, p_vinte, esito, dir_txt_path)
            with open(dir_obj_path + f'/mazzo{p_vinte}_{esito}', 'wb') as mazzo_di_test_vinto:
                pickle.dump(mazzo_temp, mazzo_di_test_vinto)
            with open(args.test + f'righe{p_vinte}_{esito}.json', 'w') as outfile:
                json.dump(righe_temp, outfile)     


#verifico che i mazzi siano stati correttamente salvati/importati
for i in range(1,4,1):
    
    load_test_path = dir_obj_path + f'/mazzo{i}_vittoria'    #analogo per sconfitta
    combination_test_path = args.test + f'righe{i}_vittoria.json'   
    
    mazzo_importato_di_prova = Mazzo()
    
    with open(load_test_path, 'rb') as apri_mazzo_di_test:
        mazzo_importato_di_prova = pickle.load(apri_mazzo_di_test)
    
    giocatore = Giocatore()
    
    tavolo=TavoloDaGioco(tavolo=[])
    
    Strategia.disponi_carte(mazzo_importato_di_prova, tavolo.tavolo)
    
    with open(combination_test_path, 'r') as combinazioni_delle_righe:
        righe = json.load(combinazioni_delle_righe)
    
    
    carta_in = mazzo_importato_di_prova.prima_carta()    
    while Giocatore.mazzetto_vuoto(mazzo_importato_di_prova) != True:
        carta_in = tavolo.sostituisci_carta(carta_in, mazzo_importato_di_prova, tavolo, righe)    
     
    cont=0
    for riga in tavolo.tavolo:
        print(f'\n  riga {cont}')
        cont+=1
        for carta in riga:
            print(carta.valore,carta.seme,carta.coperta)
    
    print(giocatore.vinto(tavolo, righe))
    print('Abbiamo importato correttamente una partita vincente!')
    
    time.sleep(5)
        
elapsed = time.perf_counter() - start       