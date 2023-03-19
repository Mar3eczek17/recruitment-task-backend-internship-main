class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)
print(miles)
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Wow"))
miles.species = "Felis silvestris"
print(miles.species)
names = ["Fletcher", "David", "Dan"]
print(names)
print(miles)