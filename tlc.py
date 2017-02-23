import scene
from graphics import *
h = scene.ret_h()
w = scene.ret_w()
win = scene.ret_win()

def ret_dir(s):
	if s.active_signal == 3:
		return 'n'
	if s.active_signal == 0:
		return 'w'
	if s.active_signal == 1:
		return 's'
	if s.active_signal == 2:
		return 'e'

def control():
	sig_list = scene.def_sig()
	
	while 1==1:
		flag = 0
		for s in sig_list:
			if s.counter==s.timer:
				s.change_sig()
				if(flag == 0):
					print ret_dir_array(sig_list)
					flag = 1
				s.counter = 0
			s.draw_signal()	
			
			s.counter +=1

        
def ret_dir_array(sig_list):
	active_dir = []
	for s in sig_list:
		active_dir.append(ret_dir(s))
	return active_dir
	

class sLight:
	def __init__(self,d):
		self.counter = 0
		
	    	self.cir = []
	    	self.cir.append(0)
	    	self.cir.append(0)
	    	self.cir.append(0)
	    	self.cir.append(0)
	    	
	    	
	    	if d==1:
	    		self.x = (w/18) + (w/9) 
	    		self.y = (h/18) + (h/9)
	    		self.active_signal = 3
	    		self.timer = 100
	    	if d==2:
	    		self.x = (w/18) + (3*(w/9)) 
	    		self.y = (h/18) + (h/9)
	    		self.active_signal = 2
	    		self.timer = 100
	    	if d==3:
	    		self.x = (w/18) + (5*(w/9)) 
	    		self.y = (h/18) + (h/9)
	    		self.active_signal = 1
	    		self.timer = 100
	    	if d==4:
	    		self.x = (w/18) + (7*(w/9)) 
	    		self.y = (h/18) + (h/9)
	    		self.active_signal = 0
	    		self.timer = 100
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
	    		
	
	def draw_signal(self):
		if self.active_signal == 0:
	    		self.cir[0] = (Circle(Point(self.x - (w/18),self.y - (h/18)), 5))
	    		self.cir[0].setFill("green")
	    		self.cir[0].draw(win)
	    		
	    	    	self.cir[1] = (Circle(Point(self.x - (w/18),self.y + (h/18)), 5))
		    	self.cir[1].setFill("red")
		    	self.cir[1].draw(win)

		    	self.cir[2] = (Circle(Point(self.x + (w/18),self.y + (h/18)), 5))
		    	self.cir[2].setFill("red")
		    	self.cir[2].draw(win)
	    		
	    		self.cir[3] = (Circle(Point(self.x + (w/18),self.y - (h/18)), 5))
		    	self.cir[3].setFill("red")
		    	self.cir[3].draw(win)
	    	
	    	
	    	if self.active_signal == 1:
	    		self.cir[0] = (Circle(Point(self.x - (w/18),self.y - (h/18)), 5))
		    	self.cir[0].setFill("red")
		    	self.cir[0].draw(win)
	    		
	    		self.cir[1] = (Circle(Point(self.x - (w/18),self.y + (h/18)), 5))
	    		self.cir[1].setFill("green")
	    		self.cir[1].draw(win)
	    		
		    	self.cir[2] = (Circle(Point(self.x + (w/18),self.y + (h/18)), 5))
		    	self.cir[2].setFill("red")
		    	self.cir[2].draw(win)

			self.cir[3] = (Circle(Point(self.x + (w/18),self.y - (h/18)), 5))
		    	self.cir[3].setFill("red")
		    	self.cir[3].draw(win)

		if self.active_signal == 2:
	    	
	    		self.cir[0] = (Circle(Point(self.x - (w/18),self.y - (h/18)), 5))
		    	self.cir[0].setFill("red")
		    	self.cir[0].draw(win)
		    	
		    	self.cir[1] = (Circle(Point(self.x - (w/18),self.y + (h/18)), 5))
		    	self.cir[1].setFill("red")
		    	self.cir[1].draw(win)

			self.cir[2] = (Circle(Point(self.x + (w/18),self.y + (h/18)), 5))
	    		self.cir[2].setFill("green")
	      		self.cir[2].draw(win)
	    		
		    	self.cir[3] = (Circle(Point(self.x + (w/18),self.y - (h/18)), 5))
		    	self.cir[3].setFill("red")
		    	self.cir[3].draw(win)

		if self.active_signal == 3:
	    		
	    		self.cir[0] = (Circle(Point(self.x - (w/18),self.y - (h/18)), 5))
		    	self.cir[0].setFill("red")
		    	self.cir[0].draw(win)
		    	
		    	self.cir[1] = (Circle(Point(self.x - (w/18),self.y + (h/18)), 5))
		    	self.cir[1].setFill("red")
		    	self.cir[1].draw(win)

		    	self.cir[2] = (Circle(Point(self.x + (w/18),self.y + (h/18)), 5))
		    	self.cir[2].setFill("red")
		    	self.cir[2].draw(win)

			self.cir[3] = (Circle(Point(self.x + (w/18),self.y - (h/18)), 5))
	    		self.cir[3].setFill("green")
	    		self.cir[3].draw(win)	
	    		
	def change_sig(self):
		self.active_signal = (self.active_signal + 1) % 4	 
