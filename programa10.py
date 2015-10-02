dividendo=int(input("dame un dividendo"))
divisor=int(input("dame un divisor"))
contador=0

numero=dividendo

while numero>=divisor:
    numero=numero-divisor
    contador=contador+1
print"el cociente es:"+ str (contador)
print"el resto es:" + str (numero)
    
    