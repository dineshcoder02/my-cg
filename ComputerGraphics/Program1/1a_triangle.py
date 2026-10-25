from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

n = int(input("ENTER THE NUMBER OF VERTICES: "))
points = []

for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

print("\n1. TRANSLATION")
print("2. ROTATION")
print("3. SCALING")

choice = int(input("ENTER YOUR CHOICE: "))

tx = ty = angle = sx = sy = 0.0

if choice == 1:
    tx = float(input("ENTER TRANSLATION IN X: "))
    ty = float(input("ENTER TRANSLATION IN Y: "))
elif choice == 2:
    angle = float(input("ENTER THE ROTATIONAL ANGLE: "))
elif choice == 3:
    sx = float(input("ENTER THE SCALING FACTOR IN X: "))
    sy = float(input("ENTER THE SCALING FACTOR IN Y: "))
else:
    print("INVALID CHOICE. NO TRANSFORMATION WILL BE APPLIED.")


def drawText(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))


def drawAxes():
    glLoadIdentity()
    glLineWidth(2.0)
    glColor3f(0.5, 0.5, 0.5)

    glBegin(GL_LINES)
    glVertex2f(-20, 0)
    glVertex2f(20, 0)
    glVertex2f(0, -20)
    glVertex2f(0, 20)
    glEnd()

    drawText(18.5, -1.2, "X")
    drawText(0.5, 18.5, "Y")


def drawPointsAndLabels():
    glPointSize(8.0)

    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()

    for x, y in points:
        label = f"({x:.1f}, {y:.1f})"
        drawText(x + 0.5, y + 0.5, label)


def drawPolygon():
    glLineWidth(2.0)

    glBegin(GL_LINE_LOOP)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    drawAxes()

    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    drawPolygon()
    drawPointsAndLabels()

    glLoadIdentity()

    if choice == 1:
        glTranslatef(tx, ty, 0)
    elif choice == 2:
        glRotatef(angle, 0, 0, 1)
    elif choice == 3:
        glScalef(sx, sy, 1)

    glColor3f(0.0, 0.0, 1.0)
    drawPolygon()
    drawPointsAndLabels()

    glFlush()


def init():
    glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-20, 20, -20, 20)

    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)

glutCreateWindow(b"2D Geometric Transformation - OpenGL")

init()
glutDisplayFunc(display)
glutMainLoop()
