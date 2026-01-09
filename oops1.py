class employee:
    # Constructor
    def __init__(self):
        self.name = "Sumedh"
        self.id = "2024AB05077"
        self.salary = "50000"
        self.designation = "ML engineer"

    def travel(self,destination):
        print("Employee is now travelling to", destination)

# Creating an object/instance
Sam = employee()

# print(Sam.salary)

# calling a method
Sam.travel("Pune")

print(type(Sam))