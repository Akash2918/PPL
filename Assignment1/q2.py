from random import randint

print("Wel-come\n")

x = raw_input("Enter p to play or q to quite : ")
#x = "p"
while x is not None :
	if (x == "p") or (x == "P") :
		print(randint(1, 6))
		x = raw_input("Enter p to play or q to quite : ")
	else :
		print("Thank you !!!")
		break
		
