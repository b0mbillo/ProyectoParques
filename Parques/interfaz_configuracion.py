import pygame
import pygame_gui
from .datos import FUENTE_TITULO, FUENTE_SUBTITULO

class InterfazConfig:
   subtitulos = ["Nombre Jugador #1: ","Nombre Jugador #2: ","Nombre Jugador #3: ","Nombre Jugador #4: ","Numero de Jugadores:      4", "Modo de Juego:        Corriente", "Diseño de tablero:        Regular"]
   def __init__(self,pantalla,manager):
      self.pantalla = pantalla
      self.manager = manager
      self.heightPantalla = self.pantalla.get_height()
      self.widthPantalla = self.pantalla.get_width()
      self.xPadding = self.widthPantalla*0.08
      self.yPadding = self.heightPantalla*0.05

   def crearElementosGUI(self):
      #boton
      xBoton = self.widthPantalla*0.3
      yBoton = self.heightPantalla*0.8
      largoBoton = self.widthPantalla*0.4
      altoBoton = self.heightPantalla*0.05
      pygame_gui.elements.UIButton(relative_rect=pygame.Rect((xBoton,yBoton),(largoBoton, altoBoton)),text="Iniciar Partida", manager=self.manager, object_id=f"botonIniciar")

      #campos de texto de los nombres
      elementos = []
      y = self.yPadding
      i = 0
      for titulo in InterfazConfig.subtitulos:
         i+=1
         y += self.heightPantalla*0.08
         if "Nombre Jugador" in titulo:
            posNumero = titulo.find("#")
            numeroJugador = titulo[posNumero+1]
            nombreInicial = f"Jugador {numeroJugador}"
            #auto escalar tamaños y posicion con width y height
            campoTexto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((self.xPadding+150, y-5), (225, 30)),initial_text=nombreInicial, manager=self.manager, object_id=f"nombreJugador{numeroJugador}")
            campoTexto.set_text_length_limit(20)
            elementos.append(campoTexto)
      return elementos
      

   def dibujarTexto(self):
      fuenteTitulo = pygame.font.SysFont(FUENTE_TITULO,35)
      fuenteSubtitulos = pygame.font.SysFont(FUENTE_SUBTITULO,15)

      titulo = fuenteTitulo.render("Configuración de Partida",True,(50,200,100))

      pygame.Surface.blit(self.pantalla,titulo,(self.xPadding,self.yPadding))
      y = self.yPadding
      for subtitulo in InterfazConfig.subtitulos:
         y += self.heightPantalla*0.08
         textoRenderizado = fuenteSubtitulos.render(subtitulo,True,(0,0,0))
         pygame.Surface.blit(self.pantalla,textoRenderizado,(self.xPadding,y))




