from abc import ABC

class User(ABC):
    def __init__(self, name , phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Employee(User):
    def __init__(self, name, phone, email, address,age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("rahim", "rahim@gmail.com", 932843, "dhaka", 23, "chef", 12000)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees= []

    def add_employee(self, name, email, phone, address):
        self.employee = Employee(name, email, phone, address)
        