def superpower(a,b):
	t=a
	for i in range(1,b):
		t=t*a
	return t
a=int(input("Dame el valor para a: "))
b=int(input("Dame el valor para b: "))
superpower(a,b)
g=superpower(a,b)
print("El resultado es: ",g)
