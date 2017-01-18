from graphics import *
import time	
import random
import subprocess as sp

def makecar(d,win):
    if d=='n':
    	cx = win.getWidth()/2 + 25
	cy = 0
    elif d=='s':
	cx = win.getWidth()/2 - 25
	cy = win.getHeight()
    elif d=='e':
	cx = win.getWidth()
	cy = win.getHeight()/2 + 25
    elif d=='w':
	cx = 0
	cy = win.getHeight()/2 - 25

    rect = Rectangle(Point(cx-15, cy-15), Point(cx+15, cy+15))
    rect.setFill("white")
    rect.draw(win)
    return rect

    


def main():
    win = GraphWin('Simulator', 1200, 700)
    w=win.getWidth()
    h=win.getHeight()
    
    rect = Rectangle(Point(0, h/2-50), Point(w, h/2+50))
    rect.setFill("black")
    rect.draw(win)

    rect = Rectangle(Point(w/2-50, 0), Point(w/2+50, h))
    rect.setFill("black")
    rect.draw(win)
    
    car_list_n = []
    car_list_e = []
    car_list_w = []
    car_list_s = []

    n_level = h/2 - 25 - 10	
    s_level = h/2 + 25 + 10
    e_level = w/2 + 25 + 10
    w_level = w/2 - 25 - 10

    car_n_level = n_level
    car_s_level = s_level
    car_e_level = e_level
    car_w_level = w_level
	
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
	
	if counter%100==0 and bool(random.getrandbits(1)):		
		car_list_n.append(makecar('n', win))
		car_list_e.append(makecar('e', win))
		car_list_w.append(makecar('w', win))
		car_list_s.append(makecar('s', win))
	
	#Update all cars
	car_n_level = n_level
    	car_s_level = s_level
    	car_e_level = e_level
    	car_w_level = w_level
	
	for car in car_list_n:
		if counter%100==0:			
			print car.getCenter().getY()," ",car_n_level		
		if car.getCenter().getY()<n_level and active_signal!=3 and car_n_level-car.getCenter().getY() <= 30 :
			car_n_level=car_n_level-40				
			print "n"	
			continue
					
		car.move(0,1)
		
	
	for car in car_list_s:
		if counter%100==0:
			print car.getCenter().getY()," ",car_s_level		
		if car.getCenter().getY()>s_level and active_signal!=1 and car.getCenter().getY()-car_s_level <= 30:
			print "s"
			car_s_level=car_s_level+40			
			continue		
		car.move(0,-1)
	for car in car_list_e:
		if counter%100==0:
			print car.getCenter().getX()," ",car_e_level			
		if car.getCenter().getX()>e_level and active_signal!=2 and car.getCenter().getX()-car_e_level <= 30:
			print "e"
			car_e_level=car_e_level+40			
			continue		
		car.move(-1,0)
	for car in car_list_w:
		if counter%100==0:
			print car.getCenter().getX()," ",car_w_level
		if car.getCenter().getX()<w_level and active_signal!=0 and car_w_level-car.getCenter().getX() <= 30:
			print "w"
			car_w_level=car_w_level-40			
			continue		
		car.move(1,0)
	 

	
	if counter%100==0:
		win.getMouse()
		sp.call('clear',shell=True)	
	time.sleep(0.01)
	counter=counter+1
    win.getMouse()
    win.close()


'''    cir1 = Circle(Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)
    
    cir2 = Circle(Point(w/2-100,h/2-100), 5)
    cir2.setFill("red")
    cir2.draw(win)
    for i in range(46):
        cir1.move(5, 0)
        time.sleep(.05)
    for i in range(46):
        cir1.move(-5, 0)
        time.sleep(.05)   '''

main()
