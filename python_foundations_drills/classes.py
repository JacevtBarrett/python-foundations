class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary = self.salary * (1 + percent / 100)

class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}.")
        print("Tests are done")

class Developer(Employee):
    #called method overriding because it overrides the method in the parent class+
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus

employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("John", 30, 2000)

employee1.increase_salary(10)
employee2.increase_salary(10, 100)
print(employee1.salary)
print(employee2.salary)