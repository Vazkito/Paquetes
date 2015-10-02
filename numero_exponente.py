'''
Created on 18/11/2014

@author: David
'''
base=int(input("dame la base"))
exponente=int(input("dame el exponente"))
contador=0
resultado=1
while contador<exponente:
    resultado=resultado*base
    contador=contador+1
print(resultado)

