#letters
#Vaasu


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np

from random import randint

from flower_field import rectangle

window_width = 500.0
window_height = 500.0

def split_string(sentence):
	split=[]
	for i in sentence:
		split += [i]
	return split

def slant(x,y,width,height,slant):
	glBegin(GL_QUADS)
	glVertex3f(x,y,0)
	glVertex3f(x+width,y,0)
	glVertex3f(x+slant*width,y+height,0)
	glVertex3f(x+(slant-1)*width,y+height,0)
	glEnd()

def letter_a(x,y,size):
	y +=.3
	slant(x,y,.15*size,-size,3)
	slant(x+size/10,y,-.15*size,-size,3)
	rectangle(x,y-size/2,size/2.4,size*.10)

def letter_b(x,y,size):
	letter_e(x,y,size)
	rectangle(x+size/2.7,y,size/8.0,size)

def letter_c(x,y,size):
	letter_l(x,y,size)
	rectangle(x+size/5,y+size/2.3,size/2.7,size/8.0)

def letter_d(x,y,size):
	size *= 1.05
	letter_c(x,y,size)
	rectangle(x+size/2.6,y,size/8.0,size)

def letter_e(x,y,size):
	letter_f(x,y,size)
	rectangle(x+size/5,y-size/2.3,size/2.7,size/8.0)

def letter_f(x,y,size):
	'''function creates F'''
	rectangle(x,y,size/8.0,size)
	rectangle(x+size/5,y+size/2.3,size/2.7,size/8.0)
	rectangle(x+size/5,y,size/2.7,size/8.0)

def letter_g(x,y,size):
	letter_c(x,y,size)
	rectangle(x+size/2.7,y-size/4.5,size/8.0,size/2.5)

def letter_h(x,y,size):
	rectangle(x,y,size/8.0,size)
	rectangle(x+size/5,y,size/2.7,size/8.0)
	rectangle(x+size/2.5,y,size/8.0,size)

def letter_i(x,y,size):
	'''function creates I '''
	letter_t(x,y,size)
	rectangle(x,y-size/2.3,size/1.7,size/8.0)

def letter_j(x,y,size):
	'''function creates J '''
	rectangle(x,y-size/4.5,size/8.0,size/2.5)
	rectangle(x+size/5,y-size/2.3,size/2.7,size/8.0)
	rectangle(x+size/2.6,y,size/8.0,size)

def letter_k(x,y,size):
	'''function creates K '''
	rectangle(x,y,size/8.0,size)
	slant(x,y,.15*size,-size/2,4.5)
	slant(x,y,.15*size,size/2,4.5)

def letter_l(x,y,size):
	'''function creates a capital L''' 
	rectangle(x,y,size/8.0,size)
	rectangle(x+size/5,y-size/2.3,size/2.6,size/8.0)

def letter_m(x,y,size):
	rectangle(x,y,size/8.0,size)
	letter_v(x+size/5,y+size/3.6,size/1.4)
	rectangle(x+size/2.1,y,size/8.0,size)

def letter_n(x,y,size):
	rectangle(x-size/5,y,size/8.0,size)
	slant(x+size/4,y-0.37,-.14*size,size,3.75)
	rectangle(x+size/4,y,size/8.0,size)

def letter_o(x,y,size):
	size *= .95
	letter_d(x,y,size)

def letter_p(x,y,size):
	letter_f(x,y,size)
	rectangle(x+size/2.5,y+size/4.6,size/8.0,size/2.5)

def letter_r(x,y,size):
	letter_p(x,y,size)
	slant(x,y,.15*size,-size/2,4.5)

def letter_s(x,y,size):
	rectangle(x+size/5,y+size/2.3,size/2.7,size/8.0)
	rectangle(x+size/5,y,size/2.7,size/8.0)
	rectangle(x+size/5,y-size/2.3,size/2.7,size/8.0)
	rectangle(x+size/2.7,y-size/4.5,size/8.0,size/2.5)
	rectangle(x,y+size/4.5,size/8.0,size/2.5)

def letter_t(x,y,size):
	rectangle(x,y,size/8.0,size)
	rectangle(x,y+size/2.3,size/1.7,size/8.0)

def letter_u(x,y,size):
	letter_l(x,y,size)
	rectangle(x+size/2.6,y,size/8.0,size)
	
def letter_v(x,y,size):
		y -= 0.3
		slant(x,y,.15*size,size,2.5)
		slant(x+size/10,y,-.15*size,size,2.5)

def letter_w(x,y,size):
		letter_v(x-.15,y,size*.9)
		letter_v(x+.15,y,size*.9)

def letter_x(x,y,size):
	y -= 0.4
	slant(x+-.20,y,.15*size,size,4)
	slant(x+.20,y,-.15*size,size,4)

def letter_y(x,y,size):
	y-=.2
	letter_v(x,y+size/2,size/1.3)
	rectangle(x+.02,y-size/5,size/8.0,size/2)

