import pygame
import random
from perro import Perro
from gato import Gato
from pizza import Pizza
from repartidor import Repartidor
from interfaz import Interfaz

# Inicializar a Pygame
pygame.init()

# Sonido
pygame.mixer.music.load("MusicaFondo.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

sonido_disparo = pygame.mixer.Sound("disparo.mp3")
sonido_golpe = pygame.mixer.Sound("golpe.mp3")
sonido_vida_perdida = pygame.mixer.Sound("vida_perdida.mp3")

sonido_disparo.set_volume(0.8)
sonido_golpe.set_volume(0.8)
sonido_vida_perdida.set_volume(0.8)

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")
icono = pygame.image.load("pizza.png")
pygame.display.set_icon(icono)

# Fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (800, 600))

# Pizza
pizzas = []
ultimo_lanzamiento_pizza = 0
tiempo_entre_pizzas = 3000

# Vidas
corazon_img = pygame.image.load("corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (32, 32))

# Repartidor
repartidor = Repartidor()

# Interfaz
interfaz = Interfaz()

# Enemigos
enemigos = []
ultimo_enemigo_creado = 0
tiempo_entre_enemigos = 2000

# Puntaje y tiempo
puntaje = 0
fuente = pygame.font.Font(None, 36)
fuente_game_over = pygame.font.Font(None, 96)
fuente_fin = pygame.font.Font(None, 48)
tiempo_inicio = pygame.time.get_ticks()
tiempo_final = 0
estado_juego = "jugando"
musica_detendida = False

# Movimiento enemigos
def crear_enemigo():
    tipo_enemigo = random.choice([Perro, Gato])
    enemigos.append(tipo_enemigo())

def mover_enemigos():
    for enemigo_actual in enemigos:
        enemigo_actual.mover_hacia(repartidor.x, repartidor.y)

def dibujar_enemigos():
    for enemigo_actual in enemigos:
        enemigo_actual.dibujar(pantalla)

def obtener_enemigo_mas_cercano(repartidor, enemigos):
    enemigo_mas_cercano = None
    distancia_mas_cercana = None

    centro_repartidor_x, centro_repartidor_y = repartidor.obtener_centro()

    for enemigo_actual in enemigos:
        centro_enemigo_x, centro_enemigo_y = enemigo_actual.obtener_centro()

        dx = centro_enemigo_x - centro_repartidor_x
        dy = centro_enemigo_y - centro_repartidor_y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia_mas_cercana is None or distancia < distancia_mas_cercana:
            distancia_mas_cercana = distancia
            enemigo_mas_cercano = enemigo_actual

    return enemigo_mas_cercano

def lanzar_pizza(repartidor, enemigo_objetivo):
    pizzas.append(Pizza(repartidor, enemigo_objetivo))
    sonido_disparo.play()

def mover_pizzas():
    global pizzas

    for pizza_actual in pizzas:
        pizza_actual.mover()

    pizzas = [
        pizza_actual
        for pizza_actual in pizzas
        if pizza_actual.esta_en_pantalla()
    ]

def dibujar_pizzas():
    for pizza_actual in pizzas:
        pizza_actual.dibujar(pantalla)

def detectar_colisiones_repartidor(tiempo_actual):
    global enemigos

    if repartidor.esta_invulnerable(tiempo_actual):
        return

    repartidor_rect = repartidor.obtener_rect()

    for enemigo_actual in enemigos:
        enemigo_rect = enemigo_actual.obtener_rect()

        if repartidor_rect.colliderect(enemigo_rect):
            repartidor.recibir_golpe(tiempo_actual)
            sonido_vida_perdida.play()
            enemigos = [
                otro_enemigo
                for otro_enemigo in enemigos
                if otro_enemigo != enemigo_actual
            ]
            break

def detectar_colisiones():
    global pizzas, enemigos, puntaje

    pizzas_sobrevivientes = []
    enemigos_sobrevivientes = list(enemigos)

    for pizza_actual in pizzas:
        pizza_choco = False

        for enemigo_actual in enemigos_sobrevivientes[:]:
            centro_pizza_x, centro_pizza_y = pizza_actual.obtener_centro()
            centro_enemigo_x, centro_enemigo_y = enemigo_actual.obtener_centro()

            dx = centro_pizza_x - centro_enemigo_x
            dy = centro_pizza_y - centro_enemigo_y
            distancia = (dx ** 2 + dy ** 2) ** 0.5

            if distancia < 30:
                enemigos_sobrevivientes.remove(enemigo_actual)
                pizza_choco = True
                puntaje += 1
                sonido_golpe.play()
                break

        if not pizza_choco:
            pizzas_sobrevivientes.append(pizza_actual)

    pizzas = pizzas_sobrevivientes
    enemigos = enemigos_sobrevivientes

def obtener_tiempo_sobrevivido(tiempo_actual):
    if estado_juego == "terminado":
        return tiempo_final

    return tiempo_actual - tiempo_inicio

def terminar_juego(tiempo_actual):
    global estado_juego, tiempo_final, musica_detendida

    estado_juego = "terminado"
    tiempo_final = tiempo_actual - tiempo_inicio

    if not musica_detendida:
        pygame.mixer.music.stop()
        musica_detendida = True
        
def actualizar_juego(tiempo_actual):
    global ultimo_enemigo_creado, ultimo_lanzamiento_pizza

    # Crear enemigos cada 2 segundos
    if tiempo_actual - ultimo_enemigo_creado >= tiempo_entre_enemigos:
        crear_enemigo()
        ultimo_enemigo_creado = tiempo_actual

    # Movimiento de todos los enemigos hacia el repartidor
    mover_enemigos()

    # Lanzamiento automático de pizzas
    if tiempo_actual - ultimo_lanzamiento_pizza >= tiempo_entre_pizzas:
        enemigo_mas_cercano = obtener_enemigo_mas_cercano(repartidor, enemigos)

        if enemigo_mas_cercano is not None:
            lanzar_pizza(repartidor, enemigo_mas_cercano)
            ultimo_lanzamiento_pizza = tiempo_actual

    mover_pizzas()
    detectar_colisiones()
    detectar_colisiones_repartidor(tiempo_actual)

    if repartidor.vidas <= 0:
        terminar_juego(tiempo_actual)
        
def dibujar_juego(tiempo_actual):
    pantalla.blit(fondo, (0, 0))

    repartidor.dibujar(pantalla, tiempo_actual)

    dibujar_enemigos()
    dibujar_pizzas()

    tiempo_sobrevivido = obtener_tiempo_sobrevivido(tiempo_actual)
    interfaz.dibujar_vidas(pantalla, repartidor.vidas)
    interfaz.dibujar_puntaje(pantalla, puntaje)
    interfaz.dibujar_cronometro(pantalla, tiempo_sobrevivido)

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    tiempo_actual = pygame.time.get_ticks()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            repartidor.manejar_tecla_presionada(evento.key)

        if evento.type == pygame.KEYUP:
            repartidor.manejar_tecla_soltada(evento.key)

    if estado_juego == "jugando":
        repartidor.mover()

        actualizar_juego(tiempo_actual)
        dibujar_juego(tiempo_actual)

    elif estado_juego == "terminado":
        repartidor.detener()
        interfaz.dibujar_pantalla_fin(
            pantalla,
            fondo,
            enemigos,
            pizzas,
            puntaje,
            tiempo_final
        )

    pygame.display.update()

pygame.quit()