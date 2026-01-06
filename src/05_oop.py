"""
=============================================================================
📘 บทที่ 5: Object-Oriented Programming (OOP)
=============================================================================
เนื้อหา: Classes, Objects, Inheritance, Polymorphism, Encapsulation
=============================================================================
"""

# =============================================================================
# 5.1 Classes และ Objects (คลาสและออบเจ็กต์)
# =============================================================================

# Class = พิมพ์เขียว (blueprint) สำหรับสร้าง Object
# Object = Instance ของ Class

# --- Basic Class ---
class Dog:
    """Class พื้นฐาน"""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (Initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# สร้าง Object (Instance)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)          # Buddy
print(dog1.bark())        # Buddy says Woof!
print(dog1.description()) # Buddy is 3 years old
print(Dog.species)        # Canis familiaris

# =============================================================================
# 5.2 Instance, Class, และ Static Methods
# =============================================================================

class MyClass:
    class_attr = "I am a class attribute"
    
    def __init__(self, value):
        self.instance_attr = value
    
    # Instance method - รับ self
    def instance_method(self):
        return f"Instance method: {self.instance_attr}"
    
    # Class method - รับ cls
    @classmethod
    def class_method(cls):
        return f"Class method: {cls.class_attr}"
    
    # Static method - ไม่รับ self หรือ cls
    @staticmethod
    def static_method():
        return "Static method: I don't need self or cls"

obj = MyClass("Hello")
print(obj.instance_method())   # Instance method: Hello
print(MyClass.class_method())  # Class method: I am a class attribute
print(MyClass.static_method()) # Static method: ...

# --- Factory Method using @classmethod ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Factory method สร้าง Person จากปีเกิด"""
        import datetime
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)
    
    @classmethod
    def from_string(cls, person_string):
        """Factory method สร้าง Person จาก string"""
        name, age = person_string.split(",")
        return cls(name.strip(), int(age.strip()))

person1 = Person("John", 30)
person2 = Person.from_birth_year("Alice", 1995)
person3 = Person.from_string("Bob, 25")

print(f"{person1.name}: {person1.age}")
print(f"{person2.name}: {person2.age}")
print(f"{person3.name}: {person3.age}")

# =============================================================================
# 5.3 Inheritance (การสืบทอด)
# =============================================================================

# --- Basic Inheritance ---
class Animal:
    """Base class (Parent)"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")
    
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    """Derived class (Child)"""
    def __init__(self, name, breed):
        super().__init__(name)  # เรียก constructor ของ parent
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching"

class Cat(Animal):
    """Another derived class"""
    def speak(self):
        return f"{self.name} says Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching"

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())   # Buddy says Woof!
print(dog.eat())     # Buddy is eating (inherited)
print(dog.fetch())   # Buddy is fetching
print(cat.speak())   # Whiskers says Meow!
print(cat.scratch()) # Whiskers is scratching

# --- Multiple Inheritance ---
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from multiple classes"""
    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(duck.speak())  # Donald says Quack!
print(duck.fly())    # I can fly!
print(duck.swim())   # I can swim!

# --- Method Resolution Order (MRO) ---
print(Duck.__mro__)  # ลำดับการค้นหา method

# =============================================================================
# 5.4 Encapsulation (การห่อหุ้ม)
# =============================================================================

class BankAccount:
    """ตัวอย่าง Encapsulation"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner           # public
        self._balance = balance      # protected (convention)
        self.__pin = "1234"          # private (name mangling)
    
    # Getter
    @property
    def balance(self):
        return self._balance
    
    # Setter
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    # Deleter
    @balance.deleter
    def balance(self):
        print("Deleting balance")
        self._balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Invalid amount or insufficient funds"
    
    def __verify_pin(self, pin):  # private method
        return pin == self.__pin

account = BankAccount("John", 1000)
print(account.balance)           # 1000 (ใช้ property)
account.balance = 2000           # ใช้ setter
print(account.balance)           # 2000
print(account.deposit(500))      # Deposited 500
print(account.withdraw(200))     # Withdrew 200

# Private attribute ยังเข้าถึงได้ผ่าน name mangling (แต่ไม่ควรทำ)
# print(account._BankAccount__pin)  # 1234

# =============================================================================
# 5.5 Polymorphism (หลายรูปแบบ)
# =============================================================================

# --- Polymorphism through Inheritance ---
def animal_sound(animal):
    """รับ Animal object ใดก็ได้"""
    print(animal.speak())

animals = [Dog("Buddy", "Labrador"), Cat("Whiskers"), Duck("Donald")]
for animal in animals:
    animal_sound(animal)

# --- Duck Typing ---
# "If it walks like a duck and quacks like a duck, it's a duck"
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} car is starting"

class Motorcycle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} motorcycle is starting"

def start_vehicle(vehicle):
    """ไม่สนใจว่าเป็น class อะไร แค่มี start() ก็พอ"""
    print(vehicle.start())

start_vehicle(Car("Toyota"))      # Toyota car is starting
start_vehicle(Motorcycle("Honda"))  # Honda motorcycle is starting

# --- Operator Overloading ---
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)   # (4, 6)
print(v1 - v2)   # (2, 2)
print(v1 * 2)    # (6, 8)
print(v1 == v2)  # False

# =============================================================================
# 5.6 Abstract Classes และ Interfaces
# =============================================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract Base Class"""
    
    @abstractmethod
    def area(self):
        """ต้อง implement ใน subclass"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """ต้อง implement ใน subclass"""
        pass
    
    def description(self):
        """Concrete method - ใช้งานได้เลย"""
        return f"I am a shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# shape = Shape()  # Error! ไม่สามารถ instantiate abstract class
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle: area={rect.area()}, perimeter={rect.perimeter()}")
print(f"Circle: area={circle.area():.2f}, perimeter={circle.perimeter():.2f}")
print(rect.description())

# =============================================================================
# 5.7 Special Methods (Magic/Dunder Methods)
# =============================================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representations
    def __str__(self):
        """สำหรับ print() - human-readable"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """สำหรับ debug - unambiguous"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Comparison
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __le__(self, other):
        return self.pages <= other.pages
    
    # Length
    def __len__(self):
        return self.pages
    
    # Container
    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()
    
    # Callable
    def __call__(self, message):
        return f"{self.title}: {message}"
    
    # Context manager
    def __enter__(self):
        print(f"Opening {self.title}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.title}")
    
    # Indexing
    def __getitem__(self, index):
        return self.title[index]

