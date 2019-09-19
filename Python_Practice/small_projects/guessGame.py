import random

num= random.randrange(1, 100)
print(num)
attempt = 0
data = []

while True:
    guess = int(input("Please enter your guess: "))
    if guess < num:
        a = num - guess
    else:
        a = guess - num

    data.append(guess)
    attempt += 1

    if guess < 100:
        if guess == num:
            print("nice guess after thismuch attempt : - ", attempt)
            print("your last two data", data[-2:])
            exit()
        elif a < 5:
            print("hottest")
        elif a < 8 :
            print("hotter")
        elif a < 11 :
            print("hot")
        else:
            print("Your guess is too high")
    else:
        print("numbers are less then 100! make sure to give less then 100")


