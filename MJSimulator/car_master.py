from graphics import *
import cmath
import random
import threading
import gtk # python-gtk2
from math import *

h=700
w=700
win=0
sourcelist=[((7*w)/36,0),((15*w)/36,0),((23*w)/36,0),((31*w)/36,0),(0,(5*h)/36),(w,(7*h)/36),(0,(13*h)/36),(w,(15*h)/36),(0,(21*h)/36),(w,(23*h)/36),(0,(29*h)/36),(w,(31*h)/36),((5*w)/36,h),((13*w/36),h),((21*w)/36,h),((29*w)/36,h)]
track = 0


def get_pixel_colour(i_x, i_y):
	i_y += 78
	i_x += 100
	o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
	return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])

class makecar:
	def __init__(self, win):

		global track		

		self.source=sourcelist[int(random.getrandbits(4))]
		self.body = Rectangle(Point(self.source[0]-5,self.source[1]-5), Point(self.source[0]+5,self.source[1]+5))
		self.body.setFill("white")
 		self.body.draw(win)
		self.sig_flag=0						# Used in checkmove
		self.cc=0							# All parameters starting with c used for circular move
		self.pc=0
		self.csf=0
		self.ctheta=0
		self.wtime=0						# Track stationary time
		self.cthetainc=0
		self.selected=0

		if self.source[0] == 0:
			self.update=(1,0)
		elif self.source[0] == w:
			self.update=(-1,0)
		elif self.source[1] == 0:
			self.update=(0,1)
		elif self.source[1] == h:
			self.update=(0,-1)

		if (bool(random.getrandbits(1)) and track ==0):
			track=1	
			self.selected=1		
			print "Source: ", self.source

	def circular_move(self, direction):		#SET CXC CYC AND CSF for circular rotation
		
		global track

		if direction.imag==1:
			self.csf = (3*h)/36
			self.cthetainc = +2
		else:
			self.csf = h/36
			self.cthetainc = -2
		self.pc = -1*direction*self.csf

		if self.selected:
			print "Direction:",direction
			print "Update:", self.update
			print "PC", self.pc
			if direction.imag==1:
				print "I'm supposed to turn right"
			else:
				print "I'm supposed to turn left"
			print "CSF:", self.csf

		
		

	def rotate(self):

		global track

		ang=radians(self.cthetainc) 
		self.cc = self.pc*cmath.rect(1,ang)
		self.ctheta+=self.cthetainc
		up = self.cc - self.pc
		self.body.move(round(up.real), round(up.imag))
		self.pc = self.cc
		if self.selected:
			print "---------------------------------"
			print "Center: ",self.body.getCenter()
			print "UPD:", up
			print "SELF.CC", self.cc
			print "SELF.PC", self.pc
			


		if abs(self.ctheta)==90:		#RESET
			self.ctheta=0
			self.csf=0
			self.sig_flag=3

	def checkmove(self):

		global track

		#Check for neighbouring car
		check = tuple([15*x for x in self.update])
		c = [ self.body.getCenter().getX(),self.body.getCenter().getY() ]
		
		if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(255,255,255):
			return False

		#Check for signal
		if self.update[1]==0:
			check = ([-(h/36)*x for x in self.update])
		else:
			check = ([(h/36)*x for x in self.update])
		check[0],check[1] = check[1],check[0]
		#Correct light is being checked - Consider value
		if self.sig_flag==1:
			if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(0,128,0):
				return True
			elif get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(255,0,0):
				self.sig_flag=0				
				return False		
			else:
				self.sig_flag=2

				return True
		#Car in junction region
		if self.sig_flag==2:
			if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(0,0,0):
				return True
			else:
				self.sig_flag=3
				return True
		#Wrong light checked - Ignore value
		if self.sig_flag==3:
			if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(0,0,0) or get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(217,217,217):
				self.sig_flag=0
				return True
			else:
				return True

		#Check right				
		if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(255,0,0):
			return False
		elif get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(0,128,0):
			self.updateupdate()			
			self.sig_flag=1
		
		return True
	
	def updateupdate(self):

		global track

		choices = [complex(0,-1),complex(1,0),complex(1,0),complex(0,1)]
		choice = choices[int(random.getrandbits(2))]		
		
		if choice.imag != 0:
			self.circular_move(choice)

		present = self.make_complex(self.update)*choice
		update=[0,0]
		update[0]=present.real
		update[1]=present.imag
		self.update = tuple(update)	

	def make_complex(self, c):
		return complex(c[0],c[1])

	def move(self):

		global track

		if self.csf!=0:
			self.rotate()
		elif self.checkmove():		
			self.body.move(self.update[0],self.update[1])
			if self.selected:
				print "Center: ",self.body.getCenter()		
		else:
			self.wtime += 1

