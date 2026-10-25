from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xmin, ymin, xmax, ymax = 100, 100, 400, 300

polygon = [
    (50, 150),
    (200, 50),
    (450, 150),
    (350, 350),
    (150, 350)
]

intersection_points = []


def inside(p, edge):
    x, y = p

    return {
        "LEFT": x >= xmin,
        "RIGHT": x <= xmax,
        "BOTTOM": y >= ymin,
        "TOP": y <= ymax
    }[edge]


def intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    dx, dy = x2 - x1, y2 - y1

    if edge == "LEFT":
        x = xmin
        y = y1 + dy * (xmin - x1) / dx

    elif edge == "RIGHT":
        x = xmax
        y = y1 + dy * (xmax - x1) / dx

    elif edge == "BOTTOM":
        y = ymin
        x = x1 if dy == 0 else x1 + dx * (ymin - y1) / dy

    else:  # TOP
        y = ymax
        x = x1 if dy == 0 else x1 + dx * (ymax - y1) / dy

    return (x, y)


def clip_polygon(poly, edge):
    output = []

    for i in range(len(poly)):
        curr = poly[i]
        prev = poly[i - 1]

        curr_in = inside(curr, edge)
        prev_in = inside(prev, edge)

        if curr_in:
            if not prev_in:
                pt = intersection(prev, curr, edge)
                output.append(pt)
                intersection_points.append(pt)

            output.append(curr)

        elif prev_in:
            pt = intersection(prev, curr, edge)
            output.append(pt)
            intersection_points.append(pt)

    return output


def sutherland_hodgman(poly):
    for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
        poly = clip_polygon(poly, edge)

    return poly


clipped_polygon = sutherland_hodgman(polygon)


def drawAxes():
    glColor3f(0, 0, 0)
    glLineWidth(2)

    glBegin(GL_LINES)
    glVertex2f(0, 200)
    glVertex2f(500, 200)
    glVertex2f(250, 0)
    glVertex2f(250, 400)
    glEnd()


def drawPolygon(poly, r, g, b):
    if not poly:
        return

    glColor3f(r, g, b)

    glBegin(GL_LINE_LOOP)
    for p in poly:
        glVertex2f(*p)
    glEnd()


def drawPoints():
    glPointSize(8)
    glColor3f(0, 0, 0)

    glBegin(GL_POINTS)
    for p in intersection_points:
        glVertex2f(*p)
    glEnd()


def drawText(x, y, text):
    glColor3f(0, 0, 0)
    glRasterPos2f(x + 5, y + 5)

    for ch in text:
        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_12, ord(ch)
        )


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    drawAxes()

    # Draw clipping window in blue
    glColor3f(0, 0, 1)

    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()

    # Draw original polygon in red
    drawPolygon(polygon, 1, 0, 0)

    # Draw clipped polygon in green
    drawPolygon(clipped_polygon, 0, 1, 0)

    # Draw intersection points
    drawPoints()

    # Label intersection points
    for p in intersection_points:
        drawText(
            p[0], p[1],
            f"({int(p[0])},{int(p[1])})"
        )

    glFlush()


def init():
    glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 400)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Sutherland Hodgman Polygon Clipping")

init()
glutDisplayFunc(display)
glutMainLoop()
