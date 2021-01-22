# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:58:21 2021

@author: leona
"""

class Carta:
      
    
    def __init__(self, seme=None, valore=None, coperta=True):
        self.seme = seme
        self.valore = valore
        self.coperta = coperta
     
        
    def is_carta(self, elem):
        
        '''Se la riga considerata ha la sintassi richiesta, viene creata una carta e restituito un valore logico True.
           Altrimenti, viene segnalata con un valore logico False e ignorata.'''
        
        flag = False
        if ',' in elem:
            elem = elem.strip().split(',')
            if len(elem) == 2 and elem[1] in 'BSDC' and elem[0].isnumeric():
                if int(elem[0]) > 0  and int(elem[0]) <= 10:
                    self.seme = elem[1]
                    self.valore = int(elem[0])
                    flag=True
                    
        return flag
