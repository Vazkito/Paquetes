#creamos dos listas una que contengan x y otra que no despues con un for elemento in palabra 


#sorted#sirve para ordenar tanto numeros como letras

# -*- coding: utf-8 -*-

palabras=["est","abc","rms","xyz","wzo","stf","xlm","toq","phf","xfm"]

listax=[]
listanox=[]

for elemento in palabras:
    
    if elemento[0]=="x":
        
        listax.append(elemento)
        
    else:
        
        listanox.append(elemento)
        
listafinal=sorted(listax) + sorted(listanox)
        
print listafinal
        
    
        
        