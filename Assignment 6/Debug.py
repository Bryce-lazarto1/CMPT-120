class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
    class Cake:
        def __init__(self, flavor, frosting):
            self.flavor = flavor
            self.frosting = frosting

        def display_info(self):
            print(f"Cake Flavor: {self.flavor}, Frosting: {self.frosting}")
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    class Car:
        def display_info(self):
            print(f"Car Model: {self.model}, Year: {self.year}, Color: {self.size}")

def main():
    newDog = Dog("Buddy", 3)
    print(newDog.name, newDog.age)

    newEmployee = Employee("John Doe", 12345, "IT")
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)

    cake1 = Cake("Chocolate", "Vanilla")
    print("Cake 1:")
    cake1.display_info()

    cake2 = Cake("double choco;ate", "strawberry")
    print("Cake 2:")
        cake2.display_info()

        cat1 = Cat("Whiskers", 2, "long")
        cat2 = Cat("Mittens", 1, "short")

        print(f"{cat1.name}'s breed guess: {cat1.breedGuess()}")


car1 = Car("KIA", 2023, "grey")

print("Car information:")
car1.display_info()

if __name__ == "__main__":
    main()


        main()

main()
