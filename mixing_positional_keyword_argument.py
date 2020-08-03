def hi(name1,name2): #example of two-parameter function:
    print("Hi,", name2)
    print("Hi,", name1)

hi("Wasim","Ashraf")
#example of three-parameter funcrion:
def address(street, city, postalCode):
    print("Your address is:",street, "St.,", city, postalCode)
s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")
address(s,c,pC)