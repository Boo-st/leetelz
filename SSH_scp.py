from paramiko import SSHClient
from scp import SCPClient
#import RPi.GPIO as GPIO
import time



class woodstocks():

	def setup():
		print("welcome to your stocktake program, the following will update your stock count and save the data to your server.")
		input(">")
		print("First, I need some basic information from you")

		host = input("What is the hostname of the machine which you would like your stocktake loaded? : ")
		filepath = input("What destination would you like your updated stocktake to be placed? : ")
		username = input("Username for Host : ")
		password = input("password for Host : ")

		print('Thank you')

		return(host, filepath, username, password)


	def new_count():
		count = True
		while count:
			exists = input('Do you have a new count to enter? (y or n)')
			if exists == 'y':
				Horses = input('Horses :')
				Elephants = input('Elephants :')
				Dogs = input('Dogs :')
				Seals = input('Seals :')
				




	def update_count(horses, elephants, dogs, seals):
		new_count = True
		while new_count:	
			newlines = input('please enter the updated Horses: ')
			newlines2 = input('please enter the updates Elephants: ')
			newlines3 = input('please enter the updates Dogs: ')
			newlines4 = input('please enter the updates Seals: ')

			test = input('Is this correct? \n Horses : {0} \n Elephants : {1} \n Dogs : {2} \n Seals : {3} \n (y or n?)'.format(newlines, newlines2, newlines3, newlines4))
			if test == 'y':
				new_count = False
			
		return(newlines, newlines2, newlines3, newlines4)


					
