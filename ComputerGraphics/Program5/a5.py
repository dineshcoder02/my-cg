from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initialize variables
Q = gluNewQuadric()
angle = 0


# Draw a cylindrical rod between two points
def bar(a, b, r=0.06):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dz = b[2] - a[2]

    L = math.sqrt(dx * dx + dy * dy + dz * dz)

    if L == 0:
        return

    glPushMatrix()
    glTranslatef(*a)

    # Align the cylinder's Z-axis with the rod direction
    if abs(dx) > 1e-8 or abs(dy) > 1e-8:
        angle_deg = math.degrees(math.acos(max(-1.0, min(1.0, dz / L))))
        glRotatef(angle_deg, -dy, dx, 0)
    elif dz < 0:
        glRotatef(180, 1, 0, 0)

    gluCylinder(Q, r, r, L, 12, 1)
    glPopMatrix()


# Draw a wheel with a tyre and six spokes
def wheel(x):
    glPushMatrix()
    glTranslatef(x, 0, 0)
    glRotatef(angle, 0, 0, 1)

    # Tyre
    glColor3f(0.1, 0.1, 0.1)
    glutSolidTorus(0.1, 1.0, 12, 24)

    # Spokes
    glColor3f(0.7, 0.7, 0.7)

    for i in range(6):
        a = i * math.pi / 6
        c = math.cos(a)
        s = math.sin(a)

        bar((-c, -s, 0), (c, s, 0), 0.02)

    glPopMatrix()


# Draw the complete bicycle
def draw_bicycle():

    # Wheels
    wheel(-1.2)
    wheel(1.2)

    # Green frame
    glColor3f(0.0, 0.5, 0.0)

    bar((-1.2, 0, 0), (0, 1, 0))
    bar((0, 1, 0), (1.2, 0, 0))
    bar((-1.2, 0, 0), (1.2, 0, 0))

    # Seat support and seat
    bar((0, 1, 0), (0, 1.4, 0))
    bar((-0.25, 1.4, 0), (0.25, 1.4, 0), 0.08)

    # Handle support and handlebar
    bar((1.2, 0, 0), (1.2, 0.8, 0))
    bar((1.2, 0.8, 0), (1.5, 0.8, 0))

    # Pedal crank and pedal
    glColor3f(0.8, 0.2, 0.0)

    bar((0, 1, 0), (0, 0.6, 0), 0.04)
    bar((-0.25, 0.6, 0), (0.25, 0.6, 0), 0.04)


# Display and animate the bicycle
def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set the camera
    gluLookAt(
        0, 0, 7,
        0, 0, 0,
        0, 1, 0
    )

    # Draw bicycle
    draw_bicycle()

    # Display the frame
    glutSwapBuffers()

    # Rotate the wheels
    angle = (angle + 2) % 360


# Initialize OpenGL settings
def init():
    glClearColor(1, 1, 1, 1)

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, 800 / 600, 1, 20)

    glMatrixMode(GL_MODELVIEW)


# Main function
def main():
    glutInit()

    glutInitDisplayMode(
        GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
    )

    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"OpenGL Bicycle")

    init()

    glutDisplayFunc(display)
    glutIdleFunc(display)

    glutMainLoop()


# Run the program
main()
