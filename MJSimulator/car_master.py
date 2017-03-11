from graphics import *
import tlc
import scene

h=scene.ret_h()
w=scene.ret_w()
win=scene.ret_win()
sourcelist=[(7*w/36,0),(15*w/36,0),(23*w/36,0),(31*w/36,0),(0,5*h/36),(w,7*h/36),(0,13*h/36),(w,15*h/36),(0,21*h/36),(w,23*h/36),(0,29*h/36),(w,31*h/36),(5*w/36,h),(13*w/36,h),(21*w/36,h),(29*w/36,h)]

class car:
	def __init__(self):
		self.source=sourcelist[int(random.getrandbits(4))]
		self.body = Rectangle(Point(self.source[0]-5,self.source[1]-5), Point(self.source[0]+5,self.source[1]+5))
		self.body.setFill("white")
 		self.body.draw(win)
		self.sig_flag=0						# Used in checkmove

		if self.source[0] == 0:
			self.update=(1,0)
		elif self.source[0] == w:
			self.update=(-1,0)
		elif self.source[1] == 0:
			self.update=(0,1)
		elif self.source[1] == h:
			self.update=(0,-1)
			

	def center(self):
		return self.body.getCenter()


	def checkmove(self,sig_list):
		#Check for neighbouring car
		check = tuple([30*x for x in self.update])
		c = self.body.getCenter() 		
		if getPixel(c[0]+check[0], c[1]+check[1])==[255,255,255]:
			return false

		#Check for signal
		if self.update[1]==0:
			check = ([-(h/36)*x for x in self.update])
		else:
			check = ([(h/36)*x for x in self.update])
		check[0],check[1] = check[1],check[0]
		#Correct light is being checked - Consider value
		if self.sig_flag==1:
			if getPixel(c[0]+check[0], c[1]+check[1])==[0,255,0]:
				return true
			elif getPixel(c[0]+check[0], c[1]+check[1])==[255,0,0]:
				self.sig_flag=0				
				return false		
			else:
				self.sig_flag=2

				return true
		#Car in junction region
		if self.sig_flag==2:
			if getPixel(c[0]+check[0], c[1]+check[1])==[0,0,0]:
				return true
			else:
				self.sig_flag=3
				return true
		#Wrong light checked - Ignore value
		if self.sig_flag==3
			if getPixel(c[0]+check[0], c[1]+check[1])==[0,0,0]:
				self.sig_flag=0
				return true
			else
				return true

		#Check right				
		if getPixel(c[0]+check[0], c[1]+check[1])==[255,0,0]:
			return false
		elif getPixel(c[0]+check[0], c[1]+check[1])==[0,255,0]:: 
			self.updateupdate()			
			self.sig_flag=1
		
		return true
	
	def updateupdate():
		choices = [complex(0,-1),complex(1,0),complex(1,0),complex(0,1)]		
		present=complex(self.update[0],self.update[1])		
		present=present*choices[int(random.getrandbits(2))]
		self.update[0]=present.real
		self.update[0]=present.imag	

	def move(self,sig_list):
		if self.checkmove():		
			self.body.move(self.update[0],self.update[1])


#PASS SIGNAL LIST FROM MULTIJUNCTION
def start(sig_list):
	
