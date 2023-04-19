# Super Class1
class Color:
    def Color_info(self):
        print("The color of the dog is white with black spots.")

# Super Class2
class Tail:
    def tail_size(self):
        print("Short and Cute tail")

#Super Class3
class Age:
    def age(self):
        print("The age is 2 months old")

# Creating Class from Super Class1,2 and 3
class Dog(Color, Tail, Age): 
    pass

# create an object of dog class
obj = Dog()

obj.Color_info()
obj.tail_size()
obj.age()