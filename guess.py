from logo import logo
import re
import random

welcome_banner = "Welcome to the number guessing game!"
description = "I'm thinking of a number between 1 and 100."

# Attempts
attempts = 0

# Number to guess
target = random.randint(1, 100)

# Guesses list initialized
guesses = []

# Start the game
print(logo)
print(welcome_banner)
print(description)


def play():
    global attempts
    # Choose difficulty
    while True:
        difficulty = input("Choose a difficulty.\nType 'easy' or 'hard':\n")
        if difficulty == 'hard':
            attempts += 5
            break
        elif difficulty == 'easy':
            attempts += 10
            break
        else:
            print("Please type 'easy' or 'hard'.\n")

    # Regex pattern for matching integers
    number_pattern = re.compile(r'^-?\d+$')

    # Player's guess
    while attempts > 0:
        # Run the loop until the guess is valid format
        while True:
            player_input = input("Make a guess:\n")
            if number_pattern.match(player_input):
                player_guess = int(player_input)

                # If guess is not in this range, ask the player to guess again
                if 1 <= player_guess <= 100:
                    # If number was already guessed
                    if player_guess in guesses:
                        print(f"You already guessed {player_guess}.\nChoose another number")
                    else:
                        break  # Valid number, exit the inner loop
            else:
                print("Please enter a valid number.")

        if player_guess < target:
            guesses.append(player_guess)
            print(f"Guesses: {''.join(str(sorted(guesses)))}")
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts left to guess the number.")
        elif player_guess > target:
            guesses.append(player_guess)
            print(f"Guesses: {''.join(str(sorted(guesses)))}")
            print("Too high.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} attempts left to guess the number.")
        else:
            guesses.append(player_guess)
            print(f"Guesses: {str(sorted(guesses))}")
            attempts -= 1
            print(f"That's correct!\nThe number is {player_guess}.\nYou win.")
            break  # Correct guess, end game

    if attempts == 0:
        print(f"No more attempts.\nYou lose!\nThe correct number is {target}")


def main():
    while True:
        # Ask the user if they want to play the game
        play_response = input("Do you want to play number guesser? Type 'yes' to play, or anything else to quit: ").lower()

        # If the user responds with 'yes', start the game
        if play_response == 'yes':
            play()
        else:
            # If the user responds anything else quit playing the game
            print("Thank you for playing! Goodbye.")
            break  # Exit the loop and end the program


if __name__ == "__main__":
    main()

