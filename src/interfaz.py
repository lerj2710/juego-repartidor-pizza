import pygame


class Interfaz:
    def __init__(self):
        self.corazon_img = pygame.image.load("corazon.png")
        self.corazon_img = pygame.transform.scale(self.corazon_img, (32, 32))

        self.fuente = pygame.font.Font(None, 36)
        self.fuente_game_over = pygame.font.Font(None, 96)
        self.fuente_fin = pygame.font.Font(None, 48)

    def dibujar_vidas(self, pantalla, vidas):
        for numero_vida in range(vidas):
            pantalla.blit(self.corazon_img, (10 + numero_vida * 36, 10))

    def dibujar_puntaje(self, pantalla, puntaje):
        texto = self.fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
        pantalla.blit(texto, (650, 10))

    def formatear_tiempo(self, milisegundos):
        segundos_totales = milisegundos // 1000
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60
        return f"{minutos}:{segundos:02}"

    def dibujar_cronometro(self, pantalla, tiempo_sobrevivido):
        texto = self.fuente.render(
            f"Tiempo: {self.formatear_tiempo(tiempo_sobrevivido)}",
            True,
            (255, 255, 255)
        )
        rect_texto = texto.get_rect(center=(400, 25))
        pantalla.blit(texto, rect_texto)

    def dibujar_pantalla_fin(self, pantalla, fondo, enemigos, pizzas, puntaje, tiempo_final):
        pantalla.blit(fondo, (0, 0))

        for enemigo_actual in enemigos:
            enemigo_actual.dibujar(pantalla)

        for pizza_actual in pizzas:
            pizza_actual.dibujar(pantalla)

        texto_game_over = self.fuente_game_over.render("GAME OVER", True, (255, 80, 80))
        rect_game_over = texto_game_over.get_rect(center=(400, 220))
        pantalla.blit(texto_game_over, rect_game_over)

        texto_puntaje = self.fuente_fin.render(
            f"Puntaje final: {puntaje}",
            True,
            (255, 255, 255)
        )
        rect_puntaje = texto_puntaje.get_rect(center=(400, 310))
        pantalla.blit(texto_puntaje, rect_puntaje)

        texto_tiempo = self.fuente_fin.render(
            f"Tiempo sobrevivido: {self.formatear_tiempo(tiempo_final)}",
            True,
            (255, 255, 255)
        )
        rect_tiempo = texto_tiempo.get_rect(center=(400, 370))
        pantalla.blit(texto_tiempo, rect_tiempo)