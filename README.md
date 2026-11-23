# 🍕 Pizza Survivor

**Pizza Survivor** es un videojuego arcade de acción y supervivencia en 2D desarrollado en Python utilizando la librería **Pygame**. En este juego, controlas a un repartidor de pizzas que debe sobrevivir el mayor tiempo posible esquivando oleadas de animales callejeros mientras lanza pizzas automáticamente para defenderse.

---

## 🎮 Características del Juego

* **Mecánica estilo *Survivor*:** El personaje dispara pizzas de forma automática cada 3 segundos apuntando directamente al enemigo más cercano.
* **Enemigos dinámicos:** Perros y gatos aparecen continuamente cada 2 segundos y persiguen al repartidor por toda la pantalla.
* **Sistema de vidas e invulnerabilidad:** El repartidor cuenta con un sistema de vidas y un breve período de invulnerabilidad tras recibir un golpe.
* **Interfaz en tiempo real (HUD):** Visualización de vidas restantes (corazones), puntaje acumulado por enemigos derrotados y cronómetro de supervivencia.
* **Audio envolvente:** Incluye música de fondo en bucle y efectos de sonido para disparos, impactos y pérdida de vidas.
* **Pantalla de Game Over:** Muestra el resumen final con la puntuación total y el tiempo sobrevivido.

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
Asegúrate de tener instalado **Python 3.x** y la librería **Pygame**.

### Instalación de dependencias
Ejecuta el siguiente comando en tu terminal para instalar Pygame:

```bash
pip install pygame
```

---

## 📂 Estructura del Proyecto

Para que el juego funcione correctamente, asegúrate de mantener la siguiente estructura de archivos y recursos (sprites y audios) en el directorio raíz:

```text
pizza-survivor/
│
├── main.py              # Archivo principal que ejecuta el bucle del juego
├── prueba.py            # Prototipo inicial de movimiento y colisiones básicas
├── repartidor.py        # Clase del jugador (movimiento, vidas, renderizado)
├── perro.py             # Clase del enemigo tipo Perro
├── gato.py              # Clase del enemigo tipo Gato
├── pizza.py             # Clase del proyectil (pizza) y su trayectoria
├── interfaz.py          # Clase encargada del HUD y pantalla de Game Over
│
├── Assets (Imágenes):
│   ├── pizza.png        # Ícono del juego y sprite del proyectil
│   ├── fondo.png        # Imagen de fondo del escenario (800x600)
│   ├── corazon.png      # Ícono de vida
│   └── repartidor.png   # Sprite del jugador
│
└── Assets (Audio):
    ├── MusicaFondo.mp3  # Música ambiental en bucle
    ├── disparo.mp3      # Sonido al lanzar una pizza
    ├── golpe.mp3        # Sonido al impactar a un enemigo
    └── vida_perdida.mp3 # Sonido al recibir daño
```

*(Nota: Las clases `Perro`, `Gato`, `Pizza`, `Repartidor` e `Interfaz` se importan desde sus respectivos módulos en `main.py`).*

---

## 🚀 Cómo Jugar

1. Clona o descarga este repositorio en tu máquina local.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python main.py
```

### Controles
* **Flechas de dirección (`↑`, `↓`, `←`, `→`):** Mover al repartidor por el escenario.
* **Ataque:** Automático (el repartidor lanza una pizza cada 3 segundos al enemigo más próximo).

---

## 🧪 Notas de Desarrollo

* El repositorio incluye el archivo `prueba.py`, el cual contiene un prototipo temprano utilizado para probar la carga de sprites, los límites de la pantalla (`800x600`) y el algoritmo básico de persecución vectorial del enemigo.