
#hot air Balloon


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np

from random import randint

from letters import rectangle,letter_f,letter_u,letter_e,letter_l, letter_b, letter_o, letter_i, slant


window_width = 500.0
window_height = 500.0


def letter_a(x,y,size):
	y +=1.0
	slant(x,y,.15*size,-size,3)
	slant(x+size/10,y,-.15*size,-size,3)
	rectangle(x,y-size/2,size/2.4,size*.10)


def letter_n(x,y,size):
	rectangle(x-size/5,y,size/8.0,size)
	slant(x+size/4,y-1.0,-.15*size,size,3.5)
	rectangle(x+size/4,y,size/8.0,size)


def rectangle(x,y,length,height):
	glBegin(GL_QUADS)
	glVertex3f(x+length/2,y+height/2,0)
	glVertex3f(x+length/2,y-height/2,0)
	glVertex3f(x-length/2,y-height/2,0)
	glVertex3f(x-length/2,y+height/2,0)
	glEnd()

def octagon(x,y,size):
	'''
	makes a regular polygon of width, 2 * size
	'''
	glBegin(GL_POLYGON)

	f=tan(pi/8)
	glVertex3f(x+size/f,y+size,0)
	glVertex3f(x+size/f,y-size,0)

	glVertex3f(x+size,y-size/f,0)
	glVertex3f(x-size,y-size/f,0)

	glVertex3f(x-size/f ,y-size,0)
	glVertex3f(x-size/f,y + size,0)

	glVertex3f(x-size,y +size/f,0)
	glVertex3f(x+size,y +size/f,0)

	glEnd()

def cloud(size):
	octagon(-.9,0,.3)
	octagon(-.5,.5,.3)
	octagon(0,0,.3)
	octagon(.5,.5,.3)
	octagon(.9,0,.3)

def balloonx(size):
	glColor3f(0.9,0.6,0.6)
	octagon(0,0,size)

	glColor3f(0.8,0.7,0.5)
	rectangle(0,-4.5*size,2*size,2*size)

def flame(size):
	glBegin(GL_POLYGON)
	glVertex3f(size/4,size/2,0)
	glVertex3f(0,0,0)
	glVertex3f(-size/4,size/2,0)
	glVertex3f(0,0,0)
	glEnd()


class Balloon():

	def __init__(self):
		''

		self.display_b=6.0
		self.bx=0
		self.by=0 + self.display_b/4
		self.flameon=0
		
		self.vx=3.0
		self.vy= 0.0
		self.time=0.02

		self.mode = .3
		self.fuel= 15.0 * self.mode // 1 + 6
		self.land=0

		self.kaboom=0
		self.title_show=1
		

	def reshape(self, w, h):
		glViewport (0, 0, w,  h)      #Defines a pixel rectangle in the window into which the final image is mapped. The (x, y) parameter specifies the lower-left corner of the viewport, and width and height are the size of the viewport rectangle. By default, the initial viewport values are (0, 0, winWidth, winHeight), where winWidth and winHeight are the size of the window.
		glMatrixMode (GL_PROJECTION)
		glLoadIdentity ()
		gluPerspective(95.0, w/h, 1.0, 14.0) #GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar
		gluLookAt(0,0,5,0,0,-5,0,1,0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef (0.0, 0.0, -5.0)

		#glutPostRedisplay()

	def title(self,x,y,size):
		width=3*size/2

		letter_b(x,y,size)
		letter_a(x+width,y,size)
		letter_l(x+2*width,y,size)
		letter_l(x+3*width,y,size)
		letter_o(x+4*width,y,size)
		letter_o(x+5*width,y,size)
		letter_n(x+6*width,y,size)

		letter_l(x+1.5*width,y-1.5*width,size)
		letter_a(x+2.5*width,y-1.5*width,size)
		letter_n(x+3.5*width,y-1.5*width,size)
		letter_o(x+4.3*width,y-1.5*width,size*1.1)



	def display(self):
		glClearColor(.6,.8,.9,0.0)
		glClear (GL_COLOR_BUFFER_BIT)

		if (self.title_show==1):
			self.title(-10,5.0,2.0)
			self.vy=0

		if (self.title_show != 1):
			self.display_b=0.0
			if (self.mode==.2):
				letter_e(8,-8,2.0)
			if (self.mode ==.3):
				letter_i(8,-8,2.0)
			if (self.mode == .6):
				letter_n(8,-8,2.0)

		glColor3f(0.6,0.9,0.6)
		rectangle(0,-11.0,30,3.0)

		glColor3f(0.4,0.4,0.4)
		rectangle(-10,-8,14,.4) #14

		glColor3f(1.0,1.0,1.0)
		letter_f(-8.0,-7,1.0)
		letter_u(-7.2,-7,1.0)
		letter_e(-6.4,-7,1.0)
		letter_l(-5.6,-7,1.0)

		glColor3f(.9,.2,.2)
		rectangle(-11.0,-8,self.fuel,.4)

		glPushMatrix()
		glTranslatef(self.display_b,self.by,0)
		glRotate(self.vy * -3.0,0.0,0.0,1.0)
		balloonx(.4)
		#put balloon design here

		if (self.flameon > 0):
			glPushMatrix()
			glColor3f(1.0,0.2,0.2)
			glTranslatef(0.0,-1.3,0.0)
			flame(.5)
			glPopMatrix()
			
		glPopMatrix()

		glPushMatrix()
		glTranslatef(-self.bx,0,0)
		glColor3f(1.0,1.0,1.0)

		for i in range (8):
			glPushMatrix()
			glTranslatef((-7+i*6),7 - (i % 2)* 9,0)
			cloud(.4)
			glPopMatrix()

		glPopMatrix()
		
		if (self.bx>24.0):
			self.bx=0

		if (self.kaboom==1):
			glColor3f(1.0,0.0,0.0)
			octagon(0,-8.0,1.0)
			glColor3f(.8,.8,0.2)
			octagon(0,-8.0,0.7)
			glColor3f(.9,.4,.4)
			octagon(0,-8.0,0.4)

		if (self.land==1):
			''
			

		self.flameon -= 1

		

		glutSwapBuffers()

	def idle(self):
		self.bx += self.vx * self.time
		self.by += self.vy * self.time

		self.vy -= .01

		if (-8.0 < self.by < -7.5):
			if (-self.mode > self.vy or self.vy > self.mode):
				self.kaboom=1
				print(self.vy)
			
			self.vy=0
			self.land= 1


		glutPostRedisplay()

	def keyboard(self,*args):
		if (args[0]=='w' and self.fuel>0):
			self.vy += .5
			self.flameon=20
			self.fuel -= 1

		if (args[0] == 'R'):
			self.title_show=0
			self.bx=0
			self.by=0
			self.flameon=0

			self.vx=3.0
			self.vy= 0.0
			self.time=0.02

			self.fuel=15.0 * self.mode // 1 + 7
			self.land=0

			self.kaboom=0

		if (args[0] == "N"):
			self.mode = .6
			

		if (args[0] == "I"):
			self.mode = .3
		

		if (args[0] == "E"):
			self.mode = .2


		glutPostRedisplay()
	def main(self):
	
		glutInit(sys.argv)                    #initial the system
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)

		glutInitWindowSize(int(window_width), int(window_height))          #initial window size
		glutInitWindowPosition(100, 100)          #initial window position

		glutCreateWindow("Balloon Land")     #assign a title for the window

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutIdleFunc(self.idle)
		glutKeyboardFunc(self.keyboard)

		glutMainLoop()                        #callback function enter the GLUT event processing loop

if __name__ == "__main__":
	balloon=Balloon()
	balloon.main()


