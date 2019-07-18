cont = 0
contN = int(input("How many times do you want to type? "))
big = 0
smaller = 0
while cont < contN:
	num = int(input("Enter the number: "))
	if cont == 1:
		big = num
		smaller = num
	if num > big:
		big = num
	if num < smaller:
		smaller = num
print("The largest number is ", big)
print("The smallest number is ", smaller)