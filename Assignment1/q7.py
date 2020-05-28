
def power(a) :
	n = 0
	while a >0 :
		a = a/10
		n = n + 1
	return n
	
print("\nFinding Armstrong Numbers\n") 
print("Enter range  of numbers\n")

start = int(raw_input("Start : "))
end = int(raw_input("End : "))

x = start

print("Following are the Armstrong Numbers : ")

while x <= end :
	s = 0
	p = power(x) 	#calculation number of digits in the number
	y = x
	while y >0 :
		 rem = y %10
		 s = s + pow(rem , p)
		 y = y/10
	
	if x == s :
		print(x)	 
	x = x + 1
	
	
