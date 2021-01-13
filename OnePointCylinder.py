from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys



def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLineWidth(2.5);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(-2.0, 0.0, -10.0)
    posx, posy = -0.001, 0.001
    sides = 100000
    r1 = 1
    glBegin(GL_POLYGON)
    c1 = 0
    s1 = 0
    c2 = 0
    s2 = 0
    for i in range(150000):
        glColor3f(1.0, 0.0, 0.0)
        c1 = r1 * cos(i * 2 * pi / sides) + posx
        s1 = r1 * sin(i * 2 * pi / sides) + posy
        glVertex3f(c1, s1, -15)
        glColor3f(1.0, 1.0, 0.0)
        c2 = r1 * cos(i * 2 * pi / sides) + posx
        s2 = r1 * sin(i * 2 * pi / sides) + posy
        glVertex3f(c2, s2, 5)

    glEnd()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(750, 750)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("One point cylinder")
    glutDisplayFunc(draw)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective(75.0, 1.0, 1.0, 75.0)

    #gluPerspective(45.0, 1, 0.1, 25.0)
    #glRotatef(45,1,0,0)

    #gluPerspective(75.0, 1, 0.1, 25.0)
     
    #glRotatef(45,1,0,0)
    #glRotatef(45,0,1,0)
    
    init()
    glutMainLoop()


main()
