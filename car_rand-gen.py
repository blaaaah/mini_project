import random

def main():
	i = 0
	fo = open("random.txt","w")
	while(i <= 10000):
		fo.write( str(random.getrandbits(1)) )
		i+=1
		
        fo.close()

main()
