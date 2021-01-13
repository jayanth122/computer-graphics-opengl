import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *


def bezierCoefficients(n,c):
        i=0
        for k in range(0,n):
        
                c[k]=1;
                for i in range(n,k,-1):
                    c[k]=c[k]*i;
                for i in range((n-k),1,-1):
                    c[k]=c[k]/i;

def display():

        cp = [[10,10],[100,200],[200,50],[300,300]]; 
        c=[0,0,0,0];
        k=0;n=3;
        x=y=u=blend=0.00;
        #int cp[4][2]={{10,10},{100,200},{200,50},{300,300}};
        #int c[4],k,n=3;
        #float x,y,u,blend;
        bezierCoefficients(n,c);
        glClear(GL_COLOR_BUFFER_BIT);
        glColor3f(1.0,0.0,0.0);
        glLineWidth(5.0);
        glBegin(GL_LINE_STRIP);

        
        for ut in range(0,100,1): # (u=0;u<1.0;u+=0.01)
                x=0;y=0;
                u=ut/100;
                for k in range(0,4):# (k=0;k<4;k++)
                        blend=c[k]*pow(u,k)*pow(1-u,n-k);
                        x+=cp[k][0]*blend;
                        y+=cp[k][1]*blend;
        
                glVertex2f(x,y);
        glEnd();
        glFlush();


def myinit():
        glClearColor(1.0,1.0,1.0,1.0);
        glColor3f(1.0,0.0,0.0);
        glPointSize(5.0);
        gluOrtho2D(0.0,250.0,0.0,300.0);


def main():
        glutInit(sys.argv);
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
        glutInitWindowSize(600,600);

        glutCreateWindow("Bezier Curve");
        glutDisplayFunc(display);
        myinit();

        glutMainLoop();

main()