def letter_z(x,y,size):
	size *= 1.1
	rectangle(x+size/5,y+size/2.3,size/2.7,size/8.0)
	rectangle(x+size/5,y-size/2.3,size/2.7,size/8.0)
	y-=.3
	size/=1.2
	slant(x,y,.15*size,size,3)
	

def single_line(letter,size, perline, line):
	space=[]
	rest_of_script=[]
	newline=len(letter)
	for i in range(len(letter)):
		if (letter[i]==" "):
			space += [i]

	space += [len(letter)-1]


	for i in range(len(space)):
		if (space[i] > perline):
			newline=space[i-1]
			break

	for i in range(newline):
		place = i % perline 

		sentence((place-13) * .7,(8-line*2),size,letter[i])

	while (newline < space[-1]):
			rest_of_script += letter[newline+1]
			newline += 1
	return rest_of_script

def single_page(letter,size,perline,line):
		rest_of_script = single_line(letter,size,perline,0)
		
		linenum=1
		while (len(rest_of_script) > 0):
			rest_of_script = single_line(rest_of_script,size,perline,linenum)
			linenum += 1 
		

def sentence(x,y,size,letter):
	if (letter == 'a'):
		letter_a(x,y,size)

	elif (letter == 'b'):
		letter_b(x,y,size)

	elif (letter == 'c'):
		letter_c(x,y,size)

	elif (letter == 'd'):
		letter_d(x,y,size)

	elif (letter == 'e'):
		letter_e(x,y,size)

	elif (letter == 'f'):
		letter_f(x,y,size)

	elif (letter == 'g'):
		letter_g(x,y,size)

	elif (letter == 'h'):
		letter_h(x,y,size)

	elif (letter == 'i'):
		letter_i(x,y,size)

	elif (letter == 'j'):
		letter_j(x,y,size)

	elif (letter == 'k'):
		letter_k(x,y,size)

	elif (letter == 'l'):
		letter_l(x,y,size)

	elif (letter == 'm'):
		letter_m(x,y,size)

	elif (letter == 'n'):
		letter_n(x,y,size)

	elif (letter =='o'):
		letter_o(x,y,size)

	elif (letter =='p'):
		letter_p(x,y,size)

	elif (letter =='r'):
		letter_r(x,y,size)

	elif (letter =='s'):
		letter_s(x,y,size)

	elif (letter == 't'):
		letter_t(x,y,size)

	elif (letter == 'u'):
		letter_u(x,y,size)

	elif (letter == 'v'):
		letter_v(x,y,size)

	elif (letter == 'w'):
		letter_w(x,y,size)

	elif (letter == 'x'):
		letter_x(x,y,size)

	elif (letter == 'y'):
		letter_y(x,y,size)

	elif (letter == 'z'):
		letter_z(x,y,size)

class Letters():
	def __init__(self):
		self.x=-8.0
		self.y=8.0
		self.size=0.6
		self.letter=split_string("try typing but no capitals or puncuation")
		self.frame=0 

	def display(self):
		glClearColor(0,0,0,0.0)
		glClear (GL_COLOR_BUFFER_BIT)
		
		title_color=abs(sin(self.frame))
		#glColor3f(title_color,title_color,title_color)
		glColor3f(1,1,1)

		single_page(self.letter,self.size,26,0)
		

		glutSwapBuffers()

	def idle(self):

		self.frame += .02
		glutPostRedisplay()

	def keyboard(self,*args):
		glColor3f(1.0,1.0,1.0)
		if (args[0]=='q'):
			del(self.letter[len(self.letter)-1])
		
		else:
			self.letter += [args[0]]

		#self.x += 1.5
		#glutSwapBuffers()
		#print(self.letter)
		glutPostRedisplay()

	def reshape(self, w, h):
		glViewport (0, 0, w,  h)      #Defines a pixel rectangle in the window into which the final image is mapped. The (x, y) parameter specifies the lower-left corner of the viewport, and width and height are the size of the viewport rectangle. By default, the initial viewport values are (0, 0, winWidth, winHeight), where winWidth and winHeight are the size of the window.
		glMatrixMode (GL_PROJECTION)
		glLoadIdentity ()
		gluPerspective(95.0, w/h, 1.0, 14.0) #GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar
		gluLookAt(0,0,5,0,0,-5,0,1,0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef (0.0, 0.0, -5.0)



	def main(self):
	
		glutInit(sys.argv)                    #initial the system
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)

		glutInitWindowSize(int(window_width), int(window_height))          #initial window size
		glutInitWindowPosition(100, 100)          #initial window position

		glutCreateWindow("Letters")     #assign a title for the window

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self.keyboard)
		glutIdleFunc(self.idle)
		
		glutMainLoop()                        #callback function enter the GLUT event processing loop

if __name__ == "__main__":
	letters=Letters()
	letters.main()
