# Initalize the variables
secret_word = "giraffe"

# This is the user's guess.
guess = ""

# Variable for number of user guesses
guess_count = 0

# Variable for limit of user guesses
guess_limit = 3

# Variable for if the user used all guesses
out_of_guesses = False

# While the user's guess isn't equal to
# the secret_word, and their guesses haven't
# exceeded 3, ask them to enter a guess.
#
# If a guess is wrong, you add 1 guess. When
# guesses exceed 3, loop ends.
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# If you are out of guesses, print
# "Out of Guesses! YOU LOSE!".
# Otherwise, print "You win!".
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")