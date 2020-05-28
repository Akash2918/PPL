
print("\nFinding first 10 Harmonic Divisor Numbers :\n")

"""def floating(n) :
	x = 1
	s = 0
	for i in n :
		x = x * i
	for i in n:
		s = s + x/i
	print("The value of s is : ", s)	
	return s/x """
	
def calculate(n) :			# function that calculates harmonic sum and returns its division with total number of divisors
	s = 0
	x = 0
	for i in n :
		x = x + 1
		s = s + 1.0/ i
	#s = floating(n)
	#print(s)
	s = x/s
	#print(s)
	return s
		
def harmonic(x) :			# function which calculates divisors of numbers and stores into list
	m = []
	i = 1
	while i <=x :
		if x % i == 0 :
			m.append(i)
		i = i + 1	
	#print(m)
	y = calculate(m)
	#print('The value of y is :', y)			# the type of y is float
	#print(y)
	y = y * 10				# converting y into int
	if y % 10 == 0 :
		return True
	else :
		return False 
		
x = 1
n = 1

while n <= 10 :
	if harmonic(x) :
		print(x)
		n = n + 1
		x = x + 1
	else :
		x = x + 1	

