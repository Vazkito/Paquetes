'''
Created on 01/12/2014

@author: David
'''
"""DIbujo del muneco"""
-*- coding: utf-g -*-
muneco = [" ______\n" + " | |\n" + " |\n"*5 + " -----",\" ______\n" + " | |\n" + " O |\n" + " |\n"*4 + " -----",\
" ______\n" + " | |\n" + " O |\n" + " | |\n" + " |\n"*3 + "-----",\
" ______\n" + " | |\n" + " O |\n" + " --| |\n" + " |\n"*3 + " -----",\
" ______\n" + " | |\n" + " O |\n" + " --|-- |\n" + "|\n"*3 + " -----",\
" ______\n" + " | |\n" + " O |\n" + " --|-- |\n" + " _/ |\n" + " |\n"*2 + " -----",\
" ______\n" + " ||\n" + " O |\n" + " --|-- |\n" + " _/ \_ |\n" + " |\n"*2 + " -----"]

def ocultar(cadena):
"""Crea una lista con la longitud de la palabra"""
ocultada = []
for i incadena:
ocultada += "_"
return ocultada

def sustituir(palabra, oculta, letra):
"""Sustituye la letra si existe en la palabra oculta"""
n = 0
while n < len(palabra):
if palabra[n] ==letra:
oculta[n] = letra
n += 1

def ahorcado():
"""Comienzo del juego, asignacion de palabra y ocultarla"""
while True:
palabra = getpass.getpass("Palabra a adivinar: ")
whilepalabra.isalpha() == False:
print "Ingrese solamente letras"
palabra = getpass.getpass("Palabra a adivinar: ")
palabra = palabra.upper()
listada = list(palabra)
lis_oculta =ocultar(palabra)
"""Asignacion de vidas"""
vidas = 6
nivel = 0
"""Presentacion"""
print "\n--EL AHORCADO--\n\nTienes 6 vidas para adivinar la palabra. Suerte!"
while vidas > 0 and "_" inlis_oculta:
pal_oculta = (" ").join(lis_oculta)
print "\nCantidad de vidas:",vidas,"\n",muneco[nivel],"\n",pal_oculta,"\n"
"""Pedido de letras o palabra completa"""
while True:
letra =... [continua]
