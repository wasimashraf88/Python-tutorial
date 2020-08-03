def hi(name): #An example of one argument
    print("Hi",name)
hi("Greeg")
#An example of two argument
def hiAll(name1,name2):
    print("Hi",name1)
    print("Hi",name2)
hiAll("Sebastian","Konrad")
#An example of three argument
def address(street,city,postalCode):
    print("Your address is:",street,"St.,",city,postalCode)
s = input("Street: ")
pC = input("Postal Code : ")
c = input("City: ")

address(s,c,pC)
