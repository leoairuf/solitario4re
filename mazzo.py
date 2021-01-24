# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:02:25 2021

@author: Leonardo Furia - Lorenzo Marcoccia
"""

from carta import Carta
import random

#----------------------------------------------------------------------------------------------------------------------------------------------#

class Mazzo:
    
    
    def __init__(self, lista_carte = []):
        self.lista_carte = lista_carte
        
        
    def carica_mazzo(self,path):
        
        '''Viene preso in entrata il path del file di testo contenente il mazzo e ,tramite l'ausilio della funzione 
           is_carta, viene creato un oggetto mazzo. Viene comunicato poi all'utente se il mazzo è utilizzabile (non ci
           sono nè duplicati nè errori di qualsiasi genere) o meno.'''
        
        #lettura file di testo
        with open(path,'r') as infile:
            contenuto = infile.readlines()
            for elem in contenuto:
                carta = Carta()
                
                #check se la riga può diventare una carta
                if carta.is_carta(elem):
                    flag = True
                    for i in self.lista_carte:
                        if i.valore == carta.valore and i.seme == carta.seme:
                            flag = False
                    
                    #se la carta è buona e non duplicata, la includo nel mazzo    
                    if flag == True:
                        self.lista_carte.append(carta) #Carta(elem[1],elem[0])) 
            
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
        
        if len(self.lista_carte) != 0:
            prima_carta=self.lista_carte.pop(-1)
        else:
            prima_carta = None
        
        return prima_carta
    
    
    def vuoto(self):
        
        '''Vengono controllate le carte ancora presenti nel mazzetto.'''
        
        return len(self.lista_carte) == 0
        
    