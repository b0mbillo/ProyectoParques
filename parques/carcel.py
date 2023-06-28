import pygame
from .datos import COLORES,T_CARCEL
#definir las posiciones en esta clase a partir del color
class Carcel:
    def __init__(self,pantalla,x,y,numColor):
        self.pantalla = pantalla
        self.pos = x,y
        self.numColor = numColor
        self.crearCarcel()

    def crearCarcel(self):
        color = COLORES[self.numColor]
        pygame.draw.circle(self.pantalla,color,self.pos,T_CARCEL//2.5)