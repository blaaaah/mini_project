#IMPORTS
import matplotlib.pyplot as plt
from math import *
import time	
import random
import subprocess as sp
from graphics import *
import ip
import numpy
import threading


#GLOBAL VARIABLES
n_den = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
s_den = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
e_den = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
w_den = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

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
cir = []

checker = False
checker2 = False

n_ptr=0
s_ptr=2
e_ptr=1
w_ptr=3

timer_val=3
c=0
active_signal = 0
car_w=[]


def const():
	global checker
	global c
	c=c+1
	checker = True
	threading.Timer(timer_val+1,const).start()

def cdf():
	#GLOBAL
	global car_list_n
	global car_list_e
	global car_list_w
	global car_list_s 

	global car_list_nl
	global car_list_el
	global car_list_wl
	global car_list_sl

	global checker
	
	global car_list_nr
	global car_list_er
	global car_list_wr
	global car_list_sr

	global car_w_time 
	global cir
	global c
	global active_signal


	c=c+1			#TO COUNT CYCLES
	position = []   #TO STORE CENTERS
	
	#GET CENTERS OF ALL CARS FOR IP
	for car in car_list_n:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_nl:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_nr:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	
	
	for car in car_list_s:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_sl:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_sr:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	
	
	for car in car_list_w:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_wl:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_wr:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())	


	for car in car_list_e:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_el:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	for car in car_list_er:
		p = car_pos()
		p.p[0] = car.body.getCenter().getX()
		p.p[1] = car.body.getCenter().getY()
		position.append(p.get_pos())
	
	

	ip.image_processing(position)

	del position

	ip.print_density()
	
   	
   	checker = True		#CHANGE TRAFFIC LIGHT IN GUI THREAD
	
	mycode()
	
def mycode():

	#GLOBAL
	global active_signal
	global next_active_signal
	global n_den
	global s_den
	global e_den
	global w_den

	global n_ptr
	global s_ptr
	global e_ptr
	global w_ptr
	global timer_val
	global c
							
	for j in range(3):
		n_den[n_ptr][j] = n_den[n_ptr][j+1]
		w_den[w_ptr][j] = w_den[w_ptr][j+1]
		s_den[s_ptr][j] = s_den[s_ptr][j+1]
		e_den[e_ptr][j] = e_den[e_ptr][j+1]

	n_den[n_ptr][3] = ip.n_density
	w_den[w_ptr][3] = ip.w_density
	s_den[s_ptr][3] = ip.s_density
	e_den[e_ptr][3] = ip.e_density
	
	ip.init_density()
	
	n_ptr=(n_ptr+1)%4
	s_ptr=(s_ptr+1)%4
	w_ptr=(w_ptr+1)%4
	e_ptr=(e_ptr+1)%4
	
	
	print 'w_den' , w_den
	print 's_den' , s_den
	print 'e_den' , e_den
	print 'n_den' , n_den
	
	if c>12:
		adjn=numpy.mean(n_den[3][:-1])-numpy.mean(n_den[n_ptr][:-1])
		adjw=numpy.mean(w_den[3][:-1])-numpy.mean(w_den[w_ptr][:-1])
		adjs=numpy.mean(s_den[3][:-1])-numpy.mean(s_den[s_ptr][:-1])
		adje=numpy.mean(e_den[3][:-1])-numpy.mean(e_den[e_ptr][:-1])
		
		avg = float (( n_den[n_ptr][3] + adjn + w_den[w_ptr][3] + adjw + s_den[s_ptr][3] + adjs + e_den[e_ptr][3] + adje ) / 4)
		
		if active_signal == -1:
			signal = next_active_signal
		else:
			signal = active_signal
		if (signal == 2):
			rd = float(n_den[(n_ptr-1)%4][3] / avg)
		elif (signal == 3):
			rd = float(w_den[(w_ptr-1)%4][3] / avg)
		elif (signal == 0):
			rd = float(s_den[(s_ptr-1)%4][3] / avg)
		elif (signal == 1):
			rd = float(e_den[(e_ptr-1)%4][3] / avg)
		
		print "ADJN",adjn
		print "ADJS",adjs
		print "ADJW",adjw
		print "ADJE",adje
		
		
		print "RELATIVE DENSITY", rd
		
		expden = float(( numpy.mean(n_den[3][:-1])+numpy.mean(s_den[3][:-1])+numpy.mean(e_den[3][:-1])+numpy.mean(w_den[3][:-1]) ) / 4 )
		print "Expected DENSITY", expden
		cr = 5
		l = 3
		timer_val = ( (rd * expden) / (l * cr) )
		if timer_val == 0:
			timer_val = 3
	else:
		timer_val = 3
	
	print "TIMER VALUE = ",timer_val
	threading.Timer(timer_val+1,cdf).start()


