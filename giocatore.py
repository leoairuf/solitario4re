# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:15:27 2021

@author: leona
"""



#-----------------------------------------------------------------------------------------------------------------------------------------------#

class Giocatore:
    
    
    def __init__(self, vittoria = True):
        self.vittoria = vittoria
    
    
    def vinto(self, tavolo, righe):
        
        '''Viene controllato l'esito della partita (Vittoria = True, Sconfitta = False)'''
        
        #check se ogni carta è posizionata correttamente
        for k, riga in enumerate(tavolo.tavolo):
            for i, carta in enumerate(riga):
                if righe[carta.seme] != k or carta.valore != i + 1 :
                    self.vittoria = False
                    
        return self.vittoria            
                

   