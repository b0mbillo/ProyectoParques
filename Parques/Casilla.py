import pygame
import json
from .datos import *
with open("Parques/Casillas.json", "r") as archivo:
        contenido = json.load(archivo)

class Casilla:
    def __init__(self,pantalla,idC,x,y,color,tipo,orientacion):
        self.pantalla = pantalla
        self.idCasilla = idC
        self.pos = x,y
        self.color = color
        self.tipo = tipo
        self.orientacion = orientacion
        match self.color:
            case "blanco":
                self.img = pygame.image.load("img/casilla.png")
            case "rojo":
                self.img = pygame.image.load("img/r_casilla.png")
            case "azul":
                self.img = pygame.image.load("img/a_casilla.png")
            case "verde":
                self.img = pygame.image.load("img/v_casilla.png")
            case "amarillo":
                self.img = pygame.image.load("img/y_casilla.png")
        self.dibujarCasilla()

    def crearCasillas(pantalla):
        idCasilla = 1
        datosCasillas = contenido["casillas"]
        casillas = []
        for casilla in datosCasillas:
            objCasilla = Casilla(pantalla,idCasilla,int(casilla["x"]),int(casilla["y"]),casilla["color"],casilla["tipo"],casilla["orientacion"])
            idCasilla += 1
            casillas.append(objCasilla)
        return casillas


    def dibujarCasilla(self):
        if self.orientacion == "vertical":
            self.img = pygame.transform.rotate(self.img,-90)
        pygame.Surface.blit(self.pantalla,self.img,self.pos)