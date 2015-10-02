'''
Created on 17/12/2014

@author: David
'''

# i=filas y j=columnas
def rellena_matrix(): 
    i=0
    j=0
    #inicializamos la matriz lista con 3 filas y 4 columnas
    lista= range(0,3)
    for i in range(0,3):
        lista[i]=range(0,4)
        
    #rellenamos la matriz con valores pedidos por teclado
    i=0
    while i<3:
        j=0
        while j<4:
    # con este print nos da la posicion de la "i" que son las filas y la posicion de la "j" que son las columnas
            print "dame la posicion:",i," ",j
            lista[i][j]=int(raw_input())
            
            j+=1
        i+=1
    return lista

#funcion que suma dos matrices y devuelve una tercera matriz resultado de la suma
def sumaMatrix(sumando1,sumando2):
    #inicializamos la matriz resultado con 3 filas y 4 columnas
    resultado= range(0,3)
    for i in range(0,3):
        resultado[i]=range(0,4)
        
    #bucle que suma las dos matrices traspasadas como parametros a la funcion    
    i=0
    while i<3:
        j=0
        while j<4:
            resultado[i][j]=sumando1[i][j]+sumando2[i][j]
            j+=1
        i+=1    
    
    return resultado



matrix1=rellena_matrix()
matrix2=rellena_matrix()

print sumaMatrix(matrix1,matrix2) 
        
        
    