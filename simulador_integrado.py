import pygame
import heapq
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# INICIAR PYGAME
pygame.init()
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador Táctico y Balístico")

# Generar Mapa con obstáculos
np.random.seed(0)
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])  # 0 = libre, 1 = obstáculo

# Posiciones de inicio y fin
start = (1, 1)

# Algoritmo A* para encontrar el camino más corto
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and grid[neighbor] == 0:
                new_cost = cost_so_far[current] + 1

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(end, neighbor)
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

    path = []
    current = end
    while current:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

# Simulador Balístico
def simulador_balistico(v0, angle, air_resistance, wind_speed, distance):
    g = 9.81  # Gravedad
    theta = np.radians(angle)  # Convertir ángulo a radianes

    # Función de ecuaciones diferenciales
    def equations(t, y):
        x, vx, y, vy = y
        v = np.sqrt(vx**2 + vy**2)  # Magnitud de la velocidad
        drag_x = -air_resistance * v * vx + wind_speed  # Resistencia y viento
        drag_y = -air_resistance * v * vy - g  # Resistencia y gravedad
        return [vx, drag_x, vy, drag_y]

    # Condiciones iniciales
    y0 = [0, v0 * np.cos(theta), 0, v0 * np.sin(theta)]

    # Resolver ODE
    t_span = (0, distance / v0 * 2)  # Ajustar tiempo de simulación según distancia
    t_eval = np.linspace(0, t_span[1], 100)
    sol = solve_ivp(equations, t_span, y0, t_eval=t_eval)

    # Graficar
    plt.figure()
    plt.plot(sol.y[0], sol.y[2], label="Trayectoria del proyectil")
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.legend()
    plt.grid()
    plt.title(f"Trayectoria hacia objetivo ({distance}m)")
    plt.show()

# Bucle principal
running = True
while running:
    Screen.fill(WHITE)

    # Dibujar cuadrícula y obstáculos
    for i in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(Screen, BLACK if grid[i, c] else WHITE, rect, 0 if grid[i, c] else 1)

    # Dibujar inicio
    pygame.draw.rect(Screen, GREEN, (start[1] * GRID_SIZE, start[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar clic del mouse para disparar un proyectil
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            target_col = mouse_x // GRID_SIZE
            target_row = mouse_y // GRID_SIZE

            # Calcular distancia y dirección hacia el objetivo
            distance = np.sqrt((target_row - start[0])**2 + (target_col - start[1])**2) * GRID_SIZE
            angle = np.degrees(np.arctan2(target_row - start[0], target_col - start[1]))
            print(f"Lanzando proyectil hacia ({target_row}, {target_col}) - Distancia: {distance:.2f}m")

            # Simular trayectoria balística
            simulador_balistico(v0=50, angle=angle, air_resistance=0.1, wind_speed=2, distance=distance)

pygame.quit()
