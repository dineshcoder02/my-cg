from OpenGL.GL import *
from OpenGL.GLUT import *
import colorsys
import math

R = int(input("ENTER RED: "))
G = int(input("ENTER GREEN: "))
B = int(input("ENTER BLUE: "))

h, s, v = colorsys.rgb_to_hsv(R / 255, G / 255, B / 255)

print("HUE        :", round(h * 360, 2))
print("SATURATION :", round(s * 100, 2), "%")
print("VALUE      :", round(v * 100, 2), "%")


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    r = 0.8

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 1)
    glVertex2f(0, 0)

    for a in range(361):
        c = colorsys.hsv_to_rgb(a / 360, 1, 1)
        glColor3f(*c)

        glVertex2f(
            r * math.cos(math.radians(a)),
            r * math.sin(math.radians(a))
        )

    glEnd()

    x = r * s * math.cos(math.radians(h * 360))
    y = r * s * math.sin(math.radians(h * 360))

    glPointSize(10)
    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"RGB TO HSV Color Wheel")

glClearColor(0, 0, 0, 1)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-1, 1, -1, 1, -1, 1)

glutDisplayFunc(display)
glutMainLoop()
