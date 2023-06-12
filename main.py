import pygame
from Parques.Constantes import *
from Parques.Dado import *
from Parques.Tablero import tablero
pygame.init()

pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Parques")


def main():
    correr = True
    while correr:
        pantalla.fill(CPANTALLA)
        tablero(pantalla)
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
