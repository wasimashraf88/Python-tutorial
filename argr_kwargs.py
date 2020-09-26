# # Arbitrary Arguments or *args
# def my_func(*kids):
#     print("The youngest child is:",kids[3])

# my_func("Emil", "Tobias","Sara","Nib")

# # Keyword Arguments   
# #You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.

# def my_func1(child1,child2,child3):
#     print("The yougest child is:" + child2)
# my_func1(child1="Harry",child2="Merry",child3="Carry")

# # Arbitrary Keyword Arguments, **kwargs
# # If you do not know how many keyword arguments that will be passed into your function, add two asterisk: **

# def my_func2(**kids):
#     print("His last name is " + kids["lname"])
# my_func2(fname = "Asim", lname = "Irshad")

def concatenate(**kwargs):
    new = " "
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        new += arg
    return new

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
