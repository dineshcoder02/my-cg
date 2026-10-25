import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glClearColor(0.1, 0.1, 0.1, 1.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, display[0] / display[1], 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -7.0)


def draw_triangles():

    # Triangle 1 - Dark Blue
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.4)
    glVertex3f(-3.0, 1.5, 0.0)
    glVertex3f(-1.0, 1.5, 0.0)
    glVertex3f(-2.0, 3.0, 0.0)
    glEnd()

    # Triangle 2 - Medium Blue
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.7)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()

    # Triangle 3 - Light Blue
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, 1.5, 0.0)
    glVertex3f(3.0, 1.5, 0.0)
    glVertex3f(2.0, 3.0, 0.0)
    glEnd()


running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_triangles()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
