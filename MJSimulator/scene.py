from graphics import *
import tlc
win = GraphWin('Simulator', 700, 700)
win.master.geometry('%dx%d+%d+%d' % (700, 700, 100, 50))
w=win.getWidth()
h=win.getHeight()
sig_list=[]

def ret_h():                              
	return h

def ret_w():
	return w
	
def ret_win():
	return win

# define the signals for all junctions
def def_sig():
	global sig_list
	for i in range(16):
		s = tlc.sLight(i+1)
		sig_list.append(s)
	return sig_list

def ret_sig_list():
	global sig_list
	return sig_list
	
# to draw the signals for all junctions
def draw_signal(sig_list):

	for s in sig_list:
	
		s.cir[0] = (Circle(Point(s.x - (w/18),s.y - (h/18)), 5))
		s.cir[0].setFill("red")
		s.cir[0].draw(win)

		s.cir[1] = (Circle(Point(s.x - (w/18),s.y + (h/18)), 5))
		s.cir[1].setFill("red")						
		s.cir[1].draw(win)

		s.cir[2] = (Circle(Point(s.x + (w/18),s.y + (h/18)), 5))
		s.cir[2].setFill("red")
		s.cir[2].draw(win)

		s.cir[3] = (Circle(Point(s.x + (w/18),s.y - (h/18)), 5))
		s.cir[3].setFill("red")
		s.cir[3].draw(win)
		
	#	s.cir[s.active_signal].setFill("green")
	#	s.cir[s.active_signal].draw(win)


# to draw the roads of the scene
def draw_scene():

	
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

	return win
	

# close the window after accepting mouse click
def draw_close():

	win.getMouse()		
    	time.sleep(3)
        win.close()


