import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Base Scene Node
class SceneNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self):
        for child in self.children:
            child.draw()


# Group Node
class GroupNode(SceneNode):
    def draw(self):
        glPushMatrix()

        for child in self.children:
            child.draw()

        glPopMatrix()


# Object Node
class ObjectNode(SceneNode):
    def __init__(
        self, name, draw_function,
        x=0, y=0, z=0,
        sx=1, sy=1, sz=1
    ):
        super().__init__(name)

        self.draw_function = draw_function

        self.x, self.y, self.z = x, y, z
        self.sx, self.sy, self.sz = sx, sy, sz

    def draw(self):
        glPushMatrix()

        glTranslatef(self.x, self.y, self.z)
        glScalef(self.sx, self.sy, self.sz)

        self.draw_function()

        glPopMatrix()


# Camera Node
class CameraNode(SceneNode):
    def __init__(self, x, y, z):
        super().__init__("Camera")

        self.x, self.y, self.z = x, y, z

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        gluLookAt(
            self.x, self.y, self.z,
            0, 0, 0,
            0, 1, 0
        )


# Draw Cube
def draw_cube():
    vertices = [
        (-1, -1,  1), (1, -1,  1),
        ( 1,  1,  1), (-1,  1,  1),
        (-1, -1, -1), (1, -1, -1),
        ( 1,  1, -1), (-1,  1, -1)
    ]

    faces = [
        (0, 1, 2, 3),
        (1, 5, 6, 2),
        (5, 4, 7, 6),
        (4, 0, 3, 7),
        (3, 2, 6, 7),
        (4, 5, 1, 0)
    ]

    glBegin(GL_QUADS)

    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()


# Car parts
def draw_body():
    glColor3f(0.9, 0.05, 0.05)
    draw_cube()


def draw_roof():
    glColor3f(0.05, 0.2, 0.9)
    draw_cube()


def draw_window():
    glColor3f(0.1, 0.9, 0.95)
    draw_cube()


# Wheel
def draw_wheel():
    glColor3f(0.02, 0.02, 0.02)

    quadric = gluNewQuadric()

    glRotatef(90, 0, 1, 0)

    gluCylinder(quadric, 0.5, 0.5, 0.3, 30, 2)

    gluDisk(quadric, 0, 0.5, 30, 1)

    glTranslatef(0, 0, 0.3)

    gluDisk(quadric, 0, 0.5, 30, 1)

    gluDeleteQuadric(quadric)


# Headlight
def draw_headlight():
    glColor3f(1.0, 1.0, 0.1)

    quadric = gluNewQuadric()

    gluSphere(quadric, 0.25, 20, 20)

    gluDeleteQuadric(quadric)


# Create Car
def create_car():
    car = GroupNode("Car")

    car.add_child(ObjectNode(
        "Body", draw_body,
        0, 0, 0, 2.5, 0.6, 1
    ))

    car.add_child(ObjectNode(
        "Roof", draw_roof,
        0, 0.9, 0, 1.4, 0.5, 0.8
    ))

    car.add_child(ObjectNode(
        "Front Window", draw_window,
        0.7, 0.9, 0.82, 0.45, 0.3, 0.08
    ))

    car.add_child(ObjectNode(
        "Rear Window", draw_window,
        -0.7, 0.9, 0.82, 0.45, 0.3, 0.08
    ))

    car.add_child(ObjectNode(
        "Front Wheel", draw_wheel,
        1.5, -0.7, 1.05
    ))

    car.add_child(ObjectNode(
        "Rear Wheel", draw_wheel,
        -1.5, -0.7, 1.05
    ))

    car.add_child(ObjectNode(
        "Front Headlight", draw_headlight,
        2.6, 0.0, 0.55
    ))

    car.add_child(ObjectNode(
        "Rear Headlight", draw_headlight,
        -2.6, 0.0, 0.55
    ))

    return car


# Main
pygame.init()

display = (1000, 700)

pygame.display.set_mode(
    display,
    DOUBLEBUF | OPENGL
)

pygame.display.set_caption("Hierarchical Scene Graph - Toy Car")

glEnable(GL_DEPTH_TEST)
glClearColor(0.12, 0.12, 0.16, 1.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()

gluPerspective(
    45,
    display[0] / display[1],
    0.1,
    100.0
)

camera = CameraNode(7, 5, 10)
car = create_car()

clock = pygame.time.Clock()
angle = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    camera.draw()

    glPushMatrix()

    # Rotate around the centre of the car
    glTranslatef(0, 0, 0)
    glRotatef(angle, 0, 1, 0)

    car.draw()

    glPopMatrix()

    angle = (angle + 0.3) % 360

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
