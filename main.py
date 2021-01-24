# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: Leonardo Furia - Lorenzo Marcoccia
"""

import time
import argparse
from tqdm import tqdm
from solitario import Solitario

#----------------------------------------------------------main------------------------------------------------------------------------------------#

#dichiarazione degli arguments
parser = argparse.ArgumentParser()

parser.add_argument("-i1", "--psingola", help = "Modalità di esecuzione",
                type = str, default = 'False')

parser.add_argument("-i3", "--mazzo", help = "Mazzo di Test",
                type = str, default = "./Custom_Test_Cases/mazzo1_errori.txt")

args = parser.parse_args()


#start del contatore prestazionale
start = time.perf_counter()    


#Di default voglio fare una sola partita con un mazzo importato; altrimenti posso fare il calcolo della probabilità
if args.psingola == 'False':
    
    Psim = []
    numero_partite = 100
    
    for ciclo in tqdm(range(1000)):
        
        partite_vinte = Solitario.calcola_probabilità_vittoria(numero_partite)
        
        #calcolo la probabilità di vittoria
        probabilità_vittoria = partite_vinte/numero_partite
        
        Psim.append(probabilità_vittoria)
    
    Solitario.CreaStatistiche(Psim,numero_partite)
   
else:
    
    vittoria = Solitario.gioca_partita(args)


elapsed = time.perf_counter() - start       
print(f'\nTempo di Esecuzione:  {elapsed}\n\n')