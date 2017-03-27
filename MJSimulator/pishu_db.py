import mysql.connector as mc 


db = mc.connect(host = "localhost",database = "node",user = "root",password = "toughpassword123")
cursor = db.cursor()

def init(sid,di):
	di = di + 'i'
	k = 3
	hai = ['ni','wi','si','ei']
	for i in range(0,4):
		if di == hai[i]:
			break

	print "**** INIT "+str(sid)+"  *****"
	i = i - 1
	while k!=0:
		i=(i+1)%4
		pi = hai[i]
		sql = "UPDATE selector SET "+pi+" = "+str(k)+" where ID = "+str(sid) 
		cursor.execute(sql)
		db.commit()
		k = k - 1;


def update(id1,n,e,w,s):
	sql = "SELECT * FROM selector WHERE ID="+str(id1)
	cursor.execute(sql)
	results = cursor.fetchone()
	sql = "SELECT * FROM node WHERE ID="+str(id1)
	cursor.execute(sql)
	resulter = cursor.fetchone()
	n = resulter[1+results[1]]+','+str(n)
	s = resulter[5+results[3]]+','+str(s)
	e = resulter[9+results[4]]+','+str(e)
	w = resulter[13+results[2]]+','+str(w)
	n=','.join(n.split(',')[1:5])
	s=','.join(s.split(',')[1:5])
	e=','.join(e.split(',')[1:5])
	w=','.join(w.split(',')[1:5])
	
	sql = "UPDATE node SET na"+str(results[1])+"='"+str(n)+"', wa"+str(results[2])+"='"+str(w)+"', sa"+str(results[3])+"='"+str(s)+"', ea"+str(results[4])+"='"+str(e)+"' WHERE ID = "+str(results[0])
	cursor.execute(sql)
	db.commit()

	pi=["ni","si","wi","ei"]
	for i in range(1,5):
		sql = "UPDATE selector SET "+pi[i-1]+" = "+str((results[i]+1)%4)+" where ID = "+str(id1)
		cursor.execute(sql)
		db.commit()
	


def delete():
		sql = "UPDATE selector SET ni = 0, si = 0, ei = 0, wi =0"
		cursor.execute(sql)
		db.commit()
		sql = "UPDATE node SET na0 = '0,0,0,0', na1 = '0,0,0,0', na2 = '0,0,0,0', na3 = '0,0,0,0', sa0 = '0,0,0,0', sa1 = '0,0,0,0', sa2 = '0,0,0,0', sa3 = '0,0,0,0', ea0 = '0,0,0,0', ea1 = '0,0,0,0', ea2 = '0,0,0,0', ea3 = '0,0,0,0', wa0 = '0,0,0,0', wa1 = '0,0,0,0', wa2 = '0,0,0,0', wa3 = '0,0,0,0'"
		cursor.execute(sql)
		db.commit()

def insert(id1,a,b,c,d,e,f,g,h,i,j,k,l):
	sqlw = "INSERT INTO node(id, n1, n2, n3, e1, e2, e3, w1, w2, w3, s1, s2, s3) VALUES ('%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')" %  (id1,a,b,c,d,e,f,g,h,i,j,k,l)
	cursor.execute(sqlw)
	db.commit()

def get(id1):
	sql = "SELECT * FROM node WHERE ID = '%d' " % (id1)
	cursor.execute(sql)
	results = cursor.fetchone()
	results=list(results)
	for i in range(1,17):
		results[i]=list(map(int, results[i].split(",")))
	return {'id':results[0],'n':results[1:5],'e':results[9:13],'w':results[13:17],'s':results[5:9]}

def geti(id1):
	sql = "SELECT * FROM selector WHERE ID = '%d' " % (id1)
	cursor.execute(sql)
	results = cursor.fetchone()
	return {'id':(results[0]-1)%4,'n':(results[1]-1)%4,'s':(results[2]-1)%4,'e':(results[3]-1)%4,'w':(results[4]-1)%4}
	

def main():
	update(3,11,22,33,44)
	print get(3)

#main()
