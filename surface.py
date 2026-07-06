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

#Generamos un ciclo infinito para que la ventana del juego se mantenga abierta
while True:
    #Escuchamos los eventos que ocurren en la ventana del juego
    for event in pygame.event.get():
        #Si le damos clic en cerrar ventana se cierra el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #Evita errores del sistema al cerrar la ventana del juego
