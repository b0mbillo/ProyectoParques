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
        self.fuenteTexto = pygame.font.SysFont(FUENTE_TEXTO,30)
        self.textoDado_1 = self.textoDado_2 = self.fuenteTexto.render("",True,FONDO_TABLERO)

    def crearTablero(self):
        x = WIDTH_PANTALLA*0.03
        y = HEIGHT_PANTALLA*0.8

        Fondo(self.pantalla)
        self.nombres()
        pygame.Surface.blit(self.pantalla,self.textoDado_1,(x,y))
        pygame.Surface.blit(self.pantalla,self.textoDado_2,(x+100,y))
        Carcel(self.pantalla,X_TABLERO+T_CARCEL/2,T_CARCEL/2, 0)
        Carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,T_CARCEL/2, 1)
        Carcel(self.pantalla,X_TABLERO+T_CARCEL/2,2.5*T_CARCEL, 2)
        Carcel(self.pantalla,X_TABLERO+2.5*T_CARCEL,2.5*T_CARCEL, 3)
        Cielo(self.pantalla)
        casillas = Casilla.crearCasillas(self.pantalla)
        self.lineas()

        return casillas #deberia devolver tambien carceles y cielo?, o hacerlos atributos de tablero

    def lineas(self):
        x, y = X_TABLERO, Y_TABLERO  
        for i in range(4):
           pygame.draw.line(self.pantalla,(0,0,0),(X_TABLERO,y),(X_TABLERO+W_TABLERO,y),3)
           pygame.draw.line(self.pantalla,(0,0,0),(x,Y_TABLERO),(x,H_TABLERO),3)
           x += T_CARCEL
           y += T_CARCEL

    def nombres(self):
        x = WIDTH_PANTALLA*0.03
        y = HEIGHT_PANTALLA*0.1
        for i, nombre in enumerate(self.nombresJugadores):
            y+=HEIGHT_PANTALLA*0.05
            texto = self.fuenteTexto.render(nombre,True,COLORES[i])
            pygame.Surface.blit(self.pantalla,texto,(x,y))

    def tirada(self,dado_1,dado_2):
        valor_1, valor_2 = dado_1.val, dado_2.val
        self.textoDado_1 = self.fuenteTexto.render(f"dado 1: {valor_1}",True,FONDO_TABLERO)
        self.textoDado_2 = self.fuenteTexto.render(f"dado 2: {valor_2}",True,FONDO_TABLERO)
