import pygame

class Pizza:
    imagen = pygame.image.load("pizza.png")
    imagen = pygame.transform.scale(imagen, (32, 32))
    ancho = 32
    alto = 32
    velocidad = 3

    def __init__(self, repartidor, objetivo):
        self.x = repartidor.x + 16
        self.y = repartidor.y + 34

        centro_pizza_x, centro_pizza_y = self.obtener_centro()

        centro_objetivo_x, centro_objetivo_y = objetivo.obtener_centro()

        dx = centro_objetivo_x - centro_pizza_x
        dy = centro_objetivo_y - centro_pizza_y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia > 0:
            self.cambio_x = (dx / distancia) * self.velocidad
            self.cambio_y = (dy / distancia) * self.velocidad
        else:
            self.cambio_x = 0
            self.cambio_y = 0

    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def esta_en_pantalla(self):
        return (
            self.x >= -self.ancho
            and self.x <= 800
            and self.y >= -self.alto
            and self.y <= 600
        )

    def obtener_centro(self):
        return self.x + self.ancho / 2, self.y + self.alto / 2
