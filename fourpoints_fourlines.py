from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def fourlines():
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,1.0)
        glVertex2f(0.15, 0.11)
        glVertex2f(0.11, -0.12)
        
        glColor3f(0.0,1.0,1.0)
        glVertex2f(0.11, -0.12)
        glVertex2f(-0.5, -0.15)

        glColor3f(1.0,1.0,0.0)
        glVertex2f(-0.5, -0.15)
        glVertex2f(-0.3, 0.13)

        glColor3f(1.0,0.0,1.0)
        glVertex2f(0.15, 0.11)
        glVertex2f(-0.3, 0.13)
        glEnd()

def fourpoints():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
        
        glColor3f(0.0,0.0,0.0)
        glVertex2f(0.15, 0.11)
        glVertex2f(0.11, -0.12)
        
        glColor3f(1.0,0.0,0.0)
        glVertex2f(-0.5, -0.15)
        glVertex2f(-0.3, 0.13)
        glEnd()

        fourlines()
        
        glFlush()

def main():
        glutInit(sys.argv)#
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)#
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Four Points")
        glutDisplayFunc(fourpoints)
        init()
        glutMainLoop()
        
main()
