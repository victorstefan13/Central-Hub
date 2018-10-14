from os import system, name 

def selection():
	system('clear')
	print("Please choose from the following:")
	print("a) add")
	print("b) subtract")
	print("c) multiplication")
	print("d) division")
	print("x) to quit")
	print("\n")

	choice = input()
	print("\n")

	if choice == "a":
		add()
	elif choice == "b":
		sub()
	elif choice == "c":
		mul()
	elif choice == "d":
		div()
	elif choice == "x":
		return
	else:
		print("\n")
		print("Wrong Choice!!! Please select again")
		print("\n")

def add():
	system('clear')
	a = int(input("Please enter your first number: "))
	b = int(input("please enter your second number: "))
	ans = a + b
	print("\n") 
	print("Answers: " + str(ans))
	print("\n")
	clear = input()
	system('clear')

def sub():
	system('clear')
	a = int(input("Please input your first number: "))
	b = int(input("Please input your second number: "))
	ans = a - b
	print("\n")
	print("Answer: " + str(ans))
	print("\n")
	clear = input()
	system('clear')

def mul():
	system('clear')
	a = int(input("Please input your first number: "))
	b = int(input("Please input your second number: "))
	ans = a * b
	print("\n")
	print("Answer: " + str(ans))
	print("\n")
	clear = input()
	system('clear')

def div():
	system('clear')
	a = int(input("Please input your first number: "))
	b = int(input("Please input your second number: "))
	ans = a / b
	print("\n")
	print("Answer: " + str(ans))
	print("\n")
	clear = input()
	system('clear')