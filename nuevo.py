'''
Created on 26/11/2014

@author: David
'''
numero=int(input("dame un numero"))
m=0
n= int(numero)
lista=[0, 0, 0, 0]
indice=0
while n>0:
    m= n % 10;
    n= n /10;
    lista[indice]=m
    indice= indice+1
print(lista)
if lista[0]==lista[3]:
    if lista[1]==lista[2]:
        print"es un numero capicua"
    else:
        print"no es un numero capicua"
else:
    print"no es un numero capicua"

