# Base class
class Animal:
    def  move(self):
        print("All Animal move in their own way")
        
    # dog
class Dog(Animal):
    def move(self):
        print("Dog runs")
        # bird
class Bird(Animal):
    def move(self):
        print("Bird flies")
        # fish
class Fish(Animal):
    def move(self):
        print("Fish swims")
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()
