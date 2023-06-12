import pygame
from .Constantes import *

class casilla:
    tipo = None
    estado = None

    def __init__(self,pantalla,x,y):
        casilla.crearCelda(pantalla,x,y)
        self.pos = x,y
    def crearCelda(pantalla,x,y):
        pantalla.blip(pantalla,FONDOCASILLA,(x,y,WCELDA,HCELDA))