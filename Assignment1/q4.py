
import random

print("\nGuess The Number\n")
print("The range of numbers is 1 to 99\n")
x = random.randint(1, 100)

#print "The value of x is : ", x
sm = 0
flag = 0
sq = 0
y = 1
m = x
while x >0 :
	rem = x%10
	#print("rem = : ", rem)
	#n += 1
	x = x/10
	sm = sm + rem
	#print("sum = ", sm)
	sq = sq + pow(rem, 2)
	y = y * rem
	#print("mul is :" , y)
print("sum of digits : " + str(sm))
print("\n\n")
guess = int(raw_input("Enter your number : "))
print(guess)
for i in range(0, 4) :
	#print("Hello world\n")
	if m == guess :
		print("You have guessed correctly\n\n\n")
		flag = 1
		break
	elif i == 1 :
		print("Sorry wrong input, please try again\n\n")
		print("Multiplication of digits : " + str(y)) 
		guess = int(raw_input("Enter your number : "))
	elif i == 2 :
		print("Sorry wrong input, please try again\n\n")
		print("Sum of squares of digits : " + str(sq))
		guess = int(raw_input("Enter your number : "))

if flag == 0 :		
	print("The number is : ", m)	
	print("\n\n")
#print("No of digits : ", n)


