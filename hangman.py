import random

name = input("Enter  your name:")
print("Hello " + name + " let's play hangman")

film_list = ["awakings","fightclub","12angryman","interstaller","greenmile","neverletmego","titanic","driver","godfather","fargo","parazit","braveheart","joker","inception","shutterısland","suffragette"]

secret_word = random.choice(film_list)
length = len(secret_word)
lives = int (length + 5)
print(f"You have {lives}.Be carefullll :)")
guess_string =""


while lives > 0:

    count = 0

    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("*")
            count +=1

    if count == 0 :
        print("You won.Congratulations!!!!")
        break
    
    guess = input("Guess:")
    guess_string+=guess

    if guess not in secret_word:
        lives-=1
        print("Wrong Guess")
        print(f"You have {lives} left")

        if lives == 0:
            print("You died:/")

   

