import matplotlib.pyplot as plt
from math import *
import time	
import random
import subprocess as sp
from graphics import *




class sLight:
	def __init__(self,d,win):
	    	self.cir = []
	    	self.active_signal = 3
	    	
	    		
	    	h = win.getHeight()
	    	w = win.getWidth()	    	
	    	
	    	if d==1:
	    		x = (w/18) + (w/9) 
	    		y = (h/18) + (h/9)
	    	if d==2:
	    		x = (w/18) + (3*(w/9)) 
	    		y = (h/18) + (h/9)
	    	if d==3:
	    		x = (w/18) + (5*(w/9)) 
	    		y = (h/18) + (h/9)
	    	if d==4:
	    		x = (w/18) + (7*(w/9)) 
	    		y = (h/18) + (h/9)
	    		
	    	if d==5:
	    		x = (w/18) + (w/9)
	    		y = (h/18) + (3*(h/9))
	    	if d==6:
	    		x = (w/18) + (3*(w/9))
	    		y = (h/18) + (3*(h/9))
	    	if d==7:
	    		x = (w/18) + (5*(w/9))
	    		y = (h/18) + (3*(h/9))
	    	if d==8:
	    		x = (w/18) + (7*(w/9))
	    		y = (h/18) + (3*(h/9))
	    		

	    	if d==9:
	    		x = (w/18) + (w/9)
	    		y = (h/18) + (5*(h/9))
	    	if d==10:
	    		x = (w/18) + (3*(w/9))
	    		y = (h/18) + (5*(h/9))
	    	if d==11:
	    		x = (w/18) + (5*(w/9))
	    		y = (h/18) + (5*(h/9))
	    	if d==12:
	    		x = (w/18) + (7*(w/9))
	    		y = (h/18) + (5*(h/9))
	    		

	    	if d==13:
	    		x = (w/18) + (w/9)
	    		y = (h/18) + (7*(h/9))
	    	if d==14:
	    		x = (w/18) + (3*(w/9))
	    		y = (h/18) + (7*(h/9))
	    	if d==15:
	    		x = (w/18) + (5*(w/9))
	    		y = (h/18) + (7*(h/9))
	    	if d==16:
	    		x = (w/18) + (7*(w/9))
	    		y = (h/18) + (7*(h/9))
	    		

	    	
	    	self.cir.append(Circle(Point(x - (w/18),y - (h/18)), 5))
	    	self.cir[0].setFill("red")
	    	self.cir[0].draw(win)

	    	self.cir.append(Circle(Point(x - (w/18),y + (h/18)), 5))
	    	self.cir[1].setFill("red")
	    	self.cir[1].draw(win)

	    	self.cir.append(Circle(Point(x + (w/18),y + (h/18)), 5))
	    	self.cir[2].setFill("red")
	    	self.cir[2].draw(win)

	    	self.cir.append(Circle(Point(x + (w/18),y - (h/18)), 5))
	    	self.cir[3].setFill("green")
	    	self.cir[3].draw(win)
    	

class makecar:

	def __init__(self,d,win):
		
		h = win.getHeight()
		w = win.getWidth()	
		self.counter = 0
		if d==1:
	    		cx = (w/18) + (w/9) + 30
			cy = -50
		elif d==2:			
			cx = (w/18) + (3*(w/9)) + 30
			cy = -50
		elif d==3:
			cx = (w/18) + (5*(w/9)) + 30
			cy = -50
		elif d==4:
			cx = (w/18) + (7*(w/9)) + 30
			cy = -50
		elif d==5:
			cx = -50
			cy = (h/18) + (h/9) - 30
		elif d==6:
			cx = -50
			cy = (h/18) + (3*(h/9)) - 30
		elif d==7:
			cx = -50
			cy = (h/18) + (5*(h/9)) - 30
		elif d==8:
			cx = -50
			cy = (h/18) + (7*(h/9)) - 30
		elif d==9:
	    		cx = (w/18) + (w/9) - 30
			cy = h + 50
		elif d==10:			
			cx = (w/18) + (3*(w/9)) - 30
			cy = h + 50
		elif d==11:
			cx = (w/18) + (5*(w/9)) - 30
			cy = h + 50
		elif d==12:
			cx = (w/18) + (7*(w/9)) - 30
			cy = h + 50	
		elif d==13:
			cx = w + 50
			cy = (h/18) + (h/9) + 30
		elif d==14:
			cx = w + 50
			cy = (h/18) + (3*(h/9)) + 30
		elif d==15:
			cx = w + 50
			cy = (h/18) + (5*(h/9)) + 30
		elif d==16:
			cx = w + 50
			cy = (h/18) + (7*(h/9)) + 30
	 	self.body = Rectangle(Point(cx-5, cy-5), Point(cx+5, cy+5))
		self.body.setFill("white")
 		self.body.draw(win)


	
