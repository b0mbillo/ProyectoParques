import pygame
from .Constantes import COLORES,T_CARCEL

class carcel:
    def __init__(self,pantalla,x,y,color):
        self.pantalla = pantalla
        self.pos = x,y
        self.crearCarcel(color)

    def crearCarcel(self,c):
        color = COLORES[c]
        pygame.draw.circle(self.pantalla,color,self.pos,T_CARCEL//2)