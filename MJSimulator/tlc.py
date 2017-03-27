import scene
from graphics import *
import threading
import ip
import pishu_db as db
import algo_dennis as algo
import inspect

h = scene.ret_h()
w = scene.ret_w()
win = scene.ret_win()

lock = threading.Lock()

# signal light 
class sLight:

	def __init__(self,d):
		self.counter = 0
		self.cir = [0,0,0,0]
		self.next_active_signal = -1
		self.checker = False
		self.checker2 = False
		self.d = d
		
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
			
		direction = ['w','s','e','n']
		db.init(self.d,direction[self.active_signal])
	# to change the green signal of a particular signal   		
	def change_sig(self):
		
		self.cir[self.active_signal].setFill("red")
	#	self.active_signal = (self.active_signal + 1) % 4	 
	#	self.cir[self.active_signal].setFill("green")
		self.next_active_signal = (self.active_signal+1)%4 
		self.active_signal = -1
		self.cir[self.next_active_signal].setFill("orange")
		self.checker = False
		threading.Timer(1, self.changelight).start()  #TRANSITION TIME B/W SIGNAL

	def const(self):
		global lock
		lock.acquire()
		caller = inspect.getouterframes(inspect.currentframe())[1][3]
		if self.d == 1:		
			print caller+" REQUESTING RESOURCE !!!!!!!"
		try:
			if self.d == 1:
				print("**** LOCKING ****")
			self.checker = True
			ip.img_process(self)
			numtodir = ['w','s','e','n']
			timer_val = algo.calc_timer(self.d,numtodir[self.next_active_signal])
			threading.Timer(1+timer_val,self.const).start()
		finally:
			lock.release()
	
	def changelight(self):
		self.checker2 = True
	
	def change_orange(self):
		self.cir[self.next_active_signal].setFill("green")
		self.active_signal = self.next_active_signal
		self.next_active_signal = -1
		self.checker2 = False
	
