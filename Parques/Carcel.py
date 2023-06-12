import pygame
from .Constantes import *

colores = [ROJO,AMARILLO,AZUL,VERDE]
class carcel:

    def __init__(self,pantalla,x,y,c):
        carcel.crearCarcel(pantalla,x,y,c)
        self.pos = x,y

    def crearCarcel(pantalla,x,y,c):
        for i,j in zip(range(4),colores):
            if c == i:
                color = j
        pygame.draw.circle(pantalla,color,(x,y),TCARCEL//2)