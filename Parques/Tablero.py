from .fondo import Fondo
from .carcel import Carcel
from .datos import *
from .cielo import Cielo
from .casilla import Casilla
#import Ficha
import pygame

class Tablero:
    #por ahora capacidad = 4
    def __init__(self,pantalla,nombresJugadores):
        self.pantalla = pantalla
        self.nombresJugadores = nombresJugadores

    def crearTablero(self):
        Fondo(self.pantalla)
        self.nombres()
        Carcel(self.pantalla,X_TABLERO+T_CARCEL/2,T_CARCEL/2, 0)
        Carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,T_CARCEL/2, 1)
        Carcel(self.pantalla,X_TABLERO+T_CARCEL/2,2.5*T_CARCEL, 2)
        Carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,2.5*T_CARCEL, 3)
        Cielo(self.pantalla)
        casillas = Casilla.crearCasillas(self.pantalla)
        self.lineas()
        return casillas

    def lineas(self):
        x = X_TABLERO ; y = Y_TABLERO  
        for i in range(4):
           pygame.draw.line(self.pantalla,(0,0,0),(X_TABLERO,y),(X_TABLERO+W_TABLERO,y),3)
           pygame.draw.line(self.pantalla,(0,0,0),(x,Y_TABLERO),(x,H_TABLERO),3)
           x += T_CARCEL
           y += T_CARCEL

    def nombres(self):
        fuenteTexto = pygame.font.SysFont(FUENTE_TEXTO,30)
        i = 0
        x = WIDTH_PANTALLA*0.07
        y = HEIGHT_PANTALLA*0.1
        for nombre in self.nombresJugadores:
            y+=HEIGHT_PANTALLA*0.05
            texto = fuenteTexto.render(nombre,True,COLORES[i])
            pygame.Surface.blit(self.pantalla,texto,(x,y))
            i+=1

            
 