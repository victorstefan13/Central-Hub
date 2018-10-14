from os import system, name 
from calculator import selection
from dateTime import displayDate
from weather import cuurentWeather


def menu():
	print("a) News")
	print("b) Weather")
	print("c) Calculator")
	print("d) Date and Time")
	print("x) to quit")
	print("\n")
	choice = input("Please choose your option: ")

	if choice == "b" or choice == "B":
		cuurentWeather()
	elif choice == "c" or choice == "C":
		selection()
	elif choice == "d" or choice == "D":
		displayDate()
	elif choice == "x" or choice == "X":
		exit()
	else:
		print("\n")
		print("Wrong choice!! Please try again")
		print("\n")
		goBack = raw_input()
		system('clear')




def main():
	system('clear')
	print("\n")
	print("Welcome to your Central Hub, where you can check news,")
	print("weather, or use utilites like calculator, clock etc")
	print("\n")

	menu()

while True: 
	main()

# if __name__ == "__main__":
# 	main()