def f(n):
	a1=0
	b1=1
	if(n==0):
		print("fibonacci de tu numero es: 0")
	if(n==1):
		print("fibonacci de tu numero es: 1")
	else:
		for i in range(2,(n+1)):
			c=a1+b1
			a1=b1
			b1=c
		return c
	
n=int(input("Dame el numero que quieres el fobonacci: "))
f(n)
t=f(n)
print("El fibonacci de tu numero es: ",t)
		
	
