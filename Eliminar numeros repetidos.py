# -*- coding: utf-8 -*-
numeros=[1,3,67,67,8,8,5,9,5,3,0,12,12,23,45,45]

"""   
for elemento in numeros :
    posicion = numeros.index(elemento )
    if posicion != len(numeros) -1:
        if elemento == numeros[posicion + 1]:
            numeros.remove (elemento)
            print numeros
            """
resultados=[]
for indice,elementos in enumerate(numeros):#enumerate para recorrer la lista cuando quiero saber el indice
    if indice != len(numeros) -1: # len (lista) es la longitud total de la lista sin expecificar cuanto ocupe 
        if elementos != numeros[indice+1]:
            resultados.append(elementos)
resultados.append(numeros[-1])#le añadimos un elementpo mas ala lista 
print resultados



