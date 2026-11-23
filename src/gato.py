import pygame
from enemigo import Enemigo


class Gato(Enemigo):
    imagen = pygame.image.load("gato.png")
    imagen = pygame.transform.scale(imagen, (42, 52))
    ancho = 42
    alto = 52
    velocidad = 0.9