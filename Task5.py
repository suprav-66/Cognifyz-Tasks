#Pallindrome Checker
# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]

# Taking input from user
s = input("Enter a string:")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
 
#Checking for a number
num = input("Enter a number")
if num == num[::-1]:
	print("Yes its a palindrome")
else:
	print("No, its not a palindrome")
