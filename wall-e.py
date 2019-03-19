from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import numpy as np
from math import *

def draw_circle(r,xc,xy,R,G,B):
    glBegin(GL_POLYGON)
    glColor3f(R,G,B)
    for theta in np.arange (0,2*pi,0.001):
        
         x=xc+r*cos(theta)
         y=xy+r*sin(theta)
         glVertex(x,y)  
    glEnd()
def draw_circleb(r,xc,xy,R,G,B):
    glBegin(GL_POINTS)
    glColor3f(R,G,B)
    for theta in np.arange (0,2*pi,0.001):
        
         x=xc+r*cos(theta)
         y=xy+r*sin(theta)
         glVertex(x,y)  
    glEnd()    

def draw():
      glClearColor(1, 1, 1, 1.0)
      glClear(GL_COLOR_BUFFER_BIT)
      glBegin(GL_LINES)
      glColor3f(1,0.9,0.3)
      glVertex(-1,0)
      glVertex(1,0)
      glVertex(0,1)
      glVertex(0,-1)
      glEnd()
      
      glBegin(GL_POLYGON)#body
      glColor3f(1,0.9,0.3)
      glVertex(0.2,0.2)
      glVertex(-0.2,0.2)
      glVertex(-0.2,-0.2)
      glVertex(0.2,-0.2)
      glEnd()
      
      glBegin(GL_POLYGON)#rightwheel
      glColor3f(0.6,0.6,0.6)
      glVertex(0.2,0)
      glVertex(0.3,0)
      glVertex(0.3,-0.3)
      glVertex(0.2,-0.3)
      glEnd()

      glBegin(GL_LINES)
      for y in np.arange (0,-0.3,-0.04):
         glColor3f(0,0,0)
         glVertex(0.2,y)
         glVertex(0.3,y) 
      glEnd()

      glBegin(GL_LINES)#wheelboard
      glVertex(0.2,0)
      glVertex(0.3,0)
      glVertex(0.3,0)
      glVertex(0.3,-0.3)
      glVertex(0.3,-0.3)
      glVertex(0.2,-0.3)
      glVertex(0.2,0)
      glVertex(0.2,-0.3)
      glVertex(-0.2,0)
      glVertex(-0.3,0)
      glVertex(-0.3,0)
      glVertex(-0.3,-0.3)
      glVertex(-0.3,-0.3)
      glVertex(-0.2,-0.3)
      glVertex(-0.2,0)
      glVertex(-0.2,-0.3)
      glEnd()
      
      
      glBegin(GL_POLYGON)#leftwheel
      glColor3f(0.6,0.6,0.6)
      glVertex(-0.2,0)
      glVertex(-0.3,0)
      glVertex(-0.3,-0.3)
      glVertex(-0.2,-0.3)
      glEnd()

      glBegin(GL_LINES)
      for y in np.arange (0.2,0.35,0.04):
         glColor3f(0,0,0)
         glVertex(0.05,y)
         glVertex(-0.05,y) 
      glEnd()


      glBegin(GL_POLYGON)#face
      glColor3f(1,0.9,0.3)
      glVertex(0.2,0.43)
      glVertex(-0.2,0.43)
      glVertex(0,0.3)
      glEnd()

      glBegin(GL_LINES)#faceboard
      glColor3f(0,0,0)
      glVertex(0.2,0.43)
      glVertex(-0.2,0.43)
      glVertex(-0.2,0.43)
      glVertex(0,0.3)
      glVertex(0,0.3)
      glVertex(0.2,0.43)
      glEnd()

      glBegin(GL_POLYGON)#neck
      glColor3f(1,0.9,0.3)
      glVertex(0.05,0.2)
      glVertex(0.05,0.35)
      glVertex(-0.05,0.35)
      glVertex(-0.05,0.2)
      glEnd()

      glBegin(GL_LINES)#neckboard
      glColor3f(0,0,0)
      glVertex(0.05,0.2)
      glVertex(0.05,0.35)
      glVertex(0.05,0.35)
      glVertex(-0.05,0.35)
      glVertex(-0.05,0.35)
      glVertex(-0.05,0.2)
      glEnd()
      
      glBegin(GL_LINES)
      for y in np.arange (0.2,0.35,0.06):
         glColor3f(0,0,0)
         glVertex(0.05,y)
         glVertex(-0.05,y) 
      glEnd()
     
     
      glBegin(GL_LINES)
      for y in np.arange (0,0.2,0.06):
         glColor3f(0,0,0)
         glVertex(0.2,y)
         glVertex(-0.2,y) 
      glEnd()
      
      glBegin(GL_LINES)#bodyboard
      glColor3f(0,0,0)
      glVertex(0.2,0.2)
      glVertex(-0.2,0.2)
      glVertex(-0.2,0.2)
      glVertex(-0.2,-0.2)
      glVertex(-0.2,-0.2)
      glVertex(0.2,-0.2)
      glVertex(0.2,-0.2)
      glVertex(0.2,0.2)
      glEnd()

      glBegin(GL_POLYGON)#righthand
      glColor3f(0.6,0.6,0.7)
      glVertex(0.25,0.08)
      glVertex(0.25,0.17)
      glVertex(0.1,0.17)
      glVertex(0.11,0.08)
      glEnd()
      
      glBegin(GL_POLYGON)#LEFthand
      glColor3f(0.6,0.6,0.7)
      glVertex(-0.25,0.08)
      glVertex(-0.25,0.17)
      glVertex(-0.1,0.17)
      glVertex(-0.11,0.08)
      glEnd()
      
      glBegin(GL_LINES)
      for y in np.arange (0,-0.3,-0.04):
         glColor3f(0,0,0)
         glVertex(-0.2,y)
         glVertex(-0.3,y)
      glEnd()
  
      #eyes
      draw_circle(0.07,-0.13,0.4,0.5,0.5,0.6)
      draw_circleb(0.07,-0.13,0.4,0,0,0)
      draw_circle(0.055,-0.11,0.43,0.6,0.6,0.7)
      draw_circleb(0.055,-0.11,0.43,0,0,0)
      draw_circle(0.07,0.13,0.40,0.5,0.5,0.6)
      draw_circleb(0.07,0.13,0.40,0,0,0)
      draw_circle(0.055,0.11,0.43,0.6,0.6,0.7)
      draw_circle(0.03,0.11,0.43,0,0,0)
      draw_circle(0.03,-0.11,0.43,0,0,0)
      draw_circle(0.02,0.05,0.15,1,0,0)
      
      
      draw_circleb(0.055,0.11,0.43,0,0,0)
      draw_circleb(0.02,0.05,0.15,0,0,0)
      
      glFlush()
      

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize(600, 600)
window = glutCreateWindow(b"OpenGL Primitives: GL_POINTS" )
glutDisplayFunc(draw)
glutMainLoop()
