import random
chances = 5
print("Welcome To Guess The Number Game")
no = random.randint(0,256)

run = True
while run:
        guess = int(input("Enter your guess"))
        if guess == no:
                print("You Got It")
                run = False
                break
        elif guess > no:
                print("You guessed  higher!")
                chances -= 1
        elif guess < no:
                print("You guessed lower!")
                chances -= 1

        if chances == 0:
              print("You Lose")
              run = False
         
