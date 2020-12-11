class Employee:
    def __init__(self, name, age, gender):
        self.name - name
        self.age = age
        self.gender = gender

    def __del__(self):
        c_name = self.__class__.__name__


e1 = Employee("rajesh", "25", "male")
e2 = Employee("Prajesh", "30", "Male")
print(e1.name, e2.age)
print(e2.name, e1.gender)