def main():
	win = GraphWin('Simulator', 1400, 1000)
	w=win.getWidth()
	h=win.getHeight()
	
	
	rect = Rectangle(Point(w/9,0), Point(2*(w/9), h))
   	rect.setFill("black")
	rect.draw(win)

	rect = Rectangle(Point(w/3,0), Point(4*(w/9), h))
   	rect.setFill("black")
	rect.draw(win)

	rect = Rectangle(Point(5*(w/9),0), Point(2*(w/3), h))
   	rect.setFill("black")
	rect.draw(win)

	rect = Rectangle(Point(7*(w/9),0), Point(8*(w/9), h))
   	rect.setFill("black")
	rect.draw(win)

	rect = Rectangle(Point(0,h/9), Point(w,2*(h/9)))
   	rect.setFill("black")
	rect.draw(win)

	rect = Rectangle(Point(0,3*(h/9)), Point(w,4*(h/9)))
   	rect.setFill("black")
	rect.draw(win)
		
	rect = Rectangle(Point(0,5*(h/9)), Point(w,6*(h/9)))
   	rect.setFill("black")
	rect.draw(win)
	
	rect = Rectangle(Point(0,7*(h/9)), Point(w,8*(h/9)))
   	rect.setFill("black")
	rect.draw(win)

     
        sig_1_n_level = (h/9)
        sig_1_s_level = (2*(h/9))
        sig_1_e_level = sig_5_e_level =sig_9_e_level =sig_13_e_level =(2*(w/9))
        sig_1_w_level = sig_5_w_level =sig_9_w_level =sig_13_w_level =(w/9)
     
        sig_2_n_level = (h/9)
        sig_2_s_level = (2*(h/9))
        sig_2_e_level =sig_6_e_level =sig_10_e_level =sig_14_e_level = (4*(w/9))
        sig_2_w_level =sig_6_w_level =sig_10_w_level =sig_14_w_level = 3*(w/9)
     
        sig_3_n_level = (h/9)
        sig_3_s_level = (2*(h/9))
        sig_3_e_level = sig_7_e_level =sig_11_e_level =sig_15_e_level =(6*(w/9))
        sig_3_w_level = sig_7_w_level =sig_11_w_level =sig_15_w_level =5*(w/9)
     
        sig_4_n_level = (h/9)
        sig_4_s_level = (2*(h/9))
        sig_4_e_level =sig_8_e_level =sig_12_e_level =sig_16_e_level = (8*(w/9))
        sig_4_w_level =sig_8_w_level =sig_12_w_level =sig_16_w_level = 7*(w/9)

	sig_5_n_level = sig_6_n_level = sig_7_n_level = sig_8_n_level = 3*(h/9)
	sig_9_n_level = sig_10_n_level = sig_11_n_level = sig_12_n_level =5*(h/9)
	sig_13_n_level = sig_14_n_level = sig_15_n_level = sig_16_n_level =7*(h/9)	
				
	sig_5_s_level = sig_6_s_level = sig_7_s_level = sig_8_s_level = 4*(h/9)
	sig_9_s_level = sig_10_s_level = sig_11_s_level = sig_12_s_level =6*(h/9)
	sig_13_s_level = sig_14_s_level = sig_15_s_level = sig_16_s_level =8*(h/9)	
		



	signal = []
	
	for i in range(16):
		s = sLight(i+1,win)
		signal.append(s)
    	
    	car_list_1 = []
    	car_list_2 = []
    	car_list_3 = []
    	car_list_4 = []
    	
    	car_list_5 = []
    	car_list_6 = []
    	car_list_7 = []
    	car_list_8 = []
    	
       	car_list_9 = []
    	car_list_10 = []
    	car_list_11 = []
    	car_list_12 = []
    	
    	car_list_13 = []
    	car_list_14 = []
    	car_list_15 = []
	car_list_16 = []

    		
	car_1_n_level = sig_1_n_level
	car_2_n_level = sig_2_n_level
	car_3_n_level = sig_3_n_level
	car_4_n_level = sig_4_n_level    	

	car_5_n_level = sig_5_n_level
	car_6_n_level = sig_6_n_level
	car_7_n_level = sig_7_n_level
	car_8_n_level = sig_8_n_level
	
	car_9_n_level = sig_9_n_level
	car_10_n_level = sig_10_n_level
	car_11_n_level = sig_11_n_level
	car_12_n_level = sig_12_n_level
	
	car_13_n_level = sig_13_n_level		
	car_14_n_level = sig_14_n_level	
	car_15_n_level = sig_15_n_level
	car_16_n_level = sig_16_n_level
	
	car_1_w_level = sig_1_w_level
	car_2_w_level = sig_2_w_level
	car_3_w_level = sig_3_w_level
	car_4_w_level = sig_4_w_level    	

	car_5_w_level = sig_5_w_level
	car_6_w_level = sig_6_w_level
	car_7_w_level = sig_7_w_level
	car_8_w_level = sig_8_w_level
	
	car_9_w_level = sig_9_w_level
	car_10_w_level = sig_10_w_level
	car_11_w_level = sig_11_w_level
	car_12_w_level = sig_12_w_level
	
	car_13_w_level = sig_13_w_level		
	car_14_w_level = sig_14_w_level	
	car_15_w_level = sig_15_w_level
	car_16_w_level = sig_16_w_level

	car_1_s_level = sig_1_s_level
	car_2_s_level = sig_2_s_level
	car_3_s_level = sig_3_s_level
	car_4_s_level = sig_4_s_level    	

	car_5_s_level = sig_5_s_level
	car_6_s_level = sig_6_s_level
	car_7_s_level = sig_7_s_level
	car_8_s_level = sig_8_s_level
	
	car_9_s_level = sig_9_s_level
	car_10_s_level = sig_10_s_level
	car_11_s_level = sig_11_s_level
	car_12_s_level = sig_12_s_level
	
	car_13_s_level = sig_13_s_level		
	car_14_s_level = sig_14_s_level	
	car_15_s_level = sig_15_s_level
	car_16_s_level = sig_16_s_level
	
	
	car_1_e_level = sig_1_e_level
	car_2_e_level = sig_2_e_level
	car_3_e_level = sig_3_e_level
	car_4_e_level = sig_4_e_level    	

	car_5_e_level = sig_5_e_level
	car_6_e_level = sig_6_e_level
	car_7_e_level = sig_7_e_level
	car_8_e_level = sig_8_e_level

	car_9_e_level = sig_9_e_level
	car_10_e_level = sig_10_e_level
	car_11_e_level = sig_11_e_level
	car_12_e_level = sig_12_e_level

	car_13_e_level = sig_13_e_level		
	car_14_e_level = sig_14_e_level	
	car_15_e_level = sig_15_e_level
	car_16_e_level = sig_16_e_level	


    	counter = 0

	while 1==1 :
	
		car_1_n_level = sig_1_n_level
		car_2_n_level = sig_2_n_level
		car_3_n_level = sig_3_n_level
		car_4_n_level = sig_4_n_level
		
		car_5_n_level = sig_5_n_level
		car_6_n_level = sig_6_n_level
		car_7_n_level = sig_7_n_level
		car_8_n_level = sig_8_n_level
		
		car_9_n_level = sig_9_n_level
		car_10_n_level = sig_10_n_level
		car_11_n_level = sig_11_n_level
		car_12_n_level = sig_12_n_level
		
		car_13_n_level = sig_13_n_level		
		car_14_n_level = sig_14_n_level	
		car_15_n_level = sig_15_n_level
		car_16_n_level = sig_16_n_level
		
		car_1_w_level = sig_1_w_level
		car_2_w_level = sig_2_w_level
		car_3_w_level = sig_3_w_level
		car_4_w_level = sig_4_w_level    	

		car_5_w_level = sig_5_w_level
		car_6_w_level = sig_6_w_level
		car_7_w_level = sig_7_w_level
		car_8_w_level = sig_8_w_level
	
		car_9_w_level = sig_9_w_level
		car_10_w_level = sig_10_w_level
		car_11_w_level = sig_11_w_level
		car_12_w_level = sig_12_w_level
	
		car_13_w_level = sig_13_w_level		
		car_14_w_level = sig_14_w_level	
		car_15_w_level = sig_15_w_level
		car_16_w_level = sig_16_w_level
		
		car_1_s_level = sig_1_s_level
		car_2_s_level = sig_2_s_level
		car_3_s_level = sig_3_s_level
		car_4_s_level = sig_4_s_level    	

		car_5_s_level = sig_5_s_level
		car_6_s_level = sig_6_s_level
		car_7_s_level = sig_7_s_level
		car_8_s_level = sig_8_s_level
	
		car_9_s_level = sig_9_s_level
		car_10_s_level = sig_10_s_level
		car_11_s_level = sig_11_s_level
		car_12_s_level = sig_12_s_level
	
		car_13_s_level = sig_13_s_level		
		car_14_s_level = sig_14_s_level	
		car_15_s_level = sig_15_s_level
		car_16_s_level = sig_16_s_level
		
		car_1_e_level = sig_1_e_level
		car_2_e_level = sig_2_e_level
		car_3_e_level = sig_3_e_level
		car_4_e_level = sig_4_e_level    	

		car_5_e_level = sig_5_e_level
		car_6_e_level = sig_6_e_level
		car_7_e_level = sig_7_e_level
		car_8_e_level = sig_8_e_level
	
		car_9_e_level = sig_9_e_level
		car_10_e_level = sig_10_e_level
		car_11_e_level = sig_11_e_level
		car_12_e_level = sig_12_e_level

		car_13_e_level = sig_13_e_level		
		car_14_e_level = sig_14_e_level	
		car_15_e_level = sig_15_e_level
		car_16_e_level = sig_16_e_level
				
		if counter==1000:
			for s in signal:
				s.cir[s.active_signal].setFill("red")    	
				s.active_signal = (s.active_signal+1)%4
				s.cir[s.active_signal].setFill("green")	
			counter = 0
		
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(1,win)				
			car_list_1.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):		
			car=makecar(2,win)				
			car_list_2.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(3,win)				
			car_list_3.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(4,win)				
			car_list_4.append(car)
			
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(5,win)				
			car_list_5.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):		
			car=makecar(6,win)				
			car_list_6.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(7,win)				
			car_list_7.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(8,win)				
			car_list_8.append(car)	
			
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(9,win)				
			car_list_9.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):		
			car=makecar(10,win)				
			car_list_10.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(11,win)				
			car_list_11.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(12,win)				
			car_list_12.append(car)	
			
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(13,win)				
			car_list_13.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):		
			car=makecar(14,win)				
			car_list_14.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(15,win)				
			car_list_15.append(car)
		if counter%100==0 and bool(random.getrandbits(1)):
			car=makecar(16,win)				
			car_list_16.append(car)	
	
		''' NORTH '''
	
		for car in car_list_1 :
			if car.body.getCenter().getY()<sig_1_n_level and signal[0].active_signal!=3 and car_1_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_1_n_level=car_1_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_5_n_level and signal[4].active_signal!=3 and car_5_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_5_n_level=car_5_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_9_n_level and signal[8].active_signal!=3 and car_9_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_9_n_level=car_9_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_13_n_level and signal[12].active_signal!=3 and car_13_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_13_n_level=car_13_n_level-20			
				continue
			car.body.move(0,1)
		for car in car_list_2 :
			if car.body.getCenter().getY()<sig_2_n_level and signal[1].active_signal!=3 and car_2_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_2_n_level=car_2_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_6_n_level and signal[5].active_signal!=3 and car_6_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_6_n_level=car_6_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_10_n_level and signal[9].active_signal!=3 and car_10_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_10_n_level=car_10_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_14_n_level and signal[13].active_signal!=3 and car_14_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_14_n_level=car_14_n_level-20		
				continue	
			car.body.move(0,1)
		for car in car_list_3 :
			if car.body.getCenter().getY()<sig_3_n_level and signal[2].active_signal!=3 and car_3_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_3_n_level=car_3_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_7_n_level and signal[6].active_signal!=3 and car_7_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_7_n_level=car_7_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_11_n_level and signal[10].active_signal!=3 and car_11_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_11_n_level=car_11_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_15_n_level and signal[14].active_signal!=3 and car_15_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_15_n_level=car_15_n_level-20		
				continue		
			car.body.move(0,1)
		for car in car_list_4 :
			if car.body.getCenter().getY()<sig_4_n_level and signal[3].active_signal!=3 and car_4_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_4_n_level=car_4_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_8_n_level and signal[7].active_signal!=3 and car_8_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_8_n_level=car_8_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_12_n_level and signal[11].active_signal!=3 and car_12_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_12_n_level=car_12_n_level-20			
				continue
			if car.body.getCenter().getY()<sig_16_n_level and signal[15].active_signal!=3 and car_16_n_level-car.body.getCenter().getY() <= 10:
				car.counter+=1			
				car_16_n_level=car_16_n_level-20			
				continue			
			car.body.move(0,1)
			
			
		''' WEST'''
		
		for car in car_list_5 :
			if car.body.getCenter().getX()<sig_1_w_level and signal[0].active_signal!=0 and car_1_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_1_w_level=car_1_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_2_w_level and signal[1].active_signal!=0 and car_2_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_2_w_level=car_2_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_3_w_level and signal[2].active_signal!=0 and car_3_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_3_w_level=car_3_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_4_w_level and signal[3].active_signal!=0 and car_4_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_4_w_level=car_4_w_level-20			
				continue
			car.body.move(1,0)
		
		for car in car_list_6 :
			if car.body.getCenter().getX()<sig_5_w_level and signal[4].active_signal!=0 and car_5_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_5_w_level=car_5_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_6_w_level and signal[5].active_signal!=0 and car_6_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_6_w_level=car_6_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_7_w_level and signal[6].active_signal!=0 and car_7_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_7_w_level=car_7_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_8_w_level and signal[7].active_signal!=0 and car_8_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_8_w_level=car_8_w_level-20		
				continue	
			car.body.move(1,0)
		for car in car_list_7 :
			if car.body.getCenter().getX()<sig_9_w_level and signal[8].active_signal!=0 and car_9_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_9_w_level=car_9_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_10_w_level and signal[9].active_signal!=0 and car_10_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_10_w_level=car_10_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_11_w_level and signal[10].active_signal!=0 and car_11_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_11_w_level=car_11_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_12_w_level and signal[11].active_signal!=0 and car_12_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_12_w_level=car_12_w_level-20		
				continue		
			car.body.move(1,0)
		for car in car_list_8 :
			if car.body.getCenter().getX()<sig_13_w_level and signal[12].active_signal!=0 and car_13_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_13_w_level=car_13_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_14_w_level and signal[13].active_signal!=0 and car_14_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_14_w_level=car_14_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_15_w_level and signal[14].active_signal!=0 and car_15_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_15_w_level=car_15_w_level-20			
				continue
			if car.body.getCenter().getX()<sig_16_w_level and signal[15].active_signal!=0 and car_16_w_level-car.body.getCenter().getX() <= 10:
				car.counter+=1			
				car_16_w_level=car_16_w_level-20			
				continue			
			car.body.move(1,0)
		
		
		''' SOUTH '''
		
		for car in car_list_9 :
			if car.body.getCenter().getY()>sig_1_s_level and signal[0].active_signal!=1 and car.body.getCenter().getY()-car_1_s_level <= 10:
				car.counter+=1			
				car_1_s_level=car_1_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_5_s_level and signal[4].active_signal!=1 and car.body.getCenter().getY()-car_5_s_level <= 10:
				car.counter+=1			
				car_5_s_level=car_5_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_9_s_level and signal[8].active_signal!=1 and car.body.getCenter().getY()-car_9_s_level <= 10:
				car.counter+=1			
				car_9_s_level=car_9_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_13_s_level and signal[12].active_signal!=1 and car.body.getCenter().getY()-car_13_s_level <= 10:
				car.counter+=1			
				car_13_s_level=car_13_s_level+20			
				continue
			car.body.move(0,-1)
		for car in car_list_10 :
			if car.body.getCenter().getY()>sig_2_s_level and signal[1].active_signal!=1 and car.body.getCenter().getY()-car_2_s_level <= 10:
				car.counter+=1			
				car_2_s_level=car_2_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_6_s_level and signal[5].active_signal!=1 and car.body.getCenter().getY()-car_6_s_level <= 10:
				car.counter+=1			
				car_6_s_level=car_6_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_10_s_level and signal[9].active_signal!=1 and car.body.getCenter().getY()-car_10_s_level <= 10:
				car.counter+=1			
				car_10_s_level=car_10_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_14_s_level and signal[13].active_signal!=1 and car.body.getCenter().getY()-car_14_s_level <= 10:
				car.counter+=1			
				car_14_s_level=car_14_s_level+20		
				continue	
			car.body.move(0,-1)
		for car in car_list_11 :
			if car.body.getCenter().getY()>sig_3_s_level and signal[2].active_signal!=1 and car.body.getCenter().getY()-car_3_s_level <= 10:
				car.counter+=1			
				car_3_s_level=car_3_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_7_s_level and signal[6].active_signal!=1 and car.body.getCenter().getY()-car_7_s_level <= 10:
				car.counter+=1			
				car_7_s_level=car_7_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_11_s_level and signal[10].active_signal!=1 and car.body.getCenter().getY()-car_11_s_level <= 10:
				car.counter+=1			
				car_11_s_level=car_11_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_15_s_level and signal[14].active_signal!=1 and car.body.getCenter().getY()-car_15_s_level <= 10:
				car.counter+=1			
				car_15_s_level=car_15_s_level+20		
				continue		
			car.body.move(0,-1)
		for car in car_list_12 :
			if car.body.getCenter().getY()>sig_4_s_level and signal[3].active_signal!=1 and car.body.getCenter().getY()-car_4_s_level <= 10:
				car.counter+=1			
				car_4_s_level=car_4_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_8_s_level and signal[7].active_signal!=1 and car.body.getCenter().getY()-car_8_s_level <= 10:
				car.counter+=1			
				car_8_s_level=car_8_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_12_s_level and signal[11].active_signal!=1 and car.body.getCenter().getY()-car_12_s_level <= 10:
				car.counter+=1			
				car_12_s_level=car_12_s_level+20			
				continue
			if car.body.getCenter().getY()>sig_16_s_level and signal[15].active_signal!=1 and car.body.getCenter().getY()-car_16_s_level <= 10:
				car.counter+=1			
				car_16_s_level=car_16_s_level+20			
				continue			
			car.body.move(0,-1)
		
		''' EAST  '''
		
		for car in car_list_13 :
			if car.body.getCenter().getX()>sig_1_e_level and signal[0].active_signal!=2 and car.body.getCenter().getX()-car_1_e_level <= 10:
				car.counter+=1			
				car_1_e_level=car_1_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_2_e_level and signal[1].active_signal!=2 and car.body.getCenter().getX()-car_2_e_level <= 10:
				car.counter+=1			
				car_2_e_level=car_2_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_3_e_level and signal[2].active_signal!=2 and car.body.getCenter().getX()-car_3_e_level <= 10:
				car.counter+=1			
				car_3_e_level=car_3_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_4_e_level and signal[3].active_signal!=2 and car.body.getCenter().getX()-car_4_e_level <= 10:
				car.counter+=1			
				car_4_e_level=car_4_e_level+20			
				continue
			car.body.move(-1,0)
		
		for car in car_list_14 :
			if car.body.getCenter().getX()>sig_5_e_level and signal[4].active_signal!=2 and car.body.getCenter().getX()-car_5_e_level  <= 10:
				car.counter+=1			
				car_5_e_level=car_5_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_6_e_level and signal[5].active_signal!=2 and car.body.getCenter().getX()-car_6_e_level  <= 10:
				car.counter+=1			
				car_6_e_level=car_6_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_7_e_level and signal[6].active_signal!=2 and car.body.getCenter().getX()-car_7_e_level <= 10:
				car.counter+=1			
				car_7_e_level=car_7_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_8_e_level and signal[7].active_signal!=2 and car.body.getCenter().getX()-car_8_e_level <= 10:
				car.counter+=1			
				car_8_e_level=car_8_e_level+20		
				continue	
			car.body.move(-1,0)
		for car in car_list_15 :
			if car.body.getCenter().getX()>sig_9_e_level and signal[8].active_signal!=2 and car.body.getCenter().getX()-car_9_e_level <= 10:
				car.counter+=1			
				car_9_e_level=car_9_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_10_e_level and signal[9].active_signal!=2 and car.body.getCenter().getX()-car_10_e_level  <= 10:
				car.counter+=1			
				car_10_e_level=car_10_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_11_e_level and signal[10].active_signal!=2 and car.body.getCenter().getX()-car_11_e_level  <= 10:
				car.counter+=1			
				car_11_e_level=car_11_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_12_e_level and signal[11].active_signal!=2 and car.body.getCenter().getX()-car_12_e_level <= 10:
				car.counter+=1			
				car_12_e_level=car_12_e_level+20		
				continue		
			car.body.move(-1,0)
		for car in car_list_16 :
			if car.body.getCenter().getX()>sig_13_e_level and signal[12].active_signal!=2 and car.body.getCenter().getX()-car_13_e_level  <= 10:
				car.counter+=1			
				car_13_e_level=car_13_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_14_e_level and signal[13].active_signal!=2 and car.body.getCenter().getX()-car_14_e_level  <= 10:
				car.counter+=1			
				car_14_e_level=car_14_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_15_e_level and signal[14].active_signal!=2 and car.body.getCenter().getX()-car_15_e_level  <= 10:
				car.counter+=1			
				car_15_e_level=car_15_e_level+20			
				continue
			if car.body.getCenter().getX()>sig_16_e_level and signal[15].active_signal!=2 and car.body.getCenter().getX()-car_16_e_level  <= 10:
				car.counter+=1			
				car_16_e_level=car_16_e_level+20			
				continue			
			car.body.move(-1,0)
		
		


		time.sleep(0.01)
		counter=counter+1

	
	win.getMouse()		
    	time.sleep(3)
        win.close()
	
	

main()



