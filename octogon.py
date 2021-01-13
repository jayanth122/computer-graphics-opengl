from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def lines():
        glBegin(GL_LINES)
        glColor3f(0.0,0.0,1.0)
        glVertex2f(0.3, 0.5)
        glVertex2f(0.5, 0.3)
        
        glColor3f(0.0,1.0,1.0)
        glVertex2f(-0.3, 0.5)
        glVertex2f(-0.5, 0.3)

        glColor3f(1.0,1.0,0.0)
        glVertex2f(-0.3, -0.5)
        glVertex2f(-0.5, -0.3)

        glColor3f(1.0,0.0,1.0)
        glVertex2f(0.3, -0.5)
        glVertex2f(0.5, -0.3)

        glColor3f(1.0,1.0,1.0)
        glVertex2f(0.5, 0.3)
        glVertex2f(0.5, -0.3)

        glVertex2f(0.3, 0.5)
        glVertex2f(-0.3, 0.5)

        glVertex2f(-0.5, -0.3)
        glVertex2f(-0.5, 0.3)

        glVertex2f(-0.3, -0.5)
        glVertex2f(0.3, -0.5)
        
        glEnd()

def points():
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
        
        glColor3f(0.0,0.0,0.0)
        glVertex2f(0.3, 0.5)
        glVertex2f(0.5, 0.3)
        
        glColor3f(1.0,0.0,0.0)
        glVertex2f(-0.3, 0.5)
        glVertex2f(-0.5, 0.3)

        glColor3f(0.0,1.0,0.0)
        glVertex2f(-0.3, -0.5)
        glVertex2f(-0.5, -0.3)

        glColor3f(0.0,0.0,1.0)
        glVertex2f(0.3, -0.5)
        glVertex2f(0.5, -0.3)
        glEnd()

        lines()
        
        glFlush()

def main():
        glutInit(sys.argv)#
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)#
        glutInitWindowSize(500,500)
        glutInitWindowPosition(50,50)
        glutCreateWindow("Octogon")
        glutDisplayFunc(points)
        init()
        glutMainLoop()
        
main()
