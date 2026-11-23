import pygame
import random

# Inicializar a Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")
icono = pygame.image.load("pizza.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (800, 600))

# Repartidor
repartidor_img = pygame.image.load("repartidor.png")
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100))
repartidor_x = 368
repartidor_y = 440
repartidor_x_cambio = 0
repartidor_y_cambio = 0
velocidad_repartidor = 1

# Perro
perro_img = pygame.image.load("perro.png")
perro_img = pygame.transform.scale(perro_img, (54, 64))
perro_x = random.randint(0, 746)
perro_y = 0
velocidad_perro = 0.5

# Movimiento repartidor
def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))

# Movimiento perro
def perro(x, y):
    pantalla.blit(perro_img, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                repartidor_x_cambio = -velocidad_repartidor
            if evento.key == pygame.K_RIGHT:
                repartidor_x_cambio = velocidad_repartidor
            if evento.key == pygame.K_UP:
                repartidor_y_cambio = -velocidad_repartidor
            if evento.key == pygame.K_DOWN:
                repartidor_y_cambio = velocidad_repartidor
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                repartidor_x_cambio = 0
            if evento.key in (pygame.K_UP, pygame.K_DOWN):
                repartidor_y_cambio = 0
    repartidor_x += repartidor_x_cambio
    repartidor_y += repartidor_y_cambio
    if repartidor_x < 0:
        repartidor_x = 0
    elif repartidor_x > 736:
        repartidor_x = 736
    if repartidor_y < 0:
        repartidor_y = 0
    elif repartidor_y > 500:
        repartidor_y = 500

    # Movimiento del perro hacia el repartidor
    dx = repartidor_x - perro_x
    dy = repartidor_y - perro_y
    distancia = (dx ** 2 + dy ** 2) ** 0.5
    if distancia > 0:
        perro_x += (dx / distancia) * velocidad_perro
        perro_y += (dy / distancia) * velocidad_perro

    pantalla.blit(fondo, (0, 0))
    repartidor(repartidor_x, repartidor_y)
    perro(perro_x, perro_y)
    pygame.display.update()

pygame.quit()
