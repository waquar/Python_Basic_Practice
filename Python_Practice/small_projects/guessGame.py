import random

num= random.randrange(1, 100)
print(num)
attempt = 0
data = []

while True:
    guess = int(input("Please enter your guess: "))
    data.append(guess)
    attempt += 1

    if guess < 100:
        if guess == num:
            print("nice guess after thismuch attempt : - ", attempt)
            print("u used these data", data)
            exit()
        elif guess - num < 5 and num -guess <5:
            print("hottest")
        elif guess - num < 15 and num-guess <5:
            print("hotter")
        elif guess - num < 20 and num-guess <5:
            print("hot")
        else:
            print("Your guess is too high")
    else:
        print("numbers are less then 100! make sure to give less then 100")


