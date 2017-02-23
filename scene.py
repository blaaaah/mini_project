from graphics import *
import tlc
win = GraphWin('Simulator', 1000, 1000)
w=win.getWidth()
h=win.getHeight()

def ret_h():                              
	return h

def ret_w():
	return w
	
def ret_win():
	return win

def def_sig():
	sig_list = []
	for i in range(16):
		s = tlc.sLight(i+1)
		sig_list.append(s)
	return sig_list

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
	

def draw_close():

	win.getMouse()		
    	time.sleep(3)
        win.close()


