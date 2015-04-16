import math
def d(x1,x2,y1,y2):
	b=x1-x2
	a=y1-y2
	ca=a*a
	cb=b*b
	x=ca+cb
	c=math.sqrt(x)
	print("La distancia entre estos puntos es: ",c)
x1=int(input("Dame un valor para x1: "))
y1=int(input("Dame un valor para y1: "))
x2=int(input("Dame un valor para x2: "))
y2=int(input("Dame un valor para y2: "))
d(x1,x2,y1,y2)
