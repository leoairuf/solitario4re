# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:18:56 2021

@author: leona
"""


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