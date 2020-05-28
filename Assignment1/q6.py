print("\nAmicable Numbers: \n")

def calculate(x) :
	s = 0
	for i in range(1, x) :
		#y = x % i
		if x%i == 0 :
			s = s + i
	return x, s
		
def isamicable(x) :
	a, b = calculate(x)
	c, d = calculate(b)
	if a == d  and a != b :
		print(a, b)
		return True
	else :
		return False				
x = 1
n = 1
#m = [ ]
while n <=10 : 
	if isamicable(x) :
		n = n + 1
		#m.append(x)
		x = x + 1
		isamicable(x)
	else :
		x = x + 1
		isamicable(x)
		
		
