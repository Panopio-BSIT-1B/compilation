import random

print("+++++++++++++")
print("Fruit Guessing Game")
print("+++++++++++++")

fruits = ["apple", "banana", "mango", "orange"]
secret_fruit = random.choice(fruits)
tries = 0

while True:
    guess = input("Guess a fruit (apple, banana, mango, orange) --> ").lower()
    tries += 1

    if guess == secret_fruit:
        print(f"{guess.capitalize()} is the right fruit! YOU GUESSED RIGHT!!!")
        break
    elif guess in fruits:
        print(f"{guess.capitalize()} isn't the right fruit. Try again!")
    else:
        print("That's not one of the choices! Please pick from apple, banana, mango, or orange.")

print(f"You tried {tries} times.")
