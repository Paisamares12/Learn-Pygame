import sys
#Importamos la librería de pygame (para crear videojuegos)
import pygame

#Iniciamos la libreria de pygame
pygame.init()

#Variables que definen el tamaño de la ventana
width = 800
height = 600

#Creamos la ventana del juego y definimos su tamaño
surface = pygame.display.set_mode((width, height)) #surface
#Le damos un título a la ventana del juego
pygame.display.set_caption("Crabby")   
"""
-RGB (Red, Green, Blue) para definir el color de fondo de la ventana del juego.
-Los colores se definen con valores del 0 al 255, donde 0 es la ausencia del color y 255 
es el color en su máxima intensidad.
-Los colores se definen mediante tuplas de 3 valores, donde el primer valor es el rojo, 
el segundo es el verde y el tercero es el azul.
"""
#Con la libreria color
red = pygame.Color(255, 0, 0) #0 - 255
green = pygame.Color(0, 255, 0) #0 - 255
blue = pygame.Color(0, 0, 255) #0 - 255
white = pygame.Color(255, 255, 255) #0 - 255

#Con tuplas
rojo = (255, 0, 0) #0 - 255
verde = (0, 255, 0) #0 - 255
azul = (0, 0, 255) #0 - 255

#Rectangulos
#Rectangulo con pygame
rect = pygame.Rect(0, 0, 200, 200) #x, y, width, height
rect.center = (width // 2, height // 2) #Centramos el rectangulo en la ventana del juego

#Rectangulo con tuplas
rect2 = (0, 0, 200, 200) #No se pueden usar métodos de rectangulo con tuplas, solo se pueden usar con pygame.Rect

print(rect) #Imprimimos las propiedades del rectangulo
print(rect.x, rect.y) #Imprimimos la posición del rectangulo

#Generamos un ciclo infinito para que la ventana del juego se mantenga abierta
while True:

    #Escuchamos los eventos que ocurren en la ventana del juego
    for event in pygame.event.get():

        #Si le damos clic en cerrar ventana se cierra el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #Evita errores del sistema al cerrar la ventana del juego

    #Rellenamos la ventana del juego con el color definido
    surface.fill(blue) 

    #Dibujamos los rectangulos en la ventana del juego
    pygame.draw.rect(surface, red, rect) #Donde ,color, rectangulo a dibujar
    pygame.draw.rect(surface, green, rect2) 
    """
    El orden al dibujar los objetos es importante, ya que si dibujamos un objeto encima de otro, 
    el objeto dibujado primero quedará debajo del objeto dibujado después.
    Draw
    -Donde se dibujara la figura
    -Color de la figura
    """

    #Posición del rectangulo, tamaño del rectangulo
    pygame.draw.rect(surface, white, (20,20, 200, 200)) 

    #Posición del circulo, radio del circulo
    pygame.draw.circle(surface, green, (width // 2, height // 2), 100) 

    #Posición inicial de la linea, posición final de la linea, grosor de la linea
    pygame.draw.line(surface, red, (0, 100), (width, height), 5) 

    #Actualizamos la ventana del juego
    pygame.display.update() 