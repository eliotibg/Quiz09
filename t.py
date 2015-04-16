def t(n):
	for i in range(0,n):
		print("t"*(i+1))
		c=i
	while(c>0):
		print("t"*(c))
		c=c-1
n=int(input("Dame el un numero para hacer el triangulo correspondiente: "))
t(n)
