import random

def hangman_game():
    fruit_names = ["Apple", "Pear", "Banana", "Grape", "Strawberry", "Watermelon", "Cherry", "Tangerine", "Orange", "Pineapple", 
                   "Mango", "Pomegranate", "Cherry", "Raspberry", "Mulberry", "Lemon", "Lime", "Guava", "Apricot", "Grapefruit", 
                   "Avocado", "Pomegranate", "Plum", "Cantaloupe", "Peach", "Date", "Fig", "Walnut", "Grape", "Mulberry", "Pomegranate"]

    random_fruit = random.choice(fruit_names)

    hidden_word = [letter if index in [1, 3] else "_" for index, letter in enumerate(random_fruit)]

    #print("Food:", random_fruit)
    print("Result:", "".join(hidden_word))

    max_wrong_attempts = 6
    wrong_attempts = 0
    guessed_positions = set()
    guessed_letters = set()

    while "_" in hidden_word and wrong_attempts < max_wrong_attempts:
        try:
            guess_letter = input("Enter the letter you guessed: ").strip().upper()

            if len(guess_letter) != 1 or not guess_letter.isalpha():
                print("Please enter a valid single letter.")
                continue

            if guess_letter in guessed_letters:
                print("You already guessed the letter {}. Please choose a different letter.".format(guess_letter))
                continue

            guessed_letters.add(guess_letter)

            correct_guess = False
            for index, letter in enumerate(random_fruit):
                if letter.upper() == guess_letter:
                    hidden_word[index] = guess_letter
                    correct_guess = True

            if correct_guess:
                print("Right guess! New situation:", " ".join(hidden_word))
            else:
                wrong_attempts += 1
                print("Wrong guess! {} attempt(s) left.".format(max_wrong_attempts - wrong_attempts))
        
        except ValueError:
            print("Please enter a valid letter.")

    if "_" in hidden_word:
        print("Game over! You couldn't complete the word. The correct word was:", random_fruit)
    else:
        print("Congratulations! You have completed the word. Correct word:", random_fruit)


def play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no.'")

hangman_game()

while play_again():
    hangman_game()

print("Thank you for playing. Goodbye!")
