import scene
from graphics import *
import gtk # python-gtk2
import pishu_db as db

h = scene.ret_h()
w = scene.ret_w()

def get_pixel_colour(i_x, i_y):
	i_y += 78
	i_x += 100
	o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
	return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])

def img_process(s):
	c = [[s.x-(w/18),s.y-(h/36)],[s.x-(w/36),s.y+(h/6)],[s.x+(w/6),s.y+(h/36)],[s.x+(w/36),s.y-(h/18)]]
	
	density = [0,0,0,0]
	
	for i in range(4):
		for j in range(h/9):
			if i%2==0:
				pix = get_pixel_colour(int(c[i][0]-j), int(c[i][1]))
			else:
				pix = get_pixel_colour(int(c[i][0]), int(c[i][1]-j))
			density[i]+=pix[0]
		density[i]/=(255)
		q = density[i]/10
		r = density[i]%10
		if r!=0:
			r=1
		density[i]=q+r
	
	#print "id="+str(s.d)+"	n="+str(density[3])+"	e="+str(density[2])+"	w="+str(density[0])+"	s="+str(density[1])
	db.update(s.d,density[3],density[2],density[0],density[1])
