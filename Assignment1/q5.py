#print("Enter the page numbers : \n")
n = int(raw_input("Enter the total number of pages : "))
i = 1
print("Enter the page numbers and press 0 to exit \n")
m = [ ]
while i != 0 :
	i = int(raw_input())
	if i != 0 :
		m.append(i)
	#i = i + 1

print(m) 
print("The page numbers not in the list : ")
for x in range(1, n+1) :
	if x not in m :
		print(x) 


