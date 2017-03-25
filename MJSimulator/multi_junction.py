from graphics import *
import tlc
import scene   
import car_gen_bhag as car_master 
import threading
from PIL import Image as NewImage
import random
import time

 #!/usr/bin/python
'''
import mysql.connector as mc 


# Open database connection
db = mc.connect("localhost","node","root","1234")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
cursor.close()
db.close()
'''
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
			if not car.move():
				del car

		#Generate cars randomly
		if counter%10==0 and bool(random.getrandbits(1)):
			car=car_master.makecar(win)				
			car_list.append(car)

		for s in sig_list:
			if s.checker == True:
				s.change_sig()
				s.checker = False

		counter = counter+1
		time.sleep(0.005)

		


main()
