'''
Created on 17/12/2014

@author: David
'''
# Declaramos la funcion:
# def nombre de la funcion (parametros):
#    cuerpo de la funcion
#    return valor a devolver

# la funcion def opera directamente asignando valor1 y 2 a sumando1 y 2 sin necesidad de un (=)

def suma(sumando1, sumando2):
    resultado=sumando1+sumando2
    return resultado


def saludar():
    print "hola como estas"


print "dame el primer sumando"
valor1=int(raw_input())

print "dame el segundo sumando"
valor2=int(raw_input())

print suma(valor1, valor2)

saludar()





