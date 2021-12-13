def factorial(num):
	m=1
	for i in range(1,num+1):
		m= i*m
	return m

print(factorial(3))#1*2*3