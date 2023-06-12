from Fondo import fondo
from Carcel import carcel
from Constantes import *

class tablero:
    #capacidad = 4
    def __init__(self,pantalla):
        self.crearTablero(pantalla)


    def crearTablero(self,pantalla):

        fondo(pantalla)
        carcel(pantalla,XTABLERO+TCARCEL/2,YTABLERO+TCARCEL/2, 0)
        carcel(pantalla,XTABLERO+2.5*TCARCEL,YTABLERO+TCARCEL/2, 1)
        carcel(pantalla,XTABLERO+TCARCEL/2,YTABLERO+2.5*TCARCEL, 2)
        carcel(pantalla,XTABLERO+2.5*TCARCEL,YTABLERO+2.5*TCARCEL, 3)
        
        
