# Cubo en 3D con biblioteca turtle 

Este código usa la biblioteca `turtle` para dibujar un cubo en perspectiva isométrica en Python. 

## Requisitos

Asegúrate de tener `tkinter` instalado en Ubuntu. Si no lo tienes, instálalo con:

```bash
sudo apt install python3-tk
```

### Verificación en Python:
```bash
python3 -m tkinter
```
Si se abre una ventana, significa que `tkinter` está correctamente instalado.

## Ejecución del Código

1. Guarda el archivo `main.py`
2. Ejecútalo con:

```bash
python3 main.py
```

## Explicación del Código

El código utiliza la biblioteca `turtle` para dibujar un cubo en una vista isométrica utilizando solo puntos para formar líneas.

### Funciones Principales

#### `dibujar_punto(x, y)`
Esta función dibuja un punto en la posición `(x, y)` dentro del lienzo de `turtle`. 

1. `turtle.penup()`: Levanta el lápiz para moverse sin dibujar.
2. `turtle.goto(x, y)`: Mueve la tortuga a las coordenadas especificadas.
3. `turtle.pendown()`: Baja el lápiz para poder dibujar.
4. `turtle.dot(2, "black")`: Dibuja un punto negro con un tamaño de 2 píxeles.

#### `dibujar_linea(x1, y1, x2, y2, pasos=100)`
Esta función simula una línea entre los puntos `(x1, y1)` y `(x2, y2)` utilizando únicamente puntos.

1. `dx = (x2 - x1) / pasos`: Calcula la distancia en X entre los puntos dividida en pequeños incrementos.
2. `dy = (y2 - y1) / pasos`: Calcula la distancia en Y entre los puntos dividida en pequeños incrementos.
3. Un bucle `for` de 0 a `pasos` repite lo siguiente:
   - Calcula la posición del punto intermedio usando `x1 + i * dx` y `y1 + i * dy`.
   - Llama a `dibujar_punto(x, y)` para dibujar el punto en esa posición.

#### `dibujar_cubo()`
Esta función organiza los puntos y las líneas para formar un cubo.

1. Define una lista `puntos` con las coordenadas de los 8 vértices del cubo.
2. Define `aristas`, una lista de pares de índices que representan las líneas del cubo.
3. Un bucle `for` recorre `aristas` y usa `dibujar_linea()` para conectar los puntos.

### Flujo de Ejecución

1. `turtle.speed(0)`: Aumenta la velocidad de dibujo al máximo.
2. `turtle.hideturtle()`: Oculta la tortuga para no ver su movimiento.
3. `dibujar_cubo()`: Llama a la función para dibujar el cubo.
4. `turtle.done()`: Mantiene la ventana abierta hasta que el usuario la cierre.

Por: Israel L.L.
