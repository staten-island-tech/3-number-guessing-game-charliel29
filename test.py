def guessing():
    import random
    actual = random.randint(1,10)
    guess = int(input("What is your number?"))
    while guess !=actual:
        if guess > 10 or guess < 1:
            print ("Invalid")
            break
        if guess > actual:
            print ("Your guess is too high")
        else:
            print("Your guess is too low")
        print ("Guess again")
        guess = int(input("What is your number?"))
    if guess == actual:
        print ("correct")
guessing()