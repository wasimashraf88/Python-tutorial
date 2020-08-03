#num1 = input("Enter your 1st number:")
#num2 = input("Enter your 2nd number:")
#num3 = input("Enter your 3rd number")

num1,num2,num3 = input("Enter three numbers comma separated: ").split(",")
print(f"Average of the number is : {(int(num1)+int(num2)+int(num3))/3}")
