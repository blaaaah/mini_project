from graphics import *
import cmath
import random
import threading
import gtk # python-gtk2
from math import *

h=700
w=700
win=0
sourcelist=[(7*w/36,0),(15*w/36,0),(23*w/36,0),(31*w/36,0),(0,5*h/36),(w,7*h/36),(0,13*h/36),(w,15*h/36),(0,21*h/36),(w,23*h/36),(0,29*h/36),(w,31*h/36),(5*w/36,h),(13*w/36,h),(21*w/36,h),(29*w/36,h)]


def get_pixel_colour(i_x, i_y):
	i_y += 78
	i_x += 100
	o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
	return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])

class makecar:
	def __init__(self, win):
		self.source=sourcelist[int(random.getrandbits(4))]
		self.body = Rectangle(Point(self.source[0]-5,self.source[1]-5), Point(self.source[0]+5,self.source[1]+5))
		self.body.setFill("white")
 		self.body.draw(win)
		self.sig_flag=0						# Used in checkmove
		self.cxc=0							# All parameters starting with c used for circular move
		self.cyc=0
		self.csf=0
		self.ctheta=0
		self.cxa=0
		self.cya=0
		self.wtime=0						# Track stationary time
		self.cthetainc=0

		if self.source[0] == 0:
			self.update=(1,0)
		elif self.source[0] == w:
			self.update=(-1,0)
		elif self.source[1] == 0:
			self.update=(0,1)
		elif self.source[1] == h:
			self.update=(0,-1)

	def circular_move(self, direction):		#SET CXC CYC AND CSF for circular rotation
		if direction.imag==1:
			self.csf = h/36
			self.cxa = h/36
			self.ctheta = 0
			self.cthetainc = +1
		else:
			self.csf = 3*h/36
			self.ctheta = 180
			self.cxa = -3*h/36
			self.cthetainc = -1
		self.cyc=0
		adj = self.make_complex(self.update)*self.csf*direction
		self.cxc, self.cyc = self.body.getCenter().getX() + adj.real, self.body.getCenter().getY() + adj.imag
		
		

	def rotate(self):
		ang=radians(self.ctheta) 
		xap=self.cxa
		yap=self.cya
		self.ctheta+=self.cthetainc
		self.cxa=(self.csf)*cos(ang)
		self.cya=(self.csf)*sin(ang)
		ux, uy = round(self.cxa - xap), round(self.cya - yap)
		print "CXA :",self.cxa, "CYA :", self.cya, "XAP :", xap,"YAP: ",yap
		self.body.move(ux, uy)
		print "Update:", ux,uy
		print self.csf

		if self.ctheta==90:		#RESET
			self.ctheta=0
			self.csf=0
		

	def checkmove(self):
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
			if get_pixel_colour(int(c[0]+check[0]), int(c[1]+check[1]))==(0,0,0):
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
		if self.csf!=0:
			self.rotate()
		elif self.checkmove():		
			self.body.move(self.update[0],self.update[1])
		else:
			self.wtime += 1

