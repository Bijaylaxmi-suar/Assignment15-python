class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print(f"Hello!!My name is {self.name},I am {self.age} years old and I am a {self.gender}.")

p1 = Person("Bijaylaxmi Suar", 18, "Female")
p1.introduce()
