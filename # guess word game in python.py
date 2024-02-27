# guess word game in python
import random
# ask player for his name
name = input("Enter your name: ")
# welcome message
print(f"Welcome Mr.{name} to Word guess Game")
# words list to choose randomly from it
word = ["banana", "apple", "cherry", "tomato", "car",  "Punisher"]
#prog choose random word
pg = random.choice(word)
# number of hands to play == letters in word
hand = len(pg)
# variable to insert letters guessed
guessed = ""
# create loop to player enter characters
while hand > 0:
    # variable will be 0 every guess
    Under_score = 0
    # ask player to guess character to complete the right word
    guess = input("guess character: ")
    # add guessed letter to guessed variables
    guessed += guess
    # loop to check every letter i n program random word
    for char in pg:
        # check if the character in random word is guessed from user
        if char in guessed:
            #if yes print it in screen
            print(char, end=" ")
        else:# if no print _ in screen
            print("_", end=" ")
            # if guessed word has _ add 1
            Under_score += 1
    # if guessed word don't has(_) player win
    if Under_score == 0:
        print ("\nYou win")
        break
    # in case letter entered by user not in random word decrement hand to play
    if guess not in pg :
        hand -= 1
        print("wrong")
    if hand == 0:
        print("game Over \nthe ward is", pg)
