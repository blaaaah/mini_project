from multiprocessing import Process    
import tlc
import scene    

def main():

	scene.draw_scene()
	tlc.control()	
	scene.draw_close()

main()
