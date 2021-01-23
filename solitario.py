# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:21:30 2021

@author: leona
"""

from mazzo import Mazzo
from giocatore import Giocatore
from tavolo import TavoloDaGioco
from strategia import SemePerRigaDinamico, SemePerRigaPrefissato
from sys import exit
import statistics as stat
import math

#----------------------------------------------------------------------------------------------------------------------------------------------#
class Solitario:
    
    def calcola_probabilità_vittoria(numero_partite):
        partite_vinte = 0 
        for partita in range(numero_partite):
            
            #definisco la classe giocatore, mazzo (che viene anche mischiato), tavolo
            giocatore = Giocatore()  
                
            mazzo = Mazzo()  
            mazzo.genera_mazzo_ordinato()
            mazzo.mischia()
            
            tavolo = TavoloDaGioco(tavolo = [])
        
            #sistemo le carte sul tavolo e genero le corrispondenze riga-seme
            tavolo.disponi_carte(mazzo)
            
            #righe=SemePerRigaPrefissato.stabilisci_seme()
            #righe = SemePerRigaCasuale.stabilisci_seme()
            
            #inizio a giocare
            righe={}
            cont=0
            carta_in = mazzo.prima_carta()
            while not carta_in == None:
                righe, cont = SemePerRigaDinamico.stabilisci_seme(cont, carta_in, righe)
                carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)
            
            #controllo se ho vinto o perso, e aumento il contatore di conseguenza    
            if giocatore.vinto(tavolo, righe): 
               partite_vinte += 1 
               
        return partite_vinte
    
#----------------------------------------------------------------------------------------------------------------------------------------------#
    
    def gioca_partita(args):
        
        #definisco i path da utilizzare per l'importazione di un mazzo singolo
        load_test_path = args.mazzo   
        partita_vinta = False
        
        mazzo = Mazzo()
        
        #importo il mazzo dal file di testo
        if not mazzo.carica_mazzo(load_test_path):
           print('\nNon posso giocare con un mazzo non valido')
           exit()
        
        print('\nMazzo caricato: ')
        for carta in mazzo.lista_carte:
            print(carta.valore, carta.seme)
        
        # with open(load_test_path, 'rb') as apri_mazzo_di_test:
        #     mazzo_importato_di_prova = pickle.load(apri_mazzo_di_test)
        
        giocatore = Giocatore()
        
        tavolo = TavoloDaGioco(tavolo = []) 
        
        tavolo.disponi_carte(mazzo) 
        
        righe = SemePerRigaPrefissato.stabilisci_seme()
        carta_in = mazzo.prima_carta()  
        while not carta_in == None:
            carta_in = tavolo.sostituisci_carta(carta_in, mazzo, tavolo, righe)    
            
        if giocatore.vinto(tavolo, righe):
            partita_vinta = True
            print('\n\npartita vinta !!')
        else:
            print('\n\npartita persa !!')
            
            
        #stampo la configurazione del tavolo per il controllo dell'utente   
        print('\n\n\nconfigurazione tavolo a partita conclusa: ')
        cont=1
        for riga in tavolo.tavolo:
            print(f'\n  riga {cont}')
            cont+=1
            for carta in riga:
                print(carta.valore, carta.seme, carta.coperta)
        
        return partita_vinta
    
    
    def CreaStatistiche(Psim,numero_partite):
        
        media = stat.mean(Psim)
        std = stat.stdev(Psim)
        e = (1.96*std)/(math.sqrt(1000))
        estremo_sx = media - e
        estremo_dx = media + e
        
        print(f'\n\nProbabilità Media di Vittoria su {numero_partite} Partite:  ', media)
        print(f'\nIntervallo di Confidenza: ({estremo_sx},{estremo_dx})')  


