'''
Created on 21/01/2015

@author: David
'''

# -*- coding: utf-8 -*-
#Definimos la clase padre Automovil
class Automovil:
    def __init__(self):
        self.fabricacion="1900"
        self.PaisOrigen="Espana"
    def Precio(self):
        self.coste=5400
        
#Definimos una clase hijo motocicletas que hereda de automovil
class Motocicletas(Automovil):
    def __init__(self):
        self.NumeroRuedas=2
        
    def Potencia(self):
        self.power=500

