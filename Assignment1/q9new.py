
print("Finding First 10 harmonic numbers\n")



def calculate(m) :
	x = 0
	rem = 0
	s = 1 
	for i in m :
		x = x + 1
		s = s * i 
	print("The value of s is : ", s)
	for i in m :
		rem = rem + (s * 1.0 / i )
	
	rem = rem / s	
	y = (x * 1.0) / rem
	print("Inside calculate function : ", y)
	return y
		
def harmonic(x) :
	i = 1
	m = []
	while i <= x  :
		if x % i == 0 :
			m.append(i)	
		i = i + 1

	print(m)
	y = calculate(m)
	print("The value of y is " ,y)
	y = y * 10
	if y % 10 == 0 :
		return True
	else :
		return False	
	
x = 267
n = 1
while n <= 10 and x < 272 :
	if harmonic(x) :
		print(x)
		print("Yes I am working")
		n = n + 1
		x = x + 1
	else :
		x = x + 1	


