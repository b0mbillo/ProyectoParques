import pygame
from .datos import COLORES,X_TABLERO,T_CARCEL

class Ficha:
    #cantidadjugadores = 4
    def __init__(self,idJ,idF,pantalla):
        self.idJugador = idJ
        self.idFicha = idF
        self.estado = "Encarcelado"
        self.pantalla = pantalla
        #estos parametros se podrian definir en otro archivo
        match self.idJugador:
            case 0:
                self.pos = (X_TABLERO+T_CARCEL/2,T_CARCEL/2)
                self.img = pygame.image.load("img/r_ficha.png")
            case 1:
                self.pos = (X_TABLERO+2.5*T_CARCEL,T_CARCEL/2)
                self.img = pygame.image.load("img/y_ficha.png")
            case 2:
                self.pos = (X_TABLERO+T_CARCEL/2,2.5*T_CARCEL)
                self.img = pygame.image.load("img/a_ficha.png")
            case 3:
                self.pos = (X_TABLERO+2.5*T_CARCEL,2.5*T_CARCEL)
                self.img = pygame.image.load("img/v_ficha.png")
            case _: 
                self.color = COLORES[self.idJugador]

    def crearFichas(pantalla):
        fichas = [[],[],[],[]]
        for idJugador in range(4):
            for idFicha in range(1):
                ficha = Ficha(idJugador,idFicha,pantalla)
                fichas[idJugador].append(ficha) 
        return fichas
    
    def dibujarFicha(self):
        pygame.Surface.blit(self.pantalla,self.img,self.pos)
