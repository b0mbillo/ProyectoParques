import pygame
from .datos import FONDO_TABLERO,X_TABLERO,Y_TABLERO,W_TABLERO,H_TABLERO

class Fondo:
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.crearFondo()
        
    def crearFondo(self):
        pygame.draw.rect(self.pantalla,FONDO_TABLERO,(X_TABLERO,Y_TABLERO,W_TABLERO,H_TABLERO))