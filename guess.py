secret_word= "python"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False
while guess != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input("enter a guess  ")
        guess_count += 1
    else:
        out_of_guess = True
    
    
if out_of_guess:
        print("you are out of guesses, You Lose")
else:
        print("you guessed right, You win")
    