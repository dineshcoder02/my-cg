import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def cube(x, y, z, sx, sy, sz, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(sx, sy, sz)
    glColor3fv(color)

    vertices = [
        (-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1),
        (-1,-1, 1), (1,-1, 1), (1,1, 1), (-1,1, 1)
    ]

    faces = [
        (0,1,2,3), (4,5,6,7), (0,1,5,4),
        (2,3,7,6), (1,2,6,5), (0,3,7,4)
    ]

    glBegin(GL_QUADS)
    for face in faces:
        for v in face:
            glVertex3fv(vertices[v])
    glEnd()
    glPopMatrix()


def wheel(x, z):
    glPushMatrix()
    glTranslatef(x, -0.55, z)
    glRotatef(90, 0, 1, 0)
    glColor3f(0.08, 0.08, 0.08)

    q = gluNewQuadric()
    gluCylinder(q, 0.38, 0.38, 0.18, 20, 1)
    gluDisk(q, 0, 0.38, 20, 1)

    glTranslatef(0, 0, 0.18)
    gluDisk(q, 0, 0.38, 20, 1)
    gluDeleteQuadric(q)

    glPopMatrix()


def car():
    # Main body
    cube(0, 0, 0, 2, 0.45, 0.8, (0.9, 0.05, 0.05))

    # Roof
    cube(-0.2, 0.75, 0, 1.1, 0.4, 0.65,
         (0.1, 0.3, 0.9))

    # Windows
    cube(-0.2, 0.78, 0.66, 0.85, 0.25, 0.03,
         (0.3, 0.9, 1.0))

    # Four wheels
    for x in [-1.25, 1.25]:
        for z in [-0.65, 0.65]:
            wheel(x, z)

    # Headlights
    cube(2.03, 0.05, -0.45, 0.08, 0.15, 0.18,
         (1.0, 1.0, 0.1))
    cube(2.03, 0.05, 0.45, 0.08, 0.15, 0.18,
         (1.0, 1.0, 0.1))


pygame.init()
display = (800, 600)

pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Simple 3D Toy Car")

glEnable(GL_DEPTH_TEST)
glClearColor(0.75, 0.85, 0.95, 1)

glMatrixMode(GL_PROJECTION)
gluPerspective(45, display[0] / display[1], 0.1, 50)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(6, 4, 7, 0, 0, 0, 0, 1, 0)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT or (
            event.type == KEYDOWN and event.key == K_ESCAPE
        ):
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    car()  # Draw car without rotation

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
