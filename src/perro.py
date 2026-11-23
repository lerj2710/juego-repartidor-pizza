import pygame
from enemigo import Enemigo

class Perro(Enemigo):
    imagen = pygame.image.load("perro.png")
    imagen = pygame.transform.scale(imagen, (54, 64))
    ancho = 54
    alto = 64
    velocidad = 0.5
