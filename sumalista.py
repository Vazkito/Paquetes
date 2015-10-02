'''
Created on 10/12/2014

@author: David
'''
lista=range(15)

import random

contador_introducidos=0

# nos genera numeros aleatorios hasta 15 introduciendolos en una lista#
while contador_introducidos<15:
    aleatorio=random.randrange(1,50)
    lista[contador_introducidos]=aleatorio
    contador_introducidos+=1
print(lista)

contador_introducidos=0
suma=0
# Nos recorre la lista inicial sumando todos los numeros y almacenandolo en la variable suma#

while contador_introducidos<15:
    suma=suma+lista[contador_introducidos]
    contador_introducidos+=1
print "la suma de todos los numeros de la lista es: "+ str (suma)    
    
    

    
