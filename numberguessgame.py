import random
number = random.randint(1, 100)
attempts = 0
print("I'm thinking of a number between 1 and 100.")
while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < number:
        print("low")
    elif guess > number:
        print("high")
    elif (guess<=0 or guess>=101):
        print("invaild range try number between 1 and 100 ")
    else:
        print("Congratulations...you guessed the number ",number," in", attempts," attempts.")
        break

