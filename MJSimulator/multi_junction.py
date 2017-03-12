from graphics import *
import tlc
import scene   
import car_master 
import threading
from PIL import Image as NewImage
import random
import time

def main():

	counter=0
	car_list=[]

	win = scene.draw_scene()
	sig_list = scene.def_sig()
	scene.draw_signal(sig_list)
	w=win.getWidth()
	h=win.getHeight()

	for s in sig_list:
		threading.Timer(3, s.const).start()
	
	while 1==1:	
		
		for car in car_list:
			car.move()

		#Generate cars randomly
		if counter%100==0 and bool(random.getrandbits(1)):
			car=car_master.makecar(win)				
			car_list.append(car)

		for s in sig_list:
			if s.checker == True:
				s.change_sig()
				s.checker = False

		counter = counter+1
		time.sleep(0.005)

		


main()
