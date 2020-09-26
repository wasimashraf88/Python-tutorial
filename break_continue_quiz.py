#take input from user if number is less than equal to 100 code work if input is greater than 100 print congratulation you win

while True:
    x = int(input("Enter your number:\n"))
    if x > 100:
        print("Congratulation you enterd greater than 100:\n")
        break
    else:
        print("Try again\n")
        continue
        
