import random

def main():
	fi = open("rand_car.txt","w")
	i = 0
	while i<=10000:
		fi.write(str(random.getrandbits(1)))
		i+=1
	fi.close()

main()
