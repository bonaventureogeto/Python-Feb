class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def vote(self):
        if self.age >= 18:
            print("You can vote")
        else:
            print("You can't vote")
            

my_person = Person('John', 30, 'Male')

print(my_person.vote())

