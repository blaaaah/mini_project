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
	n_density_array=[0,0,0]
	s_density_array=[0,0,0]
	e_density_array=[0,0,0]
	w_density_array=[0,0,0]

	for p in position:
		if(p[1]>0)and(p[1]<n_level):
			if (p[0]>(w/2))and(p[0]<((w/2)+33)):
				n_density_array[0] += 1
			elif (p[0]>(w/2)+33)and(p[0]<((w/2)+66)):
				n_density_array[1] += 1
			elif (p[0]>(w/2)+66)and(p[0]<((w/2)+100)):
				n_density_array[2] += 1
			

	
		if(p[1]>s_level)and(p[1]<h):
			if (p[0]<(w/2))and(p[0]>((w/2)-33)):
				s_density_array[0] += 1
			elif (p[0]<(w/2)-33)and(p[0]>((w/2)-66)):
				s_density_array[1] += 1
			elif (p[0]<(w/2)-66)and(p[0]>((w/2)-100)):
				s_density_array[2] += 1
		

	
		if(p[0]>e_level)and(p[0]<w):
			if (p[1]>(h/2))and(p[1]<((h/2)+33)):
				e_density_array[0] += 1
			elif (p[1]>(h/2)+33)and(p[1]<((h/2)+66)):
				e_density_array[1] += 1
			elif (p[1]>(h/2)+66)and(p[1]<((h/2)+100)):
				e_density_array[2] += 1
			
		if (p[0]>0)and(p[0]<w_level):
			if (p[1]<(h/2))and(p[1]>((h/2)-33)):
				w_density_array[0] += 1
			elif (p[1]<(h/2)-33)and(p[1]>((h/2)-66)):
				w_density_array[1] += 1
			elif (p[1]<(h/2)-66)and(p[1]>((h/2)-100)):
				w_density_array[2] += 1
	
	n_density=max(n_density_array)*3
	s_density=max(s_density_array)*3
	e_density=max(e_density_array)*3
	w_density=max(w_density_array)*3

	
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
