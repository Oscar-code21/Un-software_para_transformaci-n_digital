# Simulador Táctico y Balístico 

Este proyecto combina un **simulador táctico** (tipo mapa 2D con obstáculos) y un **simulador balístico** que calcula la trayectoria de un proyectil hacia un objetivo. Es interactivo y puedes elegir dónde disparar haciendo clic en el mapa. 

---

## **¿Qué hace este código?**

1. **Simulador Táctico**:
   - Muestra un mapa con obstáculos generados aleatoriamente.
   - Calcula la ruta más corta desde un punto inicial hasta un objetivo usando el algoritmo A\*.

2. **Simulador Balístico**:
   - Simula y grafica la trayectoria de un proyectil con factores como:
     - Gravedad 
     - Resistencia del aire 
     - Velocidad del viento 
   - La trayectoria cambia dependiendo de la distancia y dirección hacia el objetivo.

3. **Interacción**:
   - Haz clic en cualquier celda del mapa para disparar un proyectil hacia esa posición.

---

## **¿Qué necesitas para probarlo?**

- Python 3.7 o superior.
- Instalar estas librerías:
  ```bash
  pip install pygame numpy matplotlib scipy

  ```

  # ¿Como probarlo?

  1. Descarga el archivo simulador_integrado.py y ábrelo
 
  2. Ejecuta el código con:
 
     ```bash
     python simulador_integrado.py
     ```
  3. Se abrirá una ventana con un mapa táctico. Aquí puedes:
 
    - Ver el punto de inicio (marcado en verde).
    - Hacer clic en cualquier celda para seleccionar un objetivo.
    - Ver una gráfica de la trayectoria del proyectil calculada hacia ese objetivo


# Lo que te sale al ejecutarlo 
   - Un mapa táctico en 2D con obstáculos (celdas negras).
   - Al hacer clic en cualquier posición, se lanza un proyectil y se genera una gráfica mostrando su trayectoria.
   - Cada disparo tiene una trayectoria única basada en la distancia y dirección al objetivo.

