# -*- coding: utf-8 -*-

#Crear un programa que al escribir una palabra detecte las letras repetidas que hay y el numero de esta

indice=0
palabra=(raw_input("Dime una palabra:"))

resultados=[]

for indice,elementos in enumerate(palabra):#enumerate para recorrer la lista cuando quiero saber el indice
    if indice != len(palabra)  : # len (lista) es la longitud total de la lista sin expecificar cuanto ocupe 
        if palabra.count(elementos) > 1: #Recorremos de principio a fin la lista con un bucle for y en cada parada hacemos una comprobación: si el número de veces que aparece ese elemento es mayor que uno, lo mostramos.
            resultados.append(elementos)
print(resultados)
        



