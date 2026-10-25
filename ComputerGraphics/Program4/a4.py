from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

Q = None


# Draw a cylinder between two points
def bar(a, b, r=0.035):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dz = b[2] - a[2]
    length = math.sqrt(dx*dx + dy*dy + dz*dz)

    if length < 1e-8:
        return

    glPushMatrix()
    glTranslatef(*a)

    # Align cylinder along the direction from a to b
    vx, vy, vz = -dy, dx, 0
    dot = max(-1.0, min(1.0, dz / length))
    angle = math.degrees(math.acos(dot))

    if abs(vx) > 1e-8 or abs(vy) > 1e-8:
        glRotatef(angle, vx, vy, vz)
    elif dz < 0:
        glRotatef(180, 1, 0, 0)

    gluCylinder(Q, r, r, length, 12, 2)
    glPopMatrix()


# Draw a wheel with tyre, rim and spokes
def wheel(x, y=0):
    glPushMatrix()
    glTranslatef(x, y, 0)

    # Outer tyre
    glColor3f(0.08, 0.08, 0.08)
    glutSolidTorus(0.07, 0.58, 12, 48)

    # Inner rim
    glColor3f(0.7, 0.7, 0.7)
    glutWireTorus(0.018, 0.53, 8, 48)

    # Sixteen spokes
    glColor3f(0.45, 0.45, 0.45)
    glBegin(GL_LINES)
    for i in range(16):
        a = 2 * math.pi * i / 16
        glVertex3f(0, 0, 0.015)
        glVertex3f(0.53 * math.cos(a),
                   0.53 * math.sin(a), 0.015)
    glEnd()

    # Hub
    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0, 0, 0.025)
    glutSolidSphere(0.065, 16, 16)
    glPopMatrix()

    glPopMatrix()


# Draw the bicycle frame and components
def draw_bicycle():
    rear = (-1.4, 0.0, 0)
    front = (1.4, 0.0, 0)
    crank = (0.0, 0.0, 0)
    seat_joint = (-0.35, 0.85, 0)
    head_joint = (0.85, 0.85, 0)

    # Wheels (stationary)
    wheel(-1.4)
    wheel(1.4)

    # Main frame
    glColor3f(0.0, 0.45, 0.08)
    bar(rear, seat_joint, 0.045)
    bar(seat_joint, head_joint, 0.045)
    bar(head_joint, front, 0.045)
    bar(rear, crank, 0.045)
    bar(crank, seat_joint, 0.045)
    bar(crank, head_joint, 0.045)

    # Seat post
    bar(seat_joint, (-0.35, 1.18, 0), 0.035)

    # Seat
    glColor3f(0.08, 0.08, 0.08)
    bar((-0.62, 1.2, 0), (-0.12, 1.2, 0), 0.085)

    # Handlebar stem
    bar(head_joint, (0.98, 1.15, 0), 0.04)

    # Handlebar
    glColor3f(0.12, 0.12, 0.12)
    bar((0.78, 1.15, 0), (1.23, 1.15, 0), 0.045)

    # Rubber handle grips
    glColor3f(0.02, 0.02, 0.02)
    bar((0.74, 1.15, 0), (0.82, 1.15, 0), 0.06)
    bar((1.19, 1.15, 0), (1.27, 1.15, 0), 0.06)

    # Chain: two straight chain runs
    glColor3f(0.45, 0.45, 0.45)
    bar(rear, crank, 0.018)
    bar(crank, rear, 0.018)

    # Crank axle
    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(*crank)
    glutSolidSphere(0.09, 16, 16)
    glPopMatrix()

    # Crank arms and pedals
    glColor3f(0.75, 0.2, 0.0)
    bar((0, 0, 0.04), (0.28, -0.25, 0.04), 0.035)
    bar((0, 0, -0.04), (-0.28, 0.25, -0.04), 0.035)

    glColor3f(0.1, 0.1, 0.1)
    bar((0.18, -0.25, 0.04),
        (0.38, -0.25, 0.04), 0.045)
    bar((-0.38, 0.25, -0.04),
        (-0.18, 0.25, -0.04), 0.045)


# Display the stationary bicycle
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(
        0, 0.45, 7,
        0, 0.45, 0,
        0, 1, 0
    )

    draw_bicycle()
    glutSwapBuffers()


# Initialize OpenGL
def init():
    global Q

    glClearColor(1, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)

    Q = gluNewQuadric()
    gluQuadricNormals(Q, GLU_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 1, 30)

    glMatrixMode(GL_MODELVIEW)


# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Stationary Bicycle")

    init()
    glutDisplayFunc(display)

    # No idle callback: nothing rotates or animates
    glutMainLoop()


if __name__ == "__main__":
    main()
