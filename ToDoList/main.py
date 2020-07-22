file = "works.txt"
run = True
print("Welcome To The ToDoList Program")
print("Press Q to exit")
numberoftodos = 0
start = input("Start List Yes or No")
if start == "Q":
	pres('Ok to confirm')
	exit()
while run:
	if start =="Yes" or start =="yes":
		task = str(input("Enter what to do later"))
		numberoftodos += 1
		with open(file, 'a') as tasks:
			tasks.write(f'\n {task}')
		end = input("Do you want to continue[Y/N]")
		if end =="N" or end.lower() =="n":
			run = False
		elif start =="Q":
			run = False
		else:
			print("Todo is still running")

	elif start =="No" or start =="no":
		run = False
	elif start =="Q":
		run = False
print("Did you use our program")
use = input('Y/N \n')
if use =="Y" or use.lower() =="y":
	ask = input('Want to see what is left[Yes/No]')
	if ask =="Yes" or ask.lower() =="yes":
		print("Check the list.txt file")
		print("Thanks for using the program!")
	elif ask =="No" or ask.lower() =="no":
		print("Thanks for using the program")
elif use =="N" or use.lower() =="n":
	print("You can comeback and try it whenever you like")
