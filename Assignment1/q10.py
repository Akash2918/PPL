print("\nFinding first 10 numbers from geometric series \n")

fterm = int(raw_input("Enter the first term : "))
cratio = int(raw_input("Enter the common ratio : "))

print("\n\n")

for i in range(0, 10) :
	x = cratio ** i
	y = fterm * x
	print(y)
	
print("\n\n")
	
