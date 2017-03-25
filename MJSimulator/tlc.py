import scene
from graphics import *
import threading

h = scene.ret_h()
w = scene.ret_w()
win = scene.ret_win()


# signal light 
class sLight:

	def __init__(self,d):
		self.counter = 0
		self.cir = [0,0,0,0]
		self.checker = False
		
		if d==1:
			self.x = (w/18) + (w/9) 
			self.y = (h/18) + (h/9)
			self.active_signal = 3
		if d==2:
			self.x = (w/18) + ((3*w)/9) 
			self.y = (h/18) + (h/9)
			self.active_signal = 2	    		
		if d==3:
			self.x = (w/18) + ((5*w)/9) 
			self.y = (h/18) + (h/9)
			self.active_signal = 1	    		
		if d==4:
			self.x = (w/18) + ((7*w)/9) 
			self.y = (h/18) + (h/9)
			self.active_signal = 0
			
		if d==5:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + ((3*h)/9)
			self.active_signal = 2
		if d==6:
			self.x = (w/18) + ((3*w)/9)
			self.y = (h/18) + ((3*h)/9)
			self.active_signal = 1
		if d==7:
			self.x = (w/18) + ((5*w)/9)
			self.y = (h/18) + ((3*h)/9)
			self.active_signal = 0
		if d==8:
			self.x = (w/18) + ((7*w)/9)
			self.y = (h/18) + ((3*h)/9)
			self.active_signal = 3
			
		if d==9:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + ((5*h)/9)
			self.active_signal = 1
		if d==10:
			self.x = (w/18) + ((3*w)/9)
			self.y = (h/18) + ((5*h)/9)
			self.active_signal = 0
		if d==11:
			self.x = (w/18) + ((5*w)/9)
			self.y = (h/18) + ((5*h)/9)
			self.active_signal = 3
		if d==12:
			self.x = (w/18) + ((7*w)/9)
			self.y = (h/18) + ((5*h)/9)
			self.active_signal = 2
			
		if d==13:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + ((7*h)/9)
			self.active_signal = 0
		if d==14:
			self.x = (w/18) + ((3*w)/9)
			self.y = (h/18) + ((7*h)/9)
			self.active_signal = 3
		if d==15:
			self.x = (w/18) + ((5*w)/9)
			self.y = (h/18) + ((7*h)/9)
			self.active_signal = 2
		if d==16:
			self.x = (w/18) + ((7*w)/9)
			self.y = (h/18) + ((7*h)/9)
			self.active_signal = 1

	# to change the green signal of a particular signal   		
	def change_sig(self):
		
		self.cir[self.active_signal].setFill("red")
		self.active_signal = (self.active_signal + 1) % 4	 
		self.cir[self.active_signal].setFill("green")

	def const(self):
		self.checker = True
		threading.Timer(3,self.const).start()
		