import pygame, pygame_gui, sys, time
from parques import *
"""hacer un menu inicial jugar-opciones-salir"""
def configuracionPartida(reloj):
    pantallaConfig = pygame.display.set_mode((WIDTH_CONFIG,HEIGHT_CONFIG))
    pygame.display.set_caption("Configuracion Partida")
    icono = pygame.image.load("img/v_ficha.png")
    pygame.display.set_icon(icono)

    manager = pygame_gui.UIManager((WIDTH_CONFIG,HEIGHT_CONFIG))
    interfazConfig = InterfazConfig(pantallaConfig,manager)
    elementos = interfazConfig.crearElementosGUI()
    
    
    ejecutarConfiguracion = True
    while ejecutarConfiguracion: 
        tiempoActualizacion = reloj.tick(60)/1000
        pantallaConfig.fill(FONDO_TABLERO)
        interfazConfig.dibujarTexto()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "botonIniciar": 
                    for pos, elemento in enumerate(elementos):
                        if elemento.get_text() == "": #excepcion texto vacio
                            elemento.set_text(f"Jugador {pos+1}") 
                    nombresJugadores = [elemento.get_text() for elemento in elementos]

                    time.sleep(0.8)
                    pantallaJuego = pygame.display.set_mode((WIDTH_PANTALLA,HEIGHT_PANTALLA),pygame.FULLSCREEN)
                    ejecutarConfiguracion = False

            manager.process_events(event)

        manager.update(tiempoActualizacion)
        manager.draw_ui(pantallaConfig)
        pygame.display.update()
    
    return pantallaJuego, nombresJugadores
    #tambien RETORNA cantidad de jugadores, diseño y modo


def main():
    #inicializar pygame y el reloj
    pygame.init()
    reloj = pygame.time.Clock()
    #Ejecutar configuracion de partida
    pantallaParques, nombresJugadores = configuracionPartida(reloj)
    #Configuracion de la pantalla
    pygame.display.set_caption("Parques") #Pyrques luego
    icono = pygame.image.load("img/r_ficha.png")
    pygame.display.set_icon(icono)
    #Crear dados
    dado_1 = Dado()
    dado_2 = Dado()
    #Crear Tablero
    tablero = Tablero(pantallaParques,nombresJugadores)
    #Crear Fichas
    fichas = Ficha.crearFichas(pantallaParques)
    modo = "corriente"
    #Parques
    ejecutarJuego = True
    while ejecutarJuego:
        reloj.tick(60) #definir 60 fps
        #Dibujar juego
        pantallaParques.fill(COLOR_PANTALLA)
        casillas = tablero.crearTablero()
        for fichasJugador in fichas:
            for ficha in fichasJugador:
                ficha.dibujarFicha() 
        #Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutarJuego = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ejecutarJuego = False
                if event.key == pygame.K_d:
                    dado_1.generarValor(); dado_2.generarValor()
                    tirada = dado_1.val,dado_2.val
                    print(f"dado 1: {tirada[0]}, dado 2: {tirada[1]}")
        pygame.display.update()
    pygame.quit()

main()
