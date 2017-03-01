h = 1000
w = 1000

n_level = h/2 - 50 - 50	
s_level = h/2 + 50 + 50
e_level = w/2 + 50 + 50
w_level = w/2 - 50 - 50

n_density = 0
s_density = 0
w_density = 0
e_density = 0
	

def init_density():
	global n_density 
	global s_density 
	global w_density 
	global e_density 

	n_density = 0
	s_density = 0
	w_density = 0
	e_density = 0
	

def image_processing(position):

	global n_density 
	global s_density 
	global w_density 
	global e_density 
	for p in position:
		if((p[1]>0)and(p[1]<n_level)and(p[0]>(w/2))and(p[0]<((w/2)+100))):
			n_density += 1
	
		if((p[1]>s_level)and(p[1]<h)and(p[0]>((w/2)-100))and(p[0]<(w/2))):
			s_density += 1
	
		if((p[1]>(h/2))and(p[1]<((h/2)+100))and(p[0]>e_level)and(p[0]<w)):
			e_density += 1
	
		if((p[1]>((h/2)-100))and(p[1]<(h/2))and(p[0]>0)and(p[0]<w_level)):
			w_density += 1

	
def print_density():

	global n_density 
	global s_density 
	global w_density 
	global e_density 

	print 'n-density'
	print n_density
	print 's-density'
	print s_density
	print 'w-density'
	print w_density
	print 'e-density'
	print e_density
