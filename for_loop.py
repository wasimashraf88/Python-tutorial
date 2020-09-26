# Assignemnt 
#Create a list any number or string or float in string.Print those number if numbers have greater than 6

#Solution

list1 = ["string","float","Asim","Sheraz",1,5,6,8,22,200,223,"Ghufran"] #create list
for items in list1:                                      #using for loop
    if str(items).isnumeric() and items >6:         #if condition used and typecasting
        print(items)