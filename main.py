import pygame
from Parques import *
pygame.init()

pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Parques")
icono = pygame.image.load("img/r_ficha.png")
pygame.display.set_icon(icono)

tablero = tablero(pantalla)
fichas = ficha.crearFichas(pantalla)


def main():
    correr = True
    while correr:
        pantalla.fill(COLOR_PANTALLA)
        tablero.crearTablero()
        for jugador in fichas:
            for ficha in jugador:
                ficha.dibujarFicha() 
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correr = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    dado1 = dado()
                    dado2 = dado()
                    dado1.generarValor(); dado2.generarValor()
                    tirada = dado1.val,dado2.val
                    print("dado 1: {}, dado 2: {}".format(tirada[0],tirada[1]))
                    
    pygame.quit()


main()
