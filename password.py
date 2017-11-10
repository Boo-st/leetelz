import os

pass2 = input("Please enter your password: ")
with open("/Users/mitchelking/Python/password.txt", 'r') as infile:
	pass1 = infile.read()
def check(input1):
	if input1 == pass1:
		return True
	else:
		print ("Access denied")
		return False
		infile.close()
		
if check(pass2):
	print ("password accepted")
	infile.close()
	with open("/Users/mitchelking/Python/password.txt", 'w') as infile2:
		_input = input("Would you like to change your password?: (y or n) ")
		if _input == 'y':		
			pass3 =  input("Please enter your new password: ")		
			infile2.write(pass3)
			infile2.close() 




