from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys


def subtract(a, b):
    return (
        a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2]
    )


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    )


def normalize(a):
    length = math.sqrt(
        a[0] * a[0] +
        a[1] * a[1] +
        a[2] * a[2]
    )

    if length == 0:
        return (0, 0, 0)

    return (
        a[0] / length,
        a[1] / length,
        a[2] / length
    )


def dot(a, b):
    return (
        a[0] * b[0] +
        a[1] * b[1] +
        a[2] * b[2]
    )


vertices = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1)
]


faces = [
    (0, 3, 2, 1),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (1, 2, 6, 5),
    (0, 4, 7, 3)
]


base_color = (1.0, 1.0, 1.0)
light_direction = normalize((1, 6, 2))


def calculate_intensity(face):
    p1 = vertices[face[0]]
    p2 = vertices[face[1]]
    p3 = vertices[face[2]]

    A = subtract(p2, p1)
    B = subtract(p3, p1)

    N = cross(A, B)
    N = normalize(N)

    intensity = dot(N, light_direction)

    if intensity < 0:
        intensity = 0

    return intensity


def draw_cube():
    for face in faces:
        intensity = calculate_intensity(face)

        R = base_color[0] * intensity
        G = base_color[1] * intensity
        B = base_color[2] * intensity

        glColor3f(R, G, B)

        glBegin(GL_QUADS)

        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])

        glEnd()


angle = 0


def display():
    global angle

    glClear(
        GL_COLOR_BUFFER_BIT |
        GL_DEPTH_BUFFER_BIT
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(
        3, 3, 4,
        0.5, 0.5, 0.5,
        0, 1, 0
    )

    # Rotate around the centre of the cube
    glTranslatef(0.5, 0.5, 0.5)
    glRotatef(angle, 1, 1, 0)
    glTranslatef(-0.5, -0.5, -0.5)

    draw_cube()

    glutSwapBuffers()


def update(value):
    global angle

    angle += 1

    if angle >= 360:
        angle = 0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(
        45,
        width / float(height),
        0.1,
        100
    )

    glMatrixMode(GL_MODELVIEW)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)


def main():
    glutInit(sys.argv)

    glutInitDisplayMode(
        GLUT_DOUBLE |
        GLUT_RGB |
        GLUT_DEPTH
    )

    glutInitWindowSize(800, 600)

    glutCreateWindow(
        b"Flat Shading - Same Colour Cube"
    )

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutTimerFunc(0, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
