import pygame
from  Constantes import *

class fondo:
    def __init__(self,pantalla):
        self.crearFondo(pantalla)
        
    def crearFondo(self,pantalla):
        pygame.draw.rect(pantalla,FONDO,(XTABLERO,YTABLERO,WTABLERO,HTABLERO))