book1 = Book("Python Crash Course", "Eric Matthes", 560)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 480)

print(str(book1))          # 'Python Crash Course' by Eric Matthes
print(repr(book1))         # Book('Python Crash Course', 'Eric Matthes', 560)
print(book1 == book2)      # False
print(book1 > book2)       # True (560 > 480)
print(len(book1))          # 560
print("Python" in book1)   # True
print(book1("Great book!"))  # Python Crash Course: Great book!
print(book1[0:6])          # Python

# Context manager
with book1 as b:
    print(f"Reading {b.title}")

# =============================================================================
# 5.8 Data Classes (Python 3.7+)
# =============================================================================

from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    """Data class ลดการเขียน boilerplate code"""
    name: str
    age: int
    grade: float = 0.0  # default value
    courses: List[str] = field(default_factory=list)  # mutable default
    
    def is_passing(self):
        return self.grade >= 2.0

# ไม่ต้องเขียน __init__, __repr__, __eq__
student = Student("Alice", 20, 3.5, ["Math", "Science"])
print(student)  # Student(name='Alice', age=20, grade=3.5, courses=['Math', 'Science'])
print(student.is_passing())  # True

# Frozen dataclass (immutable)
@dataclass(frozen=True)
class Point:
    x: int
    y: int

pt = Point(3, 4)
# pt.x = 5  # Error! frozen dataclass

# =============================================================================
# 5.9 Composition vs Inheritance
# =============================================================================

# --- Composition (Has-a relationship) ---
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine starting..."

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    """Car HAS an Engine and Wheels (Composition)"""
    def __init__(self, brand, horsepower, wheel_size):
        self.brand = brand
        self.engine = Engine(horsepower)  # composition
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def start(self):
        return f"{self.brand}: {self.engine.start()}"

car = Car("Toyota", 150, 17)
print(car.start())  # Toyota: Engine starting...

# --- Inheritance (Is-a relationship) ---
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class SportsCar(Vehicle):  # SportsCar IS a Vehicle
    def __init__(self, brand, top_speed):
        super().__init__(brand)
        self.top_speed = top_speed

# =============================================================================
# 5.10 ตัวอย่างโปรแกรม
# =============================================================================

class Employee:
    """ระบบจัดการพนักงาน"""
    
    employee_count = 0
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self._salary = salary
        self.id = Employee.employee_count + 1
        Employee.employee_count += 1
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    def give_raise(self, percentage):
        self._salary *= (1 + percentage / 100)
        return f"{self.name} got a {percentage}% raise. New salary: {self._salary:,.2f}"
    
    def __str__(self):
        return f"[{self.id}] {self.name} - {self.position} (${self._salary:,.2f})"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, "Manager", salary)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee):
        self.team.append(employee)
        return f"Added {employee.name} to {self.department}"
    
    def team_report(self):
        report = f"\n{self.department} Team ({self.name}):\n"
        report += "-" * 40 + "\n"
        for emp in self.team:
            report += f"  {emp}\n"
        return report

# ใช้งาน
if __name__ == "__main__":
    print("\n=== Employee Management System ===")
    
    # สร้าง Manager
    manager = Manager("John Smith", 80000, "Engineering")
    
    # สร้าง Employees
    emp1 = Employee("Alice Johnson", "Developer", 60000)
    emp2 = Employee("Bob Williams", "Designer", 55000)
    emp3 = Employee("Charlie Brown", "Developer", 62000)
    
    # เพิ่มเข้าทีม
    manager.add_team_member(emp1)
    manager.add_team_member(emp2)
    manager.add_team_member(emp3)
    
    # แสดงรายงาน
    print(manager)
    print(manager.team_report())
    
    # ขึ้นเงินเดือน
    print(emp1.give_raise(10))
    
    print(f"\nTotal employees: {Employee.employee_count}")
    
    print("\n" + "="*50)
    print("📘 บทที่ 5: OOP - เสร็จสมบูรณ์!")
    print("="*50)
