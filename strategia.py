# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:11:43 2021

@author: Leonardo Furia - Lorenzo Marcoccia
"""
from abc import ABC, abstractmethod
import random

#----------------------------------------------------------------------------------------------------------------------------------------------#

class Strategy(ABC):
    
    '''interface class'''
    
    @abstractmethod
    def stabilisci_seme():
        pass
    
    
    
    
class SemePerRigaCasuale(Strategy):
    
    
    def stabilisci_seme():
        
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


    
    
class SemePerRigaPrefissato(Strategy):
    
    def stabilisci_seme():
        
        '''Viene stabilita una corrispondenza fissa seme-riga per il posizionamento delle carte.'''
        
        semi = ['B', 'C', 'D', 'S']
        righe = {}
        
        indice = 0
        for seme in semi:
            righe[seme] = indice
            indice += 1
            
        return righe 




class SemePerRigaDinamico(Strategy):
    
    '''Viene stabilita una corrispondenza seme-riga in modo dinamico'''
    
    def stabilisci_seme(cont,carta_in,righe):
         
        if carta_in.seme not in righe:
            righe[carta_in.seme] = cont
            cont += 1
                                   
        return righe, cont
        