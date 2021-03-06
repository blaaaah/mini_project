import scene
import time	
from graphics import *
h = scene.ret_h()
w = scene.ret_w()
win = scene.ret_win()


# to return the active signal direction for a single junction
def ret_dir(s):
	if s.active_signal == 3:
		return 'n'
	if s.active_signal == 0:
		return 'w'
	if s.active_signal == 1:
		return 's'
	if s.active_signal == 2:
		return 'e'

# traffic junction control
def control():
	
	
	signal_counter = 0
	
	while 1==1:
	
		sig_list = scene.ret_sig_list()	
		for s in sig_list:
			if s.counter==s.timer:
				s.change_sig()
				signal_counter += 1
				if signal_counter == 16:
					print ret_dir_array(sig_list)
					signal_counter = 0
				s.counter = 0
			
			time.sleep(0.001)
			s.counter +=1


# return the array of active signal direction for all junctions
def ret_dir_array(sig_list):
	active_dir = []
	for s in sig_list:
		active_dir.append(ret_dir(s))
	return active_dir
	

# signal light 
class sLight:

	def __init__(self,d):
		self.counter = 0
		
		self.cir = [0,0,0,0]
	
		if d==1:
			self.x = (w/18) + (w/9) 
			self.y = (h/18) + (h/9)
			self.timer = 100
			self.active_signal = 3
		if d==2:
			self.x = (w/18) + (3*(w/9)) 
			self.y = (h/18) + (h/9)
			self.timer = 100
			self.active_signal = 2	    		
		if d==3:
			self.x = (w/18) + (5*(w/9)) 
			self.y = (h/18) + (h/9)
			self.timer = 100
			self.active_signal = 1	    		
		if d==4:
			self.x = (w/18) + (7*(w/9)) 
			self.y = (h/18) + (h/9)
			self.timer = 100
			self.active_signal = 0	    		
		if d==5:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + (3*(h/9))
			self.timer = 100
			self.active_signal = 2
		if d==6:
			self.x = (w/18) + (3*(w/9))
			self.y = (h/18) + (3*(h/9))
			self.timer = 100
			self.active_signal = 1
		if d==7:
			self.x = (w/18) + (5*(w/9))
			self.y = (h/18) + (3*(h/9))
			self.timer = 100
			self.active_signal = 0
		if d==8:
			self.x = (w/18) + (7*(w/9))
			self.y = (h/18) + (3*(h/9))
			self.timer = 100
			self.active_signal = 3
	
		if d==9:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + (5*(h/9))
			self.timer = 100
			self.active_signal = 1
		if d==10:
			self.x = (w/18) + (3*(w/9))
			self.y = (h/18) + (5*(h/9))
			self.timer = 100
			self.active_signal = 0
		if d==11:
			self.x = (w/18) + (5*(w/9))
			self.y = (h/18) + (5*(h/9))
			self.timer = 100
			self.active_signal = 3
		if d==12:
			self.x = (w/18) + (7*(w/9))
			self.y = (h/18) + (5*(h/9))
			self.timer = 100
			self.active_signal = 2
	
		if d==13:
			self.x = (w/18) + (w/9)
			self.y = (h/18) + (7*(h/9))
			self.timer = 100
			self.active_signal = 0
		if d==14:
			self.x = (w/18) + (3*(w/9))
			self.y = (h/18) + (7*(h/9))
			self.timer = 100
			self.active_signal = 3
		if d==15:
			self.x = (w/18) + (5*(w/9))
			self.y = (h/18) + (7*(h/9))
			self.timer = 100
			self.active_signal = 2
		if d==16:
			self.x = (w/18) + (7*(w/9))
			self.y = (h/18) + (7*(h/9))
			self.timer = 100
			self.active_signal = 1

	# to change the green signal of a particular signal   		
	def change_sig(self):
		
		self.cir[self.active_signal].setFill("red")
		self.active_signal = (self.active_signal + 1) % 4	 
		self.cir[self.active_signal].setFill("green")
		
		
		
		
