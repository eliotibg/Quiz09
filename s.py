def superpower(a,b):
	t=a
	for i in range(1,b):
		t=t*a
	print("El resultado es: ",t)
a=int(input("Dame el valor para a: "))
b=int(input("Dame el valor para b: "))
superpower(a,b)
