import time
from os import system, name 

def displayDate():

	print("\n")
	system('clear')
	
	print (time.strftime("%d/%m/%Y"))

	print (time.strftime("%H:%M:%S"))

	print("\n")

	print("Press any key to return to the main menu; ")

	print("\n")
	back = input()
	system('clear')

