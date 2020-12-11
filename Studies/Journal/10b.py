class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")


c1 = Cat("Max", 11)
c2 = Cat("Buddy", 3.5)

for i in [c1, c2]:
    i.info()