def changelight():
	global checker2
	checker2 = True

def func(win,h,w,counter,cir,n_level,w_level,s_level,e_level):

	#GLOBAL VARIABLES
    global car_list_n
    global car_list_e
    global car_list_w
    global car_list_s 

    global car_list_nl
    global car_list_el
    global car_list_wl
    global car_list_sl

    global active_signal
    global next_active_signal
    global car_list_nr
    global car_list_er
    global car_list_wr
    global car_list_sr

    global car_w_time 


    global timer_val
    global c
    global checker
    global checker2

    fo  = open("random.txt","r")
    while 1==1:
		
			
	#Generate cars randomly
	if counter%80==0 and bool( int(fo.read(1)) ):
		car=makecar('n',win)				
		car_list_n.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):		
		car=makecar('s',win)				
		car_list_s.append(car)
	if counter%200==0 and bool( int(fo.read(1)) ):
		car=makecar('w',win)				
		car_list_w.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):
		car=makecar('e',win)				
		car_list_e.append(car)
	if counter%80==0 and bool( int(fo.read(1)) ):
		car=makecar('nl',win)				
		car_list_nl.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):		
		car=makecar('sl',win)				
		car_list_sl.append(car)
	if counter%200==0 and bool( int(fo.read(1)) ):
		car=makecar('wl',win)				
		car_list_wl.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):
		car=makecar('el',win)				
		car_list_el.append(car)
	if counter%80==0 and bool( int(fo.read(1)) ):
		car=makecar('nr',win)				
		car_list_nr.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):		
		car=makecar('sr',win)				
		car_list_sr.append(car)	
	if counter%200==0 and bool( int(fo.read(1)) ):
		car=makecar('wr',win)				
		car_list_wr.append(car)
	if counter%100==0 and bool( int(fo.read(1)) ):
		car=makecar('er',win)				
		car_list_er.append(car)
	

	#Update all car levels 
     
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

	#CHANGE GREEN LIGHT TO RED 
	if checker == True:
		cir[active_signal].setFill("red")
		next_active_signal = (active_signal+1)%4 
		active_signal = -1
		cir[next_active_signal].setFill("orange")
		checker = False
		threading.Timer(1, changelight).start()  #TRANSITION TIME B/W SIGNAL

	#CHANGE RED LIGHT TO GREEN
	if checker2 == True:
		cir[next_active_signal].setFill("green")
		active_signal = next_active_signal
		next_active_signal = -1
		checker2 = False


	#UPDATE CAR POSITION
	for car in car_list_n:
		if car.body.getCenter().getY()>h+20:
			car_w_time.append(car.counter)
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
			
			car_list_s.remove(car)
			continue			
		if car.body.getCenter().getY()>s_level and active_signal!=1 and car.body.getCenter().getY()-car_s_level <= 10:
			car.counter+=1			
			car_s_level=car_s_level+20			
			continue		
		car.body.move(0,-1)
	for car in car_list_e:		
		if car.body.getCenter().getX()<-20:
			
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
			
			car_list_sl.remove(car)
			continue			
		if car.body.getCenter().getY()>s_level and active_signal!=1 and car.body.getCenter().getY()-car_sl_level <= 10:
			car.counter+=1			
			car_sl_level=car_sl_level+20			
			continue		
		car.body.move(0,-1)
	for car in car_list_el:		
		if car.body.getCenter().getX()<-20:
			
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
			
			car_w_time.append(car.counter)
			car_list_wl.remove(car)
			continue			
		if car.body.getCenter().getX()<w_level and active_signal!=0 and car_wl_level-car.body.getCenter().getX() <= 10:
			car.counter+=1			
			car_wl_level=car_wl_level-20			
			continue		
		car.body.move(1,0)
	
		
		
	for car in car_list_nr:
		if car.body.getCenter().getX()<-20:
			car_w_time.append(car.counter)
			
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
		if car.body.getCenter().getX()>w+20:
			car_w_time.append(car.counter)
			
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
		if car.body.getCenter().getY()<-20:
			
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
		if car.body.getCenter().getY()>h+20:
			
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
	

	
	
	counter=counter+1
	
	#START COUNTING WAITING TIME ONCE ALGORITHM KICKS IN !!NOTE - COMMENT OUT FOR FIXED TIMER
	if c==4:
		for car in car_list_nr:
			car.counter=0
		for car in car_list_sr:
			car.counter=0
		for car in car_list_wr:
			car.counter=0
		for car in car_list_er:
			car.counter=0
		for car in car_list_nl:
			car.counter=0
		for car in car_list_sl:
			car.counter=0
		for car in car_list_wl:
			car.counter=0
		for car in car_list_el:
			car.counter=0
		for car in car_list_n:
			car.counter=0
		for car in car_list_s:
			car.counter=0
		for car in car_list_e:
			car.counter=0
		for car in car_list_w:
			car.counter=0

	#PRINT STANDARD DEVIATION
	if c==40:
		print "-----------------------------------------"
		print "MEAN = ",numpy.mean(car_w_time)
		print "STANDARD DEVIATION = ",numpy.std(car_w_time)
		print "-----------------------------------------"
		win.close()
		plot_graph(car_w_time)
	  



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

