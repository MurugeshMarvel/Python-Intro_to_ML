length = int(input("Enter the range for the fibonacci Series"))

a = 0
b = 1
count = 0

print "Fibonacci Series"
if length == 1:
	print a
else:
	while count < length:
		print (a, end=',')
		c = a+b
		a = b
		b = c
		count += 1

		
