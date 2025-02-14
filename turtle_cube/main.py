import turtle

def dibujar_punto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(2, "black")

def dibujar_linea(x1, y1, x2, y2, pasos=100):
    dx = (x2 - x1) / pasos
    dy = (y2 - y1) / pasos
    for i in range(pasos + 1):
        dibujar_punto(x1 + i * dx, y1 + i * dy)

def dibujar_cubo():
    puntos = [
        (-50, -50), (50, -50), (50, 50), (-50, 50),
        (-30, -30), (70, -30), (70, 70), (-30, 70)
    ]
    
    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    for arista in aristas:
        dibujar_linea(puntos[arista[0]][0], puntos[arista[0]][1], puntos[arista[1]][0], puntos[arista[1]][1])

turtle.speed(0)
turtle.hideturtle()

dibujar_cubo()

turtle.done()