class car_pos:
	def __init__(self):
		self.p = []
		self.p.append(0)
		self.p.append(0)
	def get_pos(self):
		return self.p

class makecar:

	def __init__(self,d,win):
		self.counter = 0
		self.ang = 0
		if d=='n':
	    		cx = win.getWidth()/2 +50
			cy = -500
		elif d=='s':			
			cx = win.getWidth()/2 -50
			cy = win.getHeight() + 500
		elif d=='e':
			cx = win.getWidth() + 500 
			cy = win.getHeight()/2 +50
		elif d=='w':
			cx = -500
			cy = win.getHeight()/2 -50
		elif d=='nr':
	    		cx = win.getWidth()/2 - 25 +50
			cy = -500
		elif d=='sr':			
			cx = win.getWidth()/2 + 25 -50
			cy = win.getHeight() + 500
		elif d=='er':
			cx = win.getWidth() + 500
			cy = win.getHeight()/2 - 25 +50
		elif d=='wr':
			cx = -500
			cy = win.getHeight()/2 + 25 -50
		elif d=='nl':
	    		cx = win.getWidth()/2 + 25 +50
			cy = -500
		elif d=='sl':			
			cx = win.getWidth()/2 - 25 -50
			cy = win.getHeight() + 500
		elif d=='el':
			cx = win.getWidth() + 500
			cy = win.getHeight()/2 + 25 +50
		elif d=='wl':
			cx = -500
			cy = win.getHeight()/2 - 25 -50

	 	self.body = Rectangle(Point(cx-5, cy-5), Point(cx+5, cy+5))
		self.body.setFill("white")
 		self.body.draw(win)



def plot_graph(car_w):
	
	
	fig = plt.figure(0)
	fig.canvas.set_window_title('Waiting_time graph')

	car_w.sort()		

	
	plt.plot(car_w)
	plt.ylabel('waiting time') 
	plt.show()
	plt.close()
	
	

def main():

    #GLOBAL VARIABLES
    global active_signal
    global n_den
    global s_den
    global e_den
    global w_den

    global n_ptr
    global s_ptr
    global e_ptr
    global w_ptr
    global timer_val			
    global car_list_n
    global car_list_e
    global car_list_w
    global car_list_s 
    
    global car_list_nl
    global car_list_el
    global car_list_wl
    global car_list_sl
    
    global car_list_nr
    global car_list_er
    global car_list_wr
    global car_list_sr
    
    global car_w_time 
	
    #DRAW SCENE
    win = GraphWin('Simulator', 1000, 1000)
	
    w=win.getWidth()
    h=win.getHeight()
    
    rect = Rectangle(Point(0, h/2-100), Point(w, h/2+100))
    rect.setFill("black")
    rect.draw(win)

    rect = Rectangle(Point(w/2-100, 0), Point(w/2+100, h))
    rect.setFill("black")
    rect.draw(win)
    
    	

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
    
	
    global cir 
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
    prev_active_signal = 0
    flag = True

    
    threading.Timer(timer_val, cdf).start()			#VARIABLE TIMER
    #threading.Timer(timer_val, const).start()			#FIXED TIMER
    func(win,h,w,counter,cir,n_level,w_level,s_level,e_level)
 
    fo.close()
    win.getMouse()		
    time.sleep(3)
    win.close()


main() 
plot_graph()

