import pygame
pygame.init()

infoPantalla = pygame.display.Info()
WIDTH_PANTALLA = infoPantalla.current_w
HEIGHT_PANTALLA = infoPantalla.current_h
pygame.quit()
#falta reescalar pantalla parques, para esto hay que cambiar json
WIDTH = 1280 #SIN USO
HEIGHT = 720 #PARA DEPRECAR

WIDTH_CONFIG = WIDTH_PANTALLA*0.35
HEIGHT_CONFIG = HEIGHT_PANTALLA*0.8



COLOR_PANTALLA = (33,33,33)
FONDO_TABLERO = (220,220,240)

ROJO = (255,87,87)
VERDE = (104,255,92)
AZUL = (90,90,255)
AMARILLO = (255,255,87)
COLORES = [ROJO,AMARILLO,AZUL,VERDE]

#Lo de adelante se cambia para que se reescale automaticamente
T_CARCEL = TCIELO = 720//3 #240

W_CELDA = T_CARCEL//3 #80
H_CELDA = T_CARCEL//8 #30

X_TABLERO = 280
Y_TABLERO = 0

W_TABLERO = H_TABLERO = HEIGHT #esta height seria la de la pantalla

FUENTE_TEXTO = "arialitalic"
FUENTE_TITULO = "arialbold"
FUENTE_SUBTITULO = "arial"