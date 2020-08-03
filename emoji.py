def median(a,b,c):
    if b < a and a < c or b > a and a > c:
       return a
    if c < a and b < c or c > a and b > c:
        return c
def alternateMedian(a,b,c):
    return a + b + c - min(a,b,c) - max(a,b,c) 

def main():
    x = float(input("Enter your first value: "))
    y = float(input("Enter your second value: "))
    z = float(input("Enter your third value: "))
    print("The median value is: ", median(x, y, z))
    print("Using the alternative method,it is:",alternateMedian(x, y, z))
main()
