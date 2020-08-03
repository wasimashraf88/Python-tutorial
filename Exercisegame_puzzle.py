#Exercise ,Guessing Game
#Make a variable,like winning number and assign any number to it.
#Ask user to guess a number .
#if user guessed correctly then print "YOU WIN!!!"
#if user guessed higher than actual number then print "too heigh"
#Solution............................................

winning_number = 20
guess_number = int(input("Enter your number between 0 to 100:"))
if winning_number == guess_number :
    print("You Win")
else:
    if winning_number > guess_number:
        print("too low")
    else:
     print("too high")

