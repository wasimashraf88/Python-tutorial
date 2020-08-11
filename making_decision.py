class Employee:
    no_of_leaves = 9
    def __init__(self, name , salary ,id):
        self.name = name 
        self.salary = salary
        self.id = id



    def printdetails(self):
        return f"Name is:{self.name}.Salary is {self.salary} and Id is {self.id}"
asim = Employee("Asim",10000,50)
sheraz = Employee("Sheraz",5000, 51)

# # asim.name = "Asim"
# # asim.salary = 10000
# # asim.id = 50

# # sheraz.name = "Sheraz"
# # sheraz.salary = 50000
# # sheraz.id = 51 
print(asim.printdetails())
print(sheraz.printdetails())
