import pygame
from .datos import COLORES,T_CARCEL

class Carcel:
    def __init__(self,pantalla,x,y,color):
        self.pantalla = pantalla
        self.pos = x,y
        self.crearCarcel(color)

    def crearCarcel(self,c):
        color = COLORES[c]
        pygame.draw.circle(self.pantalla,color,self.pos,T_CARCEL//2.5)