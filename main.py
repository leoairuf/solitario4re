# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:08:17 2021

@author: Leonardo Furia - Lorenzo Marcoccia
"""

import time
import argparse
from tqdm import tqdm
import statistics as stat
import math
import solitario

#----------------------------------------------------------------------------------------------------------------------------------------------#

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
        
        partite_vinte = solitario.calcola_probabilità_vittoria(numero_partite)
        
        #calcolo la probabilità di vittoria
        probabilità_vittoria = partite_vinte/numero_partite
        
        Psim.append(probabilità_vittoria)
    
    media = stat.mean(Psim)
    std = stat.stdev(Psim)
    e = (1.96*std)/(math.sqrt(1000))
    estremo_sx = media - e
    estremo_dx = media + e
    
    print(f'\n\nProbabilità Media di Vittoria su {numero_partite} Partite:  ', media)
    print(f'\nIntervallo di Confidenza: ({estremo_sx},{estremo_dx})')    

    
else:
    
    vittoria = solitario.gioca_partita(args)


elapsed = time.perf_counter() - start       
print(f'\nTempo di Esecuzione:  {elapsed}\n\n')