import pygame
import sys

pygame.init()

width = 800
height = 600

surface = pygame.display.set_mode((width, height)) #surface

image = pygame.image.load("Images/Happy_crab.png") # -> Surface

rect = image.get_rect() #Obtenemos el rectangulo de la imagen
rect.center = (width // 2, height // 2) #Centramos la imagen en la ventana del juego

#Obtener fuente
font = pygame.font.Font('freesansbold.ttf', 40) #Fuente por defecto de pygame

#Crear texto
text = font.render("Hello World", True, (247, 199, 0)) #Texto, antialiasing, color -> surface
text_center = text.get_rect() #Obtenemos el rectangulo del texto
text_center.center = (width // 2, 30) #Centramos

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0, 171, 247)) #Rellenamos la surface con el color
    surface.blit(image, rect) #Dibujamos la imagen centrada en la ventana del juego
    surface.blit(text, text_center) #Dibujamos el texto en la ventana del juego
    pygame.display.update()