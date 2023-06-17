import pygame
from .Constantes import TCIELO,X_TABLERO
class cielo:
    img = pygame.image.load("img\Pixel Skies Background pack by Digital Moons\Pixel Skies 1920x1080px (Full HD)\demo01_PixelSky_1920x1080.png")
    img = pygame.transform.scale(img,(TCIELO,TCIELO))

    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.crearCielo()
    def crearCielo(self):
        pygame.Surface.blit(self.pantalla,self.img,(X_TABLERO+TCIELO,TCIELO))