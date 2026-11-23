import pygame

class Repartidor:
    imagen = pygame.image.load("repartidor.png")
    imagen = pygame.transform.scale(imagen, (64, 100))
    ancho = 64
    alto = 100
    velocidad = 1
    tiempo_invulnerable = 1000

    def __init__(self):
        self.x = 368
        self.y = 440
        self.cambio_x = 0
        self.cambio_y = 0
        self.vidas = 3
        self.ultimo_golpe = -1000

    def manejar_tecla_presionada(self, tecla):
        if tecla == pygame.K_LEFT:
            self.cambio_x = -self.velocidad
        if tecla == pygame.K_RIGHT:
            self.cambio_x = self.velocidad
        if tecla == pygame.K_UP:
            self.cambio_y = -self.velocidad
        if tecla == pygame.K_DOWN:
            self.cambio_y = self.velocidad

    def manejar_tecla_soltada(self, tecla):
        if tecla in (pygame.K_LEFT, pygame.K_RIGHT):
            self.cambio_x = 0
        if tecla in (pygame.K_UP, pygame.K_DOWN):
            self.cambio_y = 0

    def mover(self):
        self.x += self.cambio_x
        self.y += self.cambio_y
        self.limitar_a_pantalla()

    def limitar_a_pantalla(self):
        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.ancho:
            self.x = 800 - self.ancho

        if self.y < 0:
            self.y = 0
        elif self.y > 600 - self.alto:
            self.y = 600 - self.alto

    def detener(self):
        self.cambio_x = 0
        self.cambio_y = 0

    def dibujar(self, pantalla, tiempo_actual):
        if not self.esta_invulnerable(tiempo_actual) or (tiempo_actual // 100) % 2 == 0:
            pantalla.blit(self.imagen, (self.x, self.y))

    def esta_invulnerable(self, tiempo_actual):
        return tiempo_actual - self.ultimo_golpe < self.tiempo_invulnerable

    def recibir_golpe(self, tiempo_actual):
        self.vidas -= 1
        self.ultimo_golpe = tiempo_actual

    def obtener_rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    def obtener_centro(self):
        return self.x + self.ancho / 2, self.y + self.alto / 2
