from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time


W, H = 900, 700


x = 0.0
y = 0.0
vy = 0.0
t = 0.0

action = "IDLE"
last = time.time()



def line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()



def limb(x, y, angle, l1, l2):
    a1 = math.radians(angle)

    
    mx = x + l1 * math.cos(a1)
    my = y + l1 * math.sin(a1)

    
    a2 = math.radians(angle + 25)
    ex = mx + l2 * math.cos(a2)
    ey = my + l2 * math.sin(a2)

    
    line(x, y, mx, my)
    line(mx, my, ex, ey)



def skeleton():
    
    s = math.sin(t * 8) * 25 if action == "WALK" else 0

    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(4)

    
    glBegin(GL_LINE_LOOP)
    for i in range(40):
        a = 2 * math.pi * i / 40
        hx = 0.4 * math.cos(a)
        hy = 3.5 + 0.4 * math.sin(a)
        glVertex2f(hx, hy)
    glEnd()

    # Neck and body
    line(0, 3.1, 0, 1.3)

    # Shoulders
    line(-0.7, 2.7, 0.7, 2.7)

    # Ribs
    line(-0.45, 2.3, 0.45, 2.3)
    line(-0.4, 1.9, 0.4, 1.9)

    # Pelvis
    line(-0.5, 1.3, 0.5, 1.3)

    # Arms
    limb(-0.7, 2.7, -140 + s, 0.65, 0.55)
    limb(0.7, 2.7, -40 - s, 0.65, 0.55)

    # Legs
    limb(-0.25, 1.3, -90 + s, 0.75, 0.65)
    limb(0.25, 1.3, -90 - s, 0.75, 0.65)

    glLineWidth(1)



def draw_text(xpos, ypos, text):
    glRasterPos2f(xpos, ypos)

    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))



def draw_buttons():
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, W, 0, H)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # WALK button
    glColor3f(0.1, 0.6, 0.2)
    glRectf(20, 20, 120, 60)

    # JUMP button
    glColor3f(0.1, 0.3, 0.8)
    glRectf(135, 20, 235, 60)

    # Button labels
    glColor3f(1.0, 1.0, 1.0)
    draw_text(42, 34, "WALK")
    draw_text(157, 34, "JUMP")

    # Restore previous matrices
    glPopMatrix()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)



def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the skeleton using world coordinates
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(x, y, 0)

    skeleton()

    # Draw buttons separately so they do not move
    draw_buttons()

    glutSwapBuffers()



def mouse(button, state, mx, my):
    global action, vy

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        # Convert mouse Y from top-down to bottom-up
        my = H - my

        # WALK button
        if 20 <= mx <= 120 and 20 <= my <= 60:
            action = "WALK"

        # JUMP button
        elif 135 <= mx <= 235 and 20 <= my <= 60:
            if y <= 0:
                action = "JUMP"
                vy = 7.0



def update():
    global x, y, vy, t, last, action

    now = time.time()
    dt = min(now - last, 0.05)
    last = now

    # Update animation time
    t += dt

    # Walking movement
    if action == "WALK":
        x += 0.7 * dt

        # Return to the left after leaving the screen
        if x > 7:
            x = -7

    # Jumping movement
    if action == "JUMP":
        vy -= 15 * dt
        y += vy * dt

        # Stop at the ground
        if y <= 0:
            y = 0
            vy = 0
            action = "IDLE"

    
    glutPostRedisplay()



def init():
    glClearColor(0.05, 0.05, 0.1, 1.0)

    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-8, 8, -4, 9)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def main():
    global last

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(100, 50)
    glutCreateWindow(b"2D Skeleton Animation")

    init()
    last = time.time()

   
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutIdleFunc(update)

    glutMainLoop()



main()
