from paramiko import SSHClient
from scp import SCPClient
#import RPi.GPIO as GPIO
import time



class woodstocks():

	def setup():
		print("welcome to your stocktake program, the following will update your stock count and save the data to your server.")
		input(">")
		print("First, I need some basic information from you")

		localpath = input("Please enter a local file path to store your stocktake : ")
		host = input("What is the hostname of the machine which you would like your stocktake loaded? : ")
		filepath = input("What is the filepath on your remote location : ")
		username = input("Username for Host : ")
		password = input("password for Host : ")

		print('Thank you')

		return(host, filepath, username, password, localpath)


	def new_count(file='/Users/mitchelking/Python/test.txt'):
		while True:
			exists = input('Do you have a new count to enter? (y or n)')
			if exists == 'y':
				with open(file, 'r') as item:
					try:
						text = [line.strip() for line in item]
						print(text[0])
						Horses = input('Horses :')
						print(text[1])
						Elephants = input('Elephants :')
						print(text[2])
						Dogs = input('Dogs :')
						print(text[3])
						Seals = input('Seals :')
					except IndexError:
						woodstocks.update_count()
						return False
			else:
				return False	
				


	def update_count():
		new_count = True
		while new_count:	
			newlines = input('please enter the current Horses: ')
			newlines2 = input('please enter the current Elephants: ')
			newlines3 = input('please enter the current Dogs: ')
			newlines4 = input('please enter the current Seals: ')

			test = input('Is this correct? \n Horses : {0} \n Elephants : {1} \n Dogs : {2} \n Seals : {3} \n (y or n?)'.format(newlines, newlines2, newlines3, newlines4))
			if test == 'y':
				new_count = False

		with open('/Users/mitchelking/Python/test.txt', 'w') as new_f:
			new_f.write('Horses ' + newlines + '\n' + 'Elephants ' + newlines2 + '\n' + 'Dogs ' + newlines3 + '\n' + 'Seals ' + newlines4)
			
		return(newlines, newlines2, newlines3, newlines4)


					
	def transfer(host, filepath, username, password):
		#with open('/Users/mitchelking/Python/test.txt', 'w') as new_f:
		#	new_f.write(lines[0] + '\n' + lines[1], + '\n' + lines[2] + '\n' + lines[3])

		ssh = SSHClient()
		ssh.load_system_host_keys()
		ssh.connect(host, port=22, username=username, password=password)


		scp = SCPClient(ssh.get_transport())
		scp.put('/Users/mitchelking/Python/test.txt', remote_path=filepath)
		scp.close()



#temp_host, temp_filepath, temp_username, temp_password = woodstocks.setup()
#woodstocks.transfer(temp_host, temp_filepath, temp_username, temp_password)

woodstocks.new_count()