from .Fondo import fondo
from .Carcel import carcel
from .Constantes import *
from .Cielo import cielo
#import Ficha
import pygame

class tablero:
    #capacidad = 4
    def __init__(self,pantalla):
        self.pantalla = pantalla


    def crearTablero(self):
        fondo(self.pantalla)
        carcel(self.pantalla,X_TABLERO+T_CARCEL/2,T_CARCEL/2, 0)
        carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,T_CARCEL/2, 1)
        carcel(self.pantalla,X_TABLERO+T_CARCEL/2,2.5*T_CARCEL, 2)
        carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,2.5*T_CARCEL, 3)
        cielo(self.pantalla)
        #casillas
        self.lineas()
        

    def lineas(self):
        x = X_TABLERO ; y = Y_TABLERO  
        for i in range(4):
           pygame.draw.line(self.pantalla,(0,0,0),(X_TABLERO,y),(X_TABLERO+W_TABLERO,y),3)
           pygame.draw.line(self.pantalla,(0,0,0),(x,Y_TABLERO),(x,H_TABLERO),3)
           x += T_CARCEL
           y += T_CARCEL
 