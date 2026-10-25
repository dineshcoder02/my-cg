from OpenGL.GL import *
from OpenGL.GLUT import *
import colorsys

h = float(input("ENTER HUE (0-360): "))
s = float(input("ENTER SATURATION (0-100): "))
v = float(input("ENTER VALUE (0-100): "))

r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)

print("\nRGB VALUE:")
print("R =", round(r * 255))
print("G =", round(g * 255))
print("B =", round(b * 255))


def display():
    glClearColor(r, g, b, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"HSV TO RGB")

glutDisplayFunc(display)
glutMainLoop()
