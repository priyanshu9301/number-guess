import random  # bring in the random number
import time

number = random.randint(1, 250)  # User will pick the number between 1 and 250


def intro():
    print("Enter Your Good Name : ")
    name = input()  # USer will input the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 250")
    time.sleep(.5)
    print("Start thinking And Guess!")


def pick():
    gtaken = 0
    while gtaken < 8:  # Guesses should be less than 6 attempts
        time.sleep(.25)
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string

            # this should be true otherwise it will give a warning
            if guess <= 250 and guess >= 1:

                # adds one guess each time the player is wrong
                gtaken = gtaken + 1
                if gtaken < 8:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break

                    # if the guess is right, then we are going to jump out of the while block

            if guess > 250 or guess < 1:

                # if they aren't in the range

                print("don't be mad! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 250")

        except:  # if a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:

        gtaken = str(gtaken)
        print('Good job, ' + "name" + '! You guessed my number in ' + gtaken + ' guesses!')
        print('Good job, ' + "name" + '! You guessed my number in ' + gtaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))


playagain = "yes"

while playagain == "yes" or playagain == "y" or playagain == "Yes" or playagain == "Y":

    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()