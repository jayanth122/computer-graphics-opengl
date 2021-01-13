from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glLineWidth(4)
    posx, posy = 1,1
    sides = 40
    radius = 2
    glBegin(GL_LINE_LOOP)
    c=0
    s=0
    for i in range(40):
        c= radius * cos(i*2*pi/sides) + posx
        s= radius * sin(i*2*pi/sides) + posy
        glVertex2f(c,s)
    glEnd()
    glBegin(GL_LINE_LOOP)
    c=0
    s=0
    for i in range(40):
        c= radius * cos(i*2*pi/sides) + (posx-radius)
        s= radius * sin(i*2*pi/sides) + posy
        glVertex2f(c,s)
    glEnd()
    glBegin(GL_LINE_LOOP)
    c=0
    s=0
    for i in range(40):
        c= radius * cos(i*2*pi/sides) + 0
        s= radius * sin(i*2*pi/sides) + (posy-radius)
        glVertex2f(c,s)
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    c=0
    s=0
    for i in range(15,21):
        c= radius * cos(i*2*pi/30) + posx
        s= radius * sin(i*2*pi/30) + posy
        glVertex2f(c,s)
    glEnd()
    glBegin(GL_POLYGON)
    c=0
    s=0
    for i in range(25,31):
        c= radius * cos(i*2*pi/30) + (posx-radius)
        s= radius * sin(i*2*pi/30) + posy
        glVertex2f(c,s)
    glEnd()
    glBegin(GL_POLYGON)
    c=0
    s=0
    for i in range(10,21):
        c= radius * cos(i*pi/30) + 0
        s= radius * sin(i*pi/30) + (posy-radius)
        glVertex2f(c,s)
    glEnd()
    glBegin(GL_POLYGON)
    c=0
    s=0
    list= [5,25,45]
    for i in list:
        c= 1 * cos(i*pi/30) + 0
        s= 1 * sin(i*pi/30) + 0.2
        glVertex2f(c,s)
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow('Plot Points')
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()