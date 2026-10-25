from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xmin, ymin = 100, 100
xmax, ymax = 400, 300

x1, y1 = 50, 50
x2, y2 = 450, 350

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

accept = False
cx1, cy1, cx2, cy2 = x1, y1, x2, y2


def computeCode(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


def cohenSutherland():
    global accept, cx1, cy1, cx2, cy2

    x1_, y1_ = x1, y1
    x2_, y2_ = x2, y2

    code1 = computeCode(x1_, y1_)
    code2 = computeCode(x2_, y2_)

    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif (code1 & code2) != 0:
            break

        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1_ + (x2_ - x1_) * (ymax - y1_) / (y2_ - y1_)
                y = ymax

            elif code_out & BOTTOM:
                x = x1_ + (x2_ - x1_) * (ymin - y1_) / (y2_ - y1_)
                y = ymin

            elif code_out & RIGHT:
                y = y1_ + (y2_ - y1_) * (xmax - x1_) / (x2_ - x1_)
                x = xmax

            elif code_out & LEFT:
                y = y1_ + (y2_ - y1_) * (xmin - x1_) / (x2_ - x1_)
                x = xmin

            if code_out == code1:
                x1_, y1_ = x, y
                code1 = computeCode(x1_, y1_)
            else:
                x2_, y2_ = x, y
                code2 = computeCode(x2_, y2_)

    if accept:
        cx1, cy1, cx2, cy2 = x1_, y1_, x2_, y2_


def drawLine(xa, ya, xb, yb):
    glBegin(GL_LINES)
    glVertex2f(xa, ya)
    glVertex2f(xb, yb)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Clipping window
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

    # Original line in red
    glColor3f(1, 0, 0)
    drawLine(x1, y1, x2, y2)

    # Clipped line in green
    if accept:
        glColor3f(0, 1, 0)
        drawLine(cx1, cy1, cx2, cy2)

    glFlush()


def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 400)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


cohenSutherland()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 500)
glutCreateWindow(b"Cohen Sutherland Line Clipping")

init()
glutDisplayFunc(display)
glutMainLoop()
