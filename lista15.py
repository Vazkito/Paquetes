'''
Created on 10/12/2014

@author: David
'''
mayor=0
lista=range(15)

import random
 
contador_introducidos=0
contador_comparacion=0

while contador_introducidos<15:
    
    import random
    aleatorio=random.randrange(1,50)
    
    lista[contador_introducidos]=aleatorio
    contador_introducidos+=1

   
    
   
print(lista)    

contador_introducidos=1   #indice global,,, por donde voy
contador_comparacion=0 # posicion del mayor

while contador_introducidos<15:
    #         actual               >  maximo  ???
    if(lista[contador_introducidos]>lista[contador_comparacion]):
        contador_comparacion=contador_introducidos
    contador_introducidos=contador_introducidos+1

print "la posicion en la que esta el maximo es "+ str(contador_comparacion)
print lista[contador_comparacion]


    
    