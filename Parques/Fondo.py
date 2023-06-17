import pygame
from .Constantes import FONDO,X_TABLERO,Y_TABLERO,W_TABLERO,H_TABLERO

class fondo:
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.crearFondo()
        
    def crearFondo(self):
        pygame.draw.rect(self.pantalla,FONDO,(X_TABLERO,Y_TABLERO,W_TABLERO,H_TABLERO))