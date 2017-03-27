import pishu_db as db
import numpy

def account_neighbours(sid,di):

	nsid = {'n':sid-4, 's':sid+4, 'w':sid-1, 'e':sid+1}
	if 0<sid<5:
		del nsid['n']
	if 12<sid<17:
		del nsid['s']
	if sid%4==1:
		del nsid['w']
	if sid%4==0:
		del nsid['e']
	
	if di not in nsid.keys():
		return 0
		
	nb_densities={}	
	for key in nsid.keys():
		nb_densities[key] = numpy.mean(db.get(nsid[key])[key][3])
	if numpy.mean(nb_densities.values()) == 0:
		return 0
	rd = nb_densities[di] / numpy.mean(nb_densities.values())
	return rd

def calc_timer(sid,di):

	density=db.get(sid)
	ptr = db.geti(sid)
	
	adjn=numpy.mean(density['n'][3][:-1])-numpy.mean(density['n'][ptr['n']][:-1])
	adjw=numpy.mean(density['w'][3][:-1])-numpy.mean(density['w'][ptr['w']][:-1])
	adjs=numpy.mean(density['s'][3][:-1])-numpy.mean(density['s'][ptr['s']][:-1])
	adje=numpy.mean(density['e'][3][:-1])-numpy.mean(density['e'][ptr['e']][:-1])
	

	avg = float (( density['n'][ptr['n']][3] + adjn + density['w'][ptr['w']][3] + adjw + density['s'][ptr['s']][3] + adjs + density['e'][ptr['e']][3] + adje ) / 4)

	if avg == 0:
		return 0.5

	rd = float(density[di][ptr[di]][3] / avg)

	expden = float(( numpy.mean(density['n'][3][:-1])+numpy.mean(density['s'][3][:-1])+numpy.mean(density['e'][3][:-1])+numpy.mean(density['w'][3][:-1]) ) / 4 )

	cr = 2.333
	l = 1
	#rdm = account_neighbours(sid, di)
	#if rdm == 0:
	rdm = rd
	timer_val = (( 0.6666*rd + 0.3333*rdm) * expden) / (l * cr)
	if sid==1:
		print "SID: "+str(sid)+"	Timer:"+str(timer_val)+"	Dir:"+di
	return timer_val
