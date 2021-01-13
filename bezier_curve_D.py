from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
    glClearColor(1.0,1.0,1.0,0.0);
    glColor3f(1.0,0.0,0.0);
    glPointSize(5.0);
    gluOrtho2D(0.0,250.0,0.0,300.0);

def bezierCoefficients(n,c):
    i=0
    for k in range(n):
        c[k]=1;
        for i in range(n,k,-1):
            c[k]=c[k]*i;
        for i in range((n-k),1,-1):
            c[k]=c[k]/i;

def stline():
    glColor3f(0.0,0.0,1.0);
    glLineWidth(5.0);
    glBegin(GL_LINES);
    glVertex2f(100.0,250.0);
    glVertex2f(107,100);
    glEnd();

def display():
    cp =[[0,150],[100,200],[200,50],[300,300]];
    c = [0,0,0,0]
    n=3;
    bezierCoefficients(n,c);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0,0.0,1.0);
    glLineWidth(5.0);
    glBegin(GL_LINE_STRIP);

    for v in range(100):
        x=100;y=100;
        u = v/100
        for k in range(4):
            blend=c[k]*pow(u,k)*pow(1-u,n-k);

            x+=cp[k][0]*blend;
            y+=cp[k][1]*blend;
        glVertex2f(x,y);

    glEnd();
    stline();
    glFlush();

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(650,650)
    #glutInitWindowPosition(100, 100)
    glutCreateWindow("Letter D using Bezier Curve");
    init();
    glutDisplayFunc(display)
    #glutReshapeFunc(resize);
    #glutKeyboardFunc(keyboard);
    glutMainLoop()

main()