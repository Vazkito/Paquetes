'''
Created on 02/12/2014

@author: David
'''
n1= int(input("dame una cifra"))
n2=int(input("dame una cifra"))
n3=int(input("dame una cifra"))
m=0
if n1>n2:
    if n2>n3:
        
        if n1/2==0:
            if n2/2==0:
                if n3/2==0:
                    m=n1        
                    print(m)
    
if n2>n1:
    if n3>n2:
        m= n2*n3
        print(m)
if n3>n1:
    if n2>n3:
        m= n1*n2
        print(m)        
            
    



    
    