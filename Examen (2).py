#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import wx
import random
# Examen Francisco Redondo López
# Constantes 
ancho = 350
largo = 650
incremento = 5   # incremento de la coordenada que se hará cuando proceda
delay_movimiento =50       # Delay en ms de los temporizadores
limite_arriba= 20
limite_abajo = largo-60
# Ventana aplicación 
class JaviFrame (wx.Frame):
    def  __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(ancho,largo))
        
        #Layout
        self.panel1=wx.Panel(self, -1)        
        self.boton_mover=wx.Button(self.panel1, -1, label="Botón 1", size=(100, 20), pos=(150, 200))
        
                
        self.btnNumero=wx.Button(self.panel1, -1, label="0", size=(100, 20), pos=(50, 400))
        

        self.textoCoordenada=wx.StaticText(self.panel1,-1, 'Posición botón', (30, 20)) 
        self.CuadroX=wx.TextCtrl(self.panel1, -1, size=(30, 20), pos=(50, 50))
        self.CuadroY=wx.TextCtrl(self.panel1, -1, size=(30, 20), pos=(80, 50))
       
       
        #self.boton_mover.Bind(wx.EVT_BUTTON, self.mover, self.boton_mover)
        self.temporizadorMover=wx.Timer()
        self.temporizadorMover.Bind(wx.EVT_TIMER, self.mover, self.temporizadorMover)
        self.msubir=1 # comienza subiendo
        self.mbajar=0 # comienza subiendo
        self.temporizadorMover.Start(delay_movimiento)
            
            
        # Timers & Event --> Solo un timer para el movimiento
        self.temporizadorAleatorio=wx.Timer()
        self.temporizadorAleatorio.Bind(wx.EVT_TIMER, self.generarNumero, self.temporizadorAleatorio)
        self.temporizadorAleatorio.Start(3000)
        
        # Register event handler for close event. (al pulsar el aspa 
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Centre( wx.BOTH )
        # Show frame
        self.Show()
    
    # Cerrar aplicación
    def onClose(self, event):
        # We bind this callback to the window's close event to destroy the
        #   window and stop the wx event loop.
        print "Aplicación cerrada"
        self.Show(False)
        self.Destroy()        
        
   
    # Controla el movimiento de la pelota en función del botón que YA se haya pulsado
    def mover(self, event):
        posicion=self.boton_mover.GetPositionTuple()
        nueva_x,nueva_y=posicion
        if self.msubir:
            # subir mientras no haya llegado arriba (y>20)
            if posicion[1]>limite_arriba:
                nueva_y=posicion[1]-incremento
            else: # al llegar arriba 
                self.msubir=0 
                self.mbajar=1
        else:
            # bajar mientras no haya llegado abajo (y<460)
            if posicion[1]<limite_abajo:
                nueva_y=posicion[1]+incremento                
            else:
                self.mbajar=0 
                self.msubir=1
       
        # Actualiza nueva coordenadas X e Y en el cuadro
        self.CuadroX.SetValue(str(nueva_x))
        self.CuadroY.SetValue(str(nueva_y))
        # Actualiza la nueva coordenadas
        self.boton_mover.MoveXY(nueva_x, nueva_y)
        
    def generarNumero(self, event):
        print "generar numero"
        numero_aletatorio=random.randrange(10)
        self.btnNumero.SetLabelText(str(numero_aletatorio))
        print numero_aletatorio
        print self.esprimo(numero_aletatorio)
        if self.esprimo(numero_aletatorio):
           nueva_x, nueva_y=self.boton_mover.GetPositionTuple() 
           # Actualiza la nueva coordenadas
           self.btnNumero.MoveXY(nueva_x, nueva_y)
                   
    def esprimo(self,numero):
        indice=2        
        while indice<numero:
            if(numero % indice ==0): # División entera               
                return False
            else:                
                return True          
            indice=indice+1                    
if __name__ == "__main__":
    app=wx.App()
    miFrame=JaviFrame(None, -1, "Sube Baja")
    app.MainLoop()
    
    
