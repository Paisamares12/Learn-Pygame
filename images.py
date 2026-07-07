import pygame
import sys

pygame.init()

width = 800
height = 600

surface = pygame.display.set_mode((width, height)) #surface

image = pygame.image.load("Images/happy_crab.png") # -> Surface

rect = image.get_rect() #Obtenemos el rectangulo de la imagen
rect.center = (width // 2, height // 2) #Centramos la imagen en la ventana del juego

#Obtener fuente
font = pygame.font.Font('freesansbold.ttf', 48) #Fuente por defecto de pygame

#Crear texto
text = font.render("Hello World", True, (247, 199, 0)) #Texto, antialiasing, color -> surface
text_center = text.get_rect() #Obtenemos el rectangulo del texto
text_center.center = (width // 2, 30) #Centramos

pygame.mixer.music.load("Sounds/music.mp3") #Cargamos la musica
pygame.mixer.music.set_volume(0.5) #Establecemos el volumen de la musica
pygame.mixer.music.play(-1) #Reproducimos la musica en bucle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Obtenemos el tiempo en milisegundos desde que se inicio el juego y lo convertimos a segundos
    seconds = pygame.time.get_ticks() // 1000 
    text2 = font.render(str(seconds), True, (247,0,48)) #Tiempo transcurrido
    text2_center = text2.get_rect() #Obtenemos el rectangulo del texto
    text2_center.center = (width // 2, height - 30) #Centramos el texto en la ventana del juego

    surface.fill((0, 171, 247)) #Rellenamos la surface con el color
    surface.blit(image, rect) #Dibujamos la imagen centrada en la ventana del juego
    surface.blit(text, text_center) #Dibujamos el texto en la ventana del juego
    surface.blit(text2, text2_center) #Dibujamos el tiempo transcurrido en la ventana del juego
    pygame.display.update()