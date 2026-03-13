# 1. Student class
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

s1 = Student("Sameer", 20, 85)
print(s1.name, s1.age, s1.marks)


# 2. Employee class
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def show(self):
        print(self.id, self.name, self.salary)

e1 = Employee(101, "Sam", 50000)
e1.show()


# 3. Car class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

c1 = Car("BMW", "X5", 7000000)
print(c1.brand, c1.model, c1.price)


# 4. Laptop class
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

l1 = Laptop("HP", "16GB", 70000)
l1.update_price(65000)
print(l1.price)


# 5. Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("Python", "Guido", 500)
del b1.price


# 6. College class
class College:
    college_name = "ABC College"

c1 = College()
print(c1.college_name)
print(College.college_name)


# 7. BankAccount class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

b1 = BankAccount("Sam", 1000)
b1.deposit(500)
print(b1.balance)


# 8. Mobile class
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

m1 = Mobile("OnePlus", 30000)
m1.update_price(28000)
print(m1.price)


# 9. Teacher class
class Teacher:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name, Teacher.school_name)

t1 = Teacher("Rahul")
t1.show()


# 10. Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def delete_price(self):
        del self.price

p1 = Product("Laptop", 60000)
p1.delete_price()


# 11. Employee class with class variable
class Employee2:
    company = "TCS"

e1 = Employee2()
e2 = Employee2()
print(e1.company)
print(e2.company)


# 12. Student class with class method
class Student2:
    school_name = "ABC School"

    @classmethod
    def update_school(cls, new_name):
        cls.school_name = new_name

Student2.update_school("XYZ School")
print(Student2.school_name)


# 13. Bike class
class Bike:
    category = "Two Wheeler"

b1 = Bike()
b2 = Bike()

print(b1.category)
print(b2.category)


# 14. Hospital class
class Hospital:
    hospital_name = "City Hospital"

    @classmethod
    def change_name(cls, new_name):
        cls.hospital_name = new_name

Hospital.change_name("Apollo Hospital")
print(Hospital.hospital_name)


# 15. Movie class
class Movie:
    def __init__(self, name, hero, rating):
        self.name = name
        self.hero = hero
        self.rating = rating

    def show(self):
        print(self.name, self.hero, self.rating)

m1 = Movie("RRR", "NTR", 9)
m1.show()


# 16. Course class
class Course:
    platform = "Online"

    @classmethod
    def update_platform(cls, new_platform):
        cls.platform = new_platform

Course.update_platform("Offline")
print(Course.platform)


# 17. Customer class
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def update_city(self, new_city):
        self.city = new_city

c1 = Customer("Sam", "Hyderabad")
c1.update_city("Mumbai")
print(c1.city)


# 18. Company class
class Company:
    location = "India"

del Company.location


# 19. Library class
class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author

l1 = Library("Python", "Guido")
del l1.author


# 20. Vehicle class
class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)

    def update_price(self, new_price):
        self.price = new_price

    def delete_price(self):
        del self.price

v1 = Vehicle("Car", 500000)
v1.show()
v1.update_price(450000)
v1.show()
v1.delete_price()