import random

#choose 2 integer numbers with a difference of 10
number1 = int(input("Enter the first number for the game:"))
number2 = int(input("Enter the second number for the game:"))

constraint = abs(number1 - number2)


if constraint == 10:
   print("The numbers are suitable for the game, let's start the game")
else:
   print("Please choose two numbers with a difference of 10. Try again.")

#A random number will be chosen between these two numbers
random_number = random.randint(number1, number2)

#Try to guess the randomly selected number

current_score = 10

while True:
        
        guess = int(input("Guess the number: "))

        
        if guess == random_number:
            print("Congratulations! You guessed the correct number. Your point: ", current_score )
            break
        else:
            print("Wrong guess. Try again.")
            current_score -= 1
        if current_score == 0:
            print("Sorry, you've run out of attempts. The correct number was:", random_number)
            break

"""
 when you start the game you have 10 points. 
 1 point is deducted for each incorrect attempt.
 As soon as you find the random number, 
 the decrease ends and you learn the game score.
"""