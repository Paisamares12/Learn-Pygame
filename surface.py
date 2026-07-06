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

#Con tuplas
rojo = (255, 0, 0) #0 - 255
verde = (0, 255, 0) #0 - 255
azul = (0, 0, 255) #0 - 255

#Rectangulos
rect = pygame.Rect(0, 0, 200, 200) #x, y, width, height
rect.center = (width // 2, height // 2) #Centramos el rectangulo en la ventana del juego

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
    surface.fill(blue) #Rellenamos la ventana del juego con el color definido
    #Dibujamos un rectangulo en la ventana del juego
    pygame.draw.rect(surface, red, rect) #Donde se dibuja el rectangulo, color del rectangulo, rectangulo a dibujar
    pygame.display.update() #Actualizamos la ventana del juego para que se vea el color de fondo