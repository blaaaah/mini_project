import matplotlib.pyplot as plt
from math import *
import time	
import random
import subprocess as sp
from graphics import *


car_w=[]

def rotateX(x1,y1,x2,y2,theta):
	ang=radians(theta)
	xa=x1+(x2-x1)*cos(ang)-(y2-y1)*sin(ang)
	ya=y1+(y2-y1)*cos(ang)+(x2-x1)*sin(ang)
	return xa
	
def rotateY(x1,y1,x2,y2,theta):
	ang=radians(theta)
	xa=x1+(x2-x1)*cos(ang)-(y2-y1)*sin(ang)
	ya=y1+(y2-y1)*cos(ang)+(x2-x1)*sin(ang)
	return ya

class makecar:

	def __init__(self,d,win):
		self.counter = 0
		self.ang = 0
		if d=='n':
	    		cx = win.getWidth()/2 +50
			cy = -100
		elif d=='s':			
			cx = win.getWidth()/2 -50
			cy = win.getHeight() + 100
		elif d=='e':
			cx = win.getWidth() + 100 
			cy = win.getHeight()/2 +50
		elif d=='w':
			cx = -100
			cy = win.getHeight()/2 -50
		elif d=='nr':
	    		cx = win.getWidth()/2 - 25 +50
			cy = -100
		elif d=='sr':			
			cx = win.getWidth()/2 + 25 -50
			cy = win.getHeight() + 100
		elif d=='er':
			cx = win.getWidth() + 100
			cy = win.getHeight()/2 - 25 +50
		elif d=='wr':
			cx = -100
			cy = win.getHeight()/2 + 25 -50
		elif d=='nl':
	    		cx = win.getWidth()/2 + 25 +50
			cy = -100
		elif d=='sl':			
			cx = win.getWidth()/2 - 25 -50
			cy = win.getHeight() + 100
		elif d=='el':
			cx = win.getWidth() + 100
			cy = win.getHeight()/2 + 25 +50
		elif d=='wl':
			cx = -100
			cy = win.getHeight()/2 - 25 -50

	 	self.body = Rectangle(Point(cx-5, cy-5), Point(cx+5, cy+5))
		self.body.setFill("white")
 		self.body.draw(win)



def plot_graph(car_w):
	print 'car_w'
	print car_w

	fig = plt.figure(0)
	fig.canvas.set_window_title('Waiting_time graph')

	car_w.sort()		
	print car_w
	
	plt.plot(car_w)
	plt.ylabel('waiting time') 
	plt.show()
	plt.close()
	
	

def main():

    win = GraphWin('Simulator', 1200, 700)
   
    c=0
	
    w=win.getWidth()
    h=win.getHeight()
    
    rect = Rectangle(Point(0, h/2-100), Point(w, h/2+100))
    rect.setFill("black")
    rect.draw(win)

    rect = Rectangle(Point(w/2-100, 0), Point(w/2+100, h))
    rect.setFill("black")
    rect.draw(win)
    
    car_list_n = []
    car_list_e = []
    car_list_w = []
    car_list_s = []
    
    car_list_nl = []
    car_list_el = []
    car_list_wl = []
    car_list_sl = []
    
    car_list_nr = []
    car_list_er = []
    car_list_wr = []
    car_list_sr = []
    
    car_w_time = []

    n_level = h/2 - 50 - 50	
    s_level = h/2 + 50 + 50
    e_level = w/2 + 50 + 50
    w_level = w/2 - 50 - 50

    car_n_level = n_level
    car_s_level = s_level
    car_e_level = e_level
    car_w_level = w_level
    
    car_nl_level = n_level
    car_sl_level = s_level
    car_el_level = e_level
    car_wl_level = w_level
    
    car_nr_level = n_level
    car_sr_level = s_level
    car_er_level = e_level
    car_wr_level = w_level
    
	
    cir = []
    active_signal = 3
    cir.append(Circle(Point(w/2-100,h/2-100), 5))
    cir[0].setFill("red")
    cir[0].draw(win)

    cir.append(Circle(Point(w/2-100,h/2+100), 5))
    cir[1].setFill("red")
    cir[1].draw(win)

    cir.append(Circle(Point(w/2+100,h/2+100), 5))
    cir[2].setFill("red")
    cir[2].draw(win)

    cir.append(Circle(Point(w/2+100,h/2-100), 5))
    cir[3].setFill("green")
    cir[3].draw(win)

    counter = 0

    while 1==1:
    
    	
	if counter==1000:	
		cir[active_signal].setFill("red")    	
		active_signal = (active_signal+1)%4
		cir[active_signal].setFill("green")
		if active_signal==3:
			car_n_level=n_level
		elif active_signal==0:
			car_e_level=e_level
		elif active_signal==1:
			car_s_level=s_level
		else:
			car_w_level=w_level
		counter=0
		c+=1
	
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('n',win)				
		car_list_n.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):		
		car=makecar('s',win)				
		car_list_s.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('w',win)				
		car_list_w.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('e',win)				
		car_list_e.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('nl',win)				
		car_list_nl.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):		
		car=makecar('sl',win)				
		car_list_sl.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('wl',win)				
		car_list_wl.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('el',win)				
		car_list_el.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('nr',win)				
		car_list_nr.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):		
		car=makecar('sr',win)				
		car_list_sr.append(car)
		print 'made car sr'
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('wr',win)				
		car_list_wr.append(car)
	if counter%300==0 and bool(random.getrandbits(1)):
		car=makecar('er',win)				
		car_list_er.append(car)
	
	#Update all cars
     
        car_n_level = n_level
        car_s_level = s_level
        car_e_level = e_level
        car_w_level = w_level
        
        car_nl_level = n_level
    	car_sl_level = s_level
    	car_el_level = e_level
    	car_wl_level = w_level

	car_nr_level = n_level
    	car_sr_level = s_level
    	car_er_level = e_level
    	car_wr_level = w_level

	


	for car in car_list_n:
		if car.body.getCenter().getY()>h+20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_n.remove(car)
			continue
		if car.body.getCenter().getY()<n_level and active_signal!=3 and car_n_level-car.body.getCenter().getY() <= 10:
			car.counter+=1			
			car_n_level=car_n_level-20			
			continue		
		car.body.move(0,1)
	for car in car_list_s:		
		if car.body.getCenter().getY()<-20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_s.remove(car)
			continue			
		if car.body.getCenter().getY()>s_level and active_signal!=1 and car.body.getCenter().getY()-car_s_level <= 10:
			car.counter+=1			
			car_s_level=car_s_level+20			
			continue		
		car.body.move(0,-1)
	for car in car_list_e:		
		if car.body.getCenter().getX()<-20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_e.remove(car)
			continue			
		if car.body.getCenter().getX()>e_level and active_signal!=2 and car.body.getCenter().getX()-car_e_level <= 10:
			car_e_level=car_e_level+20
			car.counter+=1			
			continue		
		car.body.move(-1,0)
	for car in car_list_w:
		if car.body.getCenter().getX()>w+20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_w.remove(car)
			continue			
		if car.body.getCenter().getX()<w_level and active_signal!=0 and car_w_level-car.body.getCenter().getX() <= 10:
			car.counter+=1			
			car_w_level=car_w_level-20			
			continue		
		car.body.move(1,0)
		
		
	for car in car_list_nl:
		if car.body.getCenter().getY()>h+20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_nl.remove(car)
			continue
		if car.body.getCenter().getY()<n_level and active_signal!=3 and car_nl_level-car.body.getCenter().getY() <= 10:
			car.counter+=1			
			car_nl_level=car_nl_level-20			
			continue		
		car.body.move(0,1)
	for car in car_list_sl:		
		if car.body.getCenter().getY()<-20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_sl.remove(car)
			continue			
		if car.body.getCenter().getY()>s_level and active_signal!=1 and car.body.getCenter().getY()-car_sl_level <= 10:
			car.counter+=1			
			car_sl_level=car_sl_level+20			
			continue		
		car.body.move(0,-1)
	for car in car_list_el:		
		if car.body.getCenter().getX()<-20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_el.remove(car)
			continue			
		if car.body.getCenter().getX()>e_level and active_signal!=2 and car.body.getCenter().getX()-car_el_level <= 10:
			car_el_level=car_el_level+20
			car.counter+=1			
			continue		
		car.body.move(-1,0)
	for car in car_list_wl:
		if car.body.getCenter().getX()>w+20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_wl.remove(car)
			continue			
		if car.body.getCenter().getX()<w_level and active_signal!=0 and car_wl_level-car.body.getCenter().getX() <= 10:
			car.counter+=1			
			car_wl_level=car_wl_level-20			
			continue		
		car.body.move(1,0)
	
		
		
	for car in car_list_nr:
		if car.body.getCenter().getY()>h+20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_nr.remove(car)
			continue
		if car.body.getCenter().getY()<n_level and active_signal!=3 and car_nr_level-car.body.getCenter().getY() <= 10:
			car.counter+=1			
			car_nr_level=car_nr_level-20			
			continue	
				
		if(car.body.getCenter().getY()<n_level):
			car.body.move(0,1)
		if(car.body.getCenter().getY()>=n_level and car.body.getCenter().getX()>w_level):
			x = rotateX(w/2-100,h/2-100,w/2 - 25 + 50,h/2 - 100,car.ang)
			y = rotateY(w/2-100,h/2-100,w/2 - 25 + 50,h/2 - 100,car.ang)
			car.body.move(-1*abs(x-car.body.getCenter().getX()),abs(y-car.body.getCenter().getY()))
			car.ang+=1
		if(car.body.getCenter().getX()<=w_level):
			car.body.move(-1,0)	
		
	for car in car_list_sr:		
		if car.body.getCenter().getY()<-20:
			car_w_time.append(car.counter)
			print car.counter
			car_list_sr.remove(car)
			continue			
		if car.body.getCenter().getY()>s_level and active_signal!=1 and car.body.getCenter().getY()-car_sr_level <= 10:
			car.counter+=1			
			car_sr_level=car_sr_level+20			
			continue	
			
		if(car.body.getCenter().getY()>s_level):
			car.body.move(0,-1)
		if(car.body.getCenter().getX()<e_level and car.body.getCenter().getY()<=s_level):
			x = rotateX(w/2+100,h/2+100,w/2 + 25 -50,h/2+100,car.ang)
			y = rotateY(w/2+100,h/2+100,w/2 + 25 -50,h/2+100,car.ang)
			car.body.move(abs(x-car.body.getCenter().getX()),-1*abs(y-car.body.getCenter().getY()))
			car.ang+=1
		if(car.body.getCenter().getX()>=e_level):
			car.body.move(1,0)
					
	for car in car_list_er:		
		if car.body.getCenter().getX()<-20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_er.remove(car)
			continue			
		if car.body.getCenter().getX()>e_level and active_signal!=2 and car.body.getCenter().getX()-car_er_level <= 10:
			car_er_level=car_er_level+20
			car.counter+=1			
			continue		
		
		if(car.body.getCenter().getX()>e_level):
			car.body.move(-1,0)
		if(car.body.getCenter().getX()<=e_level and car.body.getCenter().getY()>n_level):
			x = rotateX(w/2+100,h/2-100,w/2 + 100,h/2 - 25 + 50,car.ang)
			y = rotateY(w/2+100,h/2-100,w/2 + 100,h/2 - 25 + 50,car.ang)
			car.body.move(-1*abs(x-car.body.getCenter().getX()),-1*abs(y-car.body.getCenter().getY()))
			car.ang+=1
		if(car.body.getCenter().getY()<=n_level):
			car.body.move(0,-1)		
		
	for car in car_list_wr:
		if car.body.getCenter().getX()>w+20:
			print car.counter
			car_w_time.append(car.counter)
			car_list_wr.remove(car)
			continue			
		if car.body.getCenter().getX()<w_level and active_signal!=0 and car_wr_level-car.body.getCenter().getX() <= 10:
			car.counter+=1			
			car_wr_level=car_wr_level-20			
			continue		
		
		if(car.body.getCenter().getX()<w_level):
			car.body.move(1,0)
		if(car.body.getCenter().getX()>=w_level and car.body.getCenter().getY()<s_level):
			x = rotateX(w/2-100,h/2+100,w/2 - 100,h/2 + 25 - 50,car.ang)
			y = rotateY(w/2-100,h/2+100,w/2 - 100,h/2 + 25 - 50,car.ang)
			car.body.move(abs(x-car.body.getCenter().getX()),abs(y-car.body.getCenter().getY()))
			car.ang+=1
		if(car.body.getCenter().getY()>=s_level):
			car.body.move(0,1)	
	
	time.sleep(0.01)
	counter=counter+1
	
	
	
	if c==8:
		
		print'car_w_time'
		print car_w_time
		win.close()
		plot_graph(car_w_time)
	  	
	
    win.getMouse()		
    time.sleep(3)
    win.close()


main() 
plot_graph()
