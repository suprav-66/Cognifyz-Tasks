#Email Validator
from email_validator import validate_email, EmailNotValidError
#taking function check for checking
def check(email):
	try:
	# validate and get info
		v = validate_email(email) 
		# replacing with normalized form
		email = v["email"] 
		print("True")
	except EmailNotValidError as e:
		# if email is not valid, exception message will be printed
		print(str(e))

s=input("Enter a mail (valid or invalid) to check:")
check(s)
