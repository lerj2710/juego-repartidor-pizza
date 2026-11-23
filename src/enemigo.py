import pygame
import random

class Enemigo:
    imagen = None
    ancho = 0
    alto = 0
    velocidad = 0

    def __init__(self):
        self.x, self.y = self.obtener_posicion_inicial()

    @classmethod
    def obtener_posicion_inicial(cls):
        posiciones_por_borde = {
            "arriba": [random.randint(0, 800 - cls.ancho), -cls.alto],
            "abajo": [random.randint(0, 800 - cls.ancho), 600],
            "izquierda": [-cls.ancho, random.randint(0, 600 - cls.alto)],
            "derecha": [800, random.randint(0, 600 - cls.alto)],
        }

        borde = random.choice(list(posiciones_por_borde.keys()))
        return posiciones_por_borde[borde]

    def mover_hacia(self, objetivo_x, objetivo_y):
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia > 0:
            self.x += (dx / distancia) * self.velocidad
            self.y += (dy / distancia) * self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def obtener_rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def obtener_centro(self):
        return self.x + self.ancho / 2, self.y + self.alto / 2
