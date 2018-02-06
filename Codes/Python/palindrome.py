string = raw_input("Enter the String to check Palindrome")
string_reverse = string[::-1]
if string == string_reverse:
	print "The string is palindrome"
else:
	print "The string is not  Palindrome"

