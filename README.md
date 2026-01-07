# 🐍 Python Summary Project

สรุปเนื้อหา Python ทั้งหมดแบบละเอียด พร้อมตัวอย่างโค้ดและคำอธิบาย

## 📚 เนื้อหาทั้งหมด 8 บท

| บท | หัวข้อ | ไฟล์ |
|:---:|--------|------|
| 1 | **Python Basics** - Variables, Data Types, Operators, I/O | `01_basics.py` |
| 2 | **Control Flow** - Conditionals, Loops, Match-Case, Comprehensions | `02_control_flow.py` |
| 3 | **Data Structures** - List, Tuple, Set, Dictionary, Collections | `03_data_structures.py` |
| 4 | **Functions** - Parameters, Lambda, Decorators, Generators | `04_functions.py` |
| 5 | **OOP** - Classes, Inheritance, Polymorphism, Encapsulation | `05_oop.py` |
| 6 | **File I/O & Exceptions** - Files, JSON/CSV, Exception Handling | `06_files_exceptions.py` |
| 7 | **Modules & Packages** - Modules, Standard Library, pip, venv | `07_modules.py` |
| 8 | **Advanced Python** - Type Hints, Async/Await, Testing, Best Practices | `08_advanced.py` |

## 🚀 วิธีใช้งาน

```bash
# รันโปรแกรมหลัก (พร้อมเมนูเลือกบท)
python main.py

# รันแต่ละบทแยก
python 01_basics.py
python 02_control_flow.py
# ... และอื่นๆ
```

## 📁 โครงสร้างโปรเจค

```
Python-summarize/
├── main.py              # Entry point
├── 01_basics.py         # บทที่ 1
├── 02_control_flow.py   # บทที่ 2
├── 03_data_structures.py # บทที่ 3
├── 04_functions.py      # บทที่ 4
├── 05_oop.py            # บทที่ 5
├── 06_files_exceptions.py # บทที่ 6
├── 07_modules.py        # บทที่ 7
├── 08_advanced.py       # บทที่ 8
├── __init__.py
└── README.md
```

---

## 📖 สรุปคำสั่ง Python ทั้งหมด

---

## 📘 บทที่ 1: Python Basics (พื้นฐาน)

### 1.1 Variables (ตัวแปร)

```python
# การกำหนดค่าตัวแปร
name = "สมชาย"           # String
age = 25                  # Integer
height = 175.5            # Float
is_student = True         # Boolean
nothing = None            # NoneType

# กำหนดหลายตัวแปรพร้อมกัน
x, y, z = 1, 2, 3
a = b = c = 0
```

### 1.2 Data Types (ชนิดข้อมูล)

```python
# Numeric Types
integer_num = 42                    # int
float_num = 3.14159                 # float
complex_num = 3 + 4j                # complex
binary_num = 0b1010                 # binary (= 10)
hex_num = 0xFF                      # hexadecimal (= 255)
big_num = 1_000_000                 # ใช้ _ คั่นหลัก

# String Types
single_quote = 'Hello'
double_quote = "World"
multi_line = """Multi-line string"""
raw_string = r"Path\to\file"        # Raw string
formatted = f"Name: {name}"         # f-string

# String Operations
text = "Python"
text.upper()                        # PYTHON
text.lower()                        # python
text.split()                        # แยกคำ
text.replace("old", "new")          # แทนที่
text[0:3]                           # Pyt (slicing)
len(text)                           # 6
```

### 1.3 String Formatting

```python
name = "John"
age = 30

# % formatting (แบบเก่า)
msg = "Name: %s, Age: %d" % (name, age)

# .format()
msg = "Name: {}, Age: {}".format(name, age)

# f-string (แนะนำ - Python 3.6+)
msg = f"Name: {name}, Age: {age}"
```

### 1.4 Type Conversion & Checking

```python
# Type Conversion
int("123")                  # string → int
float("3.14")               # string → float
str(42)                     # int → string

# Type Checking
type(42)                    # <class 'int'>
isinstance(42, int)         # True
isinstance(42, (int, float))  # True
```

### 1.5 Operators (ตัวดำเนินการ)

```python
# Arithmetic (คณิตศาสตร์)
10 + 3    # 13  (บวก)
10 - 3    # 7   (ลบ)
10 * 3    # 30  (คูณ)
10 / 3    # 3.33 (หาร)
10 // 3   # 3   (หารปัดเศษลง)
10 % 3    # 1   (หารเอาเศษ)
10 ** 3   # 1000 (ยกกำลัง)

# Comparison (เปรียบเทียบ)
5 == 5    # True  (เท่ากับ)
5 != 3    # True  (ไม่เท่ากับ)
5 > 3     # True  (มากกว่า)
5 < 3     # False (น้อยกว่า)
5 >= 5    # True  (≥)
5 <= 3    # False (≤)

# Logical (ตรรกะ)
True and False   # False
True or False    # True
not True         # False

# Assignment (กำหนดค่า)
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4

# Bitwise
a & b     # AND
a | b     # OR
a ^ b     # XOR
~a        # NOT
a << 1    # Left shift
a >> 1    # Right shift

# Identity & Membership
x is y         # เป็น object เดียวกัน
x is not y     # ไม่ใช่ object เดียวกัน
"a" in list    # อยู่ใน list
"a" not in list  # ไม่อยู่ใน list
```

### 1.6 Input/Output

```python
# Output
print("Hello, World!")
print("A", "B", sep=", ")        # A, B
print("Hello", end=" ")          # ไม่ขึ้นบรรทัดใหม่

# f-string formatting
print(f"Score: {95.5:.2f}")      # 2 ทศนิยม
print(f"Number: {42:05d}")       # 00042
print(f"Binary: {42:b}")         # 101010

# Input
name = input("Enter name: ")
age = int(input("Enter age: "))
```

---

## 📘 บทที่ 2: Control Flow (การควบคุมการทำงาน)

### 2.1 Conditional Statements

```python
# if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary Operator
status = "ผู้ใหญ่" if age >= 18 else "เด็ก"

# Nested if
if age >= 18:
    if has_license:
        print("ขับรถได้")
```

### 2.2 Loops (การวนรอบ)

```python
# for loop
for fruit in ["apple", "banana"]:
    print(fruit)

# for with range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# enumerate (ได้ทั้ง index และ value)
for index, item in enumerate(items):
    print(f"{index}: {item}")

# zip (วนหลาย list พร้อมกัน)
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop Controls
break       # ออกจาก loop
continue    # ข้ามไปรอบถัดไป
pass        # ไม่ทำอะไร (placeholder)

# for-else (else ทำงานเมื่อ loop จบปกติ)
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

### 2.3 Match-Case (Python 3.10+)

```python
match status:
    case 200:
        return "OK"
    case 404:
        return "Not Found"
    case _:              # default
        return "Unknown"

# Pattern matching
match point:
    case (0, 0):
        return "Origin"
    case (0, y):
        return f"On Y-axis at y={y}"
    case (x, 0):
        return f"On X-axis at x={x}"

# with guards
match num:
    case n if n < 0:
        return "Negative"
    case n if n == 0:
        return "Zero"
```

### 2.4 Comprehensions

```python
# List Comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]

# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(5)}

# Set Comprehension
unique_lens = {len(word) for word in words}

# Generator Expression
gen = (x**2 for x in range(10))
sum_squares = sum(x**2 for x in range(10))
```

---

## 📘 บทที่ 3: Data Structures (โครงสร้างข้อมูล)

### 3.1 List (รายการ)

```python
# สร้าง List
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4]]

# Indexing & Slicing
fruits[0]       # ตัวแรก
fruits[-1]      # ตัวสุดท้าย
fruits[1:4]     # index 1-3
fruits[:3]      # 3 ตัวแรก
fruits[2:]      # ตั้งแต่ index 2
fruits[::-1]    # กลับลำดับ

# List Methods
list.append(x)       # เพิ่มท้าย
list.insert(i, x)    # เพิ่มที่ตำแหน่ง i
list.extend([...])   # เพิ่มหลายตัว
list.remove(x)       # ลบค่า x ตัวแรก
list.pop()           # ลบและ return ตัวสุดท้าย
list.pop(i)          # ลบและ return ตำแหน่ง i
list.clear()         # ลบทั้งหมด
list.index(x)        # หาตำแหน่งของ x
list.count(x)        # นับจำนวน x
list.sort()          # เรียงลำดับ
list.reverse()       # กลับลำดับ
list.copy()          # คัดลอก

# List Operations
list1 + list2        # รวม list
list * 3             # ทำซ้ำ 3 รอบ
len(list)            # ความยาว
min(list), max(list) # ค่าน้อย/มากสุด
sum(list)            # ผลรวม

# Unpacking
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]
```

### 3.2 Tuple (ทูเพิล)

```python
# สร้าง Tuple (immutable)
single = (1,)              # ต้องมี comma
coords = (10, 20, 30)
coords = 10, 20, 30        # ไม่ต้องมีวงเล็บ

# Tuple Methods
tuple.index(x)     # หาตำแหน่ง
tuple.count(x)     # นับจำนวน

# Named Tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)
```

### 3.3 Set (เซต)

```python
# สร้าง Set (ไม่ซ้ำ, ไม่มีลำดับ)
empty_set = set()          # ไม่ใช่ {}
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3])  # {1, 2, 3}

# Set Methods
set.add(x)          # เพิ่มค่า
set.update([...])   # เพิ่มหลายค่า
set.remove(x)       # ลบ (error ถ้าไม่มี)
set.discard(x)      # ลบ (ไม่ error)
set.pop()           # ลบตัวใดตัวหนึ่ง

# Set Operations
A | B    # Union (รวม)
A & B    # Intersection (ร่วม)
A - B    # Difference (ต่าง)
A ^ B    # Symmetric Difference

A.union(B)
A.intersection(B)
A.difference(B)
A.issubset(B)      # A เป็น subset ของ B?
A.issuperset(B)    # A เป็น superset ของ B?
A.isdisjoint(B)    # ไม่มีสมาชิกร่วม?

# Frozen Set (immutable)
frozen = frozenset([1, 2, 3])
```

### 3.4 Dictionary (พจนานุกรม)

```python
# สร้าง Dictionary
person = {"name": "John", "age": 30}
from_tuples = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=25)
from_keys = dict.fromkeys(["a", "b"], 0)

# Accessing & Modifying
person["name"]              # John
person.get("name")          # John
person.get("salary", 0)     # 0 (default)
person["age"] = 31          # อัพเดท
person["email"] = "x@y.com" # เพิ่มใหม่
person.update({...})        # อัพเดทหลาย key

# Removing
del person["email"]
person.pop("age")           # ลบและ return value
person.popitem()            # ลบ item ล่าสุด

# Dictionary Methods
dict.keys()         # ได้ keys ทั้งหมด
dict.values()       # ได้ values ทั้งหมด
dict.items()        # ได้ (key, value) pairs
"key" in dict       # ตรวจสอบ key
dict.copy()         # คัดลอก
dict.setdefault("key", default)  # เพิ่มถ้าไม่มี

# Merging (Python 3.9+)
merged = dict1 | dict2
```

### 3.5 Collections Module

```python
from collections import Counter, defaultdict, deque

# Counter - นับจำนวน
counter = Counter("abracadabra")
counter.most_common(2)   # [('a', 5), ('b', 2)]

# defaultdict - dict ที่มี default value
dd = defaultdict(list)
dd["fruits"].append("apple")

dd_int = defaultdict(int)
dd_int["count"] += 1

# deque - Double-Ended Queue
dq = deque([1, 2, 3])
dq.append(4)         # เพิ่มขวา
dq.appendleft(0)     # เพิ่มซ้าย
dq.pop()             # ลบขวา
dq.popleft()         # ลบซ้าย
dq.rotate(1)         # หมุน
```

### 3.6 String Operations

```python
# Trimming
text.strip()         # ลบ whitespace ทั้งสองฝั่ง
text.lstrip()        # ลบ whitespace ซ้าย
text.rstrip()        # ลบ whitespace ขวา

# Case
text.upper()         # ตัวพิมพ์ใหญ่
text.lower()         # ตัวพิมพ์เล็ก
text.capitalize()    # ขึ้นต้นตัวใหญ่
text.title()         # Title Case
text.swapcase()      # สลับ case

# Checking
str.isalpha()        # ตัวอักษรทั้งหมด?
str.isdigit()        # ตัวเลขทั้งหมด?
str.isalnum()        # ตัวอักษรหรือตัวเลข?
str.isspace()        # whitespace?

# Finding & Replacing
text.find("word")        # หาตำแหน่งแรก (-1 ถ้าไม่เจอ)
text.rfind("word")       # หาตำแหน่งสุดท้าย
text.count("word")       # นับจำนวน
text.replace("old", "new")

# Split & Join
text.split(",")          # แยกเป็น list
",".join(list)           # รวม list เป็น string
text.splitlines()        # แยกตาม newline

# Justify
text.ljust(10, "-")      # Python----
text.rjust(10, "-")      # ----Python
text.center(10, "-")     # --Python--
text.zfill(10)           # 0000Python

# Start/End
text.startswith("Py")    # True/False
text.endswith(".py")     # True/False
```

---

## 📘 บทที่ 4: Functions (ฟังก์ชัน)

### 4.1 Basic Functions

```python
# Function พื้นฐาน
def greet(name):
    return f"Hello, {name}!"

# Multiple return values
def calculate(a, b):
    return a + b, a - b, a * b  # return tuple

sum_val, diff, product = calculate(10, 3)
```

### 4.2 Parameters

```python
# Default Parameters
def greet(name, greeting="Hello"):
    return f"{greeting} {name}!"

# *args - รับ arguments ไม่จำกัด
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs - รับ keyword arguments ไม่จำกัด
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)

# Combined
def func(a, b, *args, **kwargs):
    pass

# Keyword-only (หลัง *)
def func(name, *, greeting="Hi"):
    pass

# Positional-only (ก่อน /) - Python 3.8+
def func(a, b, /):
    pass
```

### 4.3 Scope

```python
# Global variable
global_var = "global"

def test():
    local_var = "local"
    global global_var    # ใช้ global
    global_var = "modified"

# Nonlocal (nested function)
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    return inner
```

### 4.4 Lambda Functions

```python
# Lambda syntax
add = lambda x, y: x + y
square = lambda x: x ** 2

# ใช้กับ built-in functions
sorted(items, key=lambda x: x[1])  # sort by index 1

# map - apply function to each
list(map(lambda x: x**2, [1, 2, 3]))

# filter - keep items that pass
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

# reduce - combine items
from functools import reduce
reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24
```

### 4.5 Decorators

```python
# Basic Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# functools.wraps - รักษา metadata
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 4.6 Generators

```python
# Generator function (yield)
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# การใช้งาน
gen = count_up_to(5)
next(gen)  # 1
next(gen)  # 2

for num in count_up_to(5):
    print(num)

# Generator Expression
squares = (x**2 for x in range(10))

# yield from
def chain(*iterables):
    for it in iterables:
        yield from it
```

### 4.7 Built-in Functions

```python
# Math
abs(-5)              # 5
round(3.7)           # 4
round(3.14159, 2)    # 3.14
pow(2, 3)            # 8
divmod(17, 5)        # (3, 2)

# Sequence
len(items)           # ความยาว
min(items)           # ค่าน้อยสุด
max(items)           # ค่ามากสุด
sum(items)           # ผลรวม
sorted(items)        # เรียงลำดับ (return list ใหม่)
reversed(items)      # กลับลำดับ (return iterator)

# Type
type(obj)            # ได้ชนิดข้อมูล
isinstance(obj, int) # ตรวจสอบชนิด
callable(obj)        # เรียกใช้ได้ไหม?

# Iterator
range(5)             # 0, 1, 2, 3, 4
zip([1,2], [3,4])    # [(1,3), (2,4)]
enumerate(['a','b']) # [(0,'a'), (1,'b')]
any([False, True])   # True (มี True อย่างน้อย 1)
all([True, True])    # True (ทั้งหมดเป็น True)
```

---

## 📘 บทที่ 5: OOP (Object-Oriented Programming)

### 5.1 Classes & Objects

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# สร้าง Object
dog = Dog("Buddy", 3)
print(dog.name)       # Buddy
print(dog.bark())     # Buddy says Woof!
print(Dog.species)    # Canis familiaris
```

### 5.2 Method Types

```python
class MyClass:
    class_attr = "shared"
    
    def __init__(self, value):
        self.instance_attr = value
    
    # Instance method - รับ self
    def instance_method(self):
        return self.instance_attr
    
    # Class method - รับ cls
    @classmethod
    def class_method(cls):
        return cls.class_attr
    
    # Static method - ไม่รับ self/cls
    @staticmethod
    def static_method():
        return "static"

# Factory method
@classmethod
def from_string(cls, data_string):
    parts = data_string.split(",")
    return cls(*parts)
```

### 5.3 Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # เรียก parent
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Woof!"

# Multiple Inheritance
class Duck(Animal, Flyable, Swimmable):
    pass

# MRO (Method Resolution Order)
Duck.__mro__
```

### 5.4 Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance    # protected (convention)
        self.__pin = "1234"        # private (name mangling)
    
    # Property (getter)
    @property
    def balance(self):
        return self._balance
    
    # Setter
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Cannot be negative")
        self._balance = value
    
    # Deleter
    @balance.deleter
    def balance(self):
        self._balance = 0
```

### 5.5 Polymorphism

```python
# Duck Typing
def start_vehicle(vehicle):
    print(vehicle.start())  # ไม่สนใจ class, แค่มี start()

# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
```

### 5.6 Abstract Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

### 5.7 Special Methods (Magic Methods)

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):          # print()
        return f"'{self.title}'"
    
    def __repr__(self):         # debug
        return f"Book('{self.title}', {self.pages})"
    
    def __eq__(self, other):    # ==
        return self.title == other.title
    
    def __lt__(self, other):    # <
        return self.pages < other.pages
    
    def __len__(self):          # len()
        return self.pages
    
    def __contains__(self, item):  # in
        return item in self.title
    
    def __call__(self, msg):    # object()
        return f"{self.title}: {msg}"
    
    def __getitem__(self, key): # object[key]
        return self.title[key]
    
    # Context manager
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass
```

### 5.8 Data Classes

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grade: float = 0.0
    courses: List[str] = field(default_factory=list)

# ไม่ต้องเขียน __init__, __repr__, __eq__

@dataclass(frozen=True)  # Immutable
class Point:
    x: int
    y: int
```

---

## 📘 บทที่ 6: File I/O & Exceptions

### 6.1 File Operations

```python
# Mode: 'r' read, 'w' write, 'a' append, 'x' create
#       'b' binary, 't' text (default)

# อ่านไฟล์
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()         # อ่านทั้งหมด
    # หรือ
    lines = f.readlines()      # อ่านเป็น list
    # หรือ
    for line in f:             # อ่านทีละบรรทัด
        print(line.strip())

# เขียนไฟล์
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("Hello\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# File Methods
f.read(size)      # อ่าน size chars
f.readline()      # อ่านบรรทัด
f.tell()          # ตำแหน่งปัจจุบัน
f.seek(offset)    # ย้ายตำแหน่ง
```

### 6.2 JSON

```python
import json

# เขียน JSON
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# อ่าน JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# String ↔ JSON
json_str = json.dumps(data)
data = json.loads(json_str)
```

### 6.3 CSV

```python
import csv

# เขียน CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# อ่าน CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Dict Writer/Reader
with open('data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(data)

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))
```

### 6.4 OS & Path

```python
import os
from pathlib import Path

# os module
os.getcwd()                  # current directory
os.listdir('.')              # list files
os.path.exists('file.txt')   # ไฟล์มีไหม?
os.path.isfile('file.txt')   # เป็นไฟล์?
os.path.isdir('folder')      # เป็น folder?
os.path.join('a', 'b', 'c')  # a/b/c
os.makedirs('a/b/c', exist_ok=True)
os.remove('file.txt')        # ลบไฟล์

# pathlib (modern)
p = Path('folder') / 'file.txt'
p.exists()
p.is_file()
p.parent                     # folder
p.name                       # file.txt
p.stem                       # file
p.suffix                     # .txt
p.read_text()
p.write_text('content')
```

### 6.5 Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# try-except-else-finally
try:
    file = open('test.txt')
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())  # ทำถ้าไม่มี error
finally:
    print("Cleanup")    # ทำเสมอ

# Raise exception
if age < 0:
    raise ValueError("Age cannot be negative")

# Re-raise
except Exception:
    print("Logging...")
    raise

# Custom Exception
class ValidationError(Exception):
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(message)

# Exception Chaining
except ZeroDivisionError as e:
    raise RuntimeError("Failed") from e
```

### 6.6 Context Managers

```python
# Using with
with open('file.txt') as f:
    content = f.read()

# Multiple contexts
with open('in.txt') as fin, open('out.txt', 'w') as fout:
    fout.write(fin.read())

# Custom Context Manager (class)
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        print(f"Took {time.time() - self.start:.2f}s")

# Custom Context Manager (decorator)
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Took {time.time() - start:.2f}s")

# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
```

---

## 📘 บทที่ 7: Modules & Packages

### 7.1 Import

```python
# Basic import
import math
math.sqrt(16)

# Import specific items
from math import sqrt, pi

# Import with alias
import math as m
from math import factorial as fact

# Import all (ไม่แนะนำ)
from math import *
```

### 7.2 Creating Modules

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# ใช้งาน
import mymodule
mymodule.greet("Alice")

# __name__ guard
if __name__ == "__main__":
    # รันเมื่อ execute โดยตรง
    print("Running directly")
```

### 7.3 Packages

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# __init__.py
from .module1 import func1
from .module2 import func2
__all__ = ['func1', 'func2']

# Usage
from mypackage import func1
from mypackage.subpackage import module3
```

### 7.4 Standard Library

```python
# datetime
from datetime import datetime, date, timedelta
now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
datetime.strptime("2024-01-15", "%Y-%m-%d")
now.strftime("%Y-%m-%d %H:%M:%S")

# random
import random
random.random()              # 0.0 - 1.0
random.randint(1, 10)        # 1-10
random.choice(['a', 'b'])    # สุ่มเลือก
random.sample(range(10), 3)  # สุ่ม 3 ตัว
random.shuffle(list)         # สลับ

# collections
from collections import Counter, defaultdict, deque

# itertools
import itertools
itertools.count(1)           # 1, 2, 3, ...
itertools.cycle('AB')        # A, B, A, B, ...
itertools.chain([1,2], [3,4])  # 1, 2, 3, 4
itertools.permutations('AB', 2)
itertools.combinations('ABC', 2)

# functools
from functools import reduce, partial, lru_cache

@lru_cache(maxsize=100)     # cache results
def expensive_func(n):
    return n * n

# re (Regular Expressions)
import re
re.search(r'\w+@\w+\.\w+', text)
re.findall(r'\d+', text)
re.sub(r'old', 'new', text)
re.split(r'\s+', text)

# hashlib
import hashlib
hashlib.md5(text.encode()).hexdigest()
hashlib.sha256(text.encode()).hexdigest()
```

### 7.5 pip & Virtual Environments

```bash
# pip
pip install package
pip install package==1.2.3
pip install -r requirements.txt
pip list
pip freeze > requirements.txt
pip uninstall package

# Virtual Environment
python -m venv myenv
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # macOS/Linux
deactivate
```

---

## 📘 บทที่ 8: Advanced Python

### 8.1 Type Hints

```python
from typing import List, Dict, Optional, Union, Callable, TypeVar

# Basic
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Variables
name: str = "John"
age: int = 30

# Collections
def process(items: List[str]) -> Dict[str, int]:
    pass

# Optional & Union
def find(id: int) -> Optional[str]:  # str หรือ None
    pass

def process(value: Union[str, int]) -> str:  # str หรือ int
    pass

# Python 3.10+
def process(value: str | int) -> str:
    pass

# Callable
def apply(func: Callable[[int, int], int]) -> int:
    pass

# TypeVar (Generics)
T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

# Literal
from typing import Literal

def set_status(status: Literal["active", "inactive"]) -> None:
    pass

# TypedDict
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
```

### 8.2 Async/Await

```python
import asyncio

# Async function
async def fetch_data():
    await asyncio.sleep(1)
    return "Data"

# Run
asyncio.run(fetch_data())

# Concurrent execution
async def main():
    results = await asyncio.gather(
        fetch_data("API 1"),
        fetch_data("API 2"),
        fetch_data("API 3")
    )

# Timeout
async def with_timeout():
    try:
        result = await asyncio.wait_for(slow_op(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Timed out!")

# Async generator
async def async_counter(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

# Async context manager
async with AsyncResource() as resource:
    await resource.do_something()
```

### 8.3 Testing

```python
# unittest
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# Run: python -m unittest test_file.py

# pytest (pip install pytest)
def test_add():
    assert add(2, 3) == 5

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Run: pytest test_file.py -v

# Mocking
from unittest.mock import Mock, patch

mock_func = Mock(return_value=42)
mock_func.assert_called_once()

with patch.object(APIClient, 'fetch') as mock:
    mock.return_value = {"data": "test"}
```

### 8.4 Design Patterns

```python
# Singleton
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory
class AnimalFactory:
    @staticmethod
    def create(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        return animals[animal_type]()

# Observer
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer(message)
```

### 8.5 Performance Tips

```python
# Generator ประหยัด memory กว่า List
squares = (x**2 for x in range(1000000))

# String join เร็วกว่า +=
result = "".join(str(i) for i in range(1000))

# ใช้ Built-in functions
total = sum(numbers)  # เร็วกว่า loop

# Caching
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_func(n):
    return n * n
```

---

## 🎯 เหมาะสำหรับ

- 🔰 ผู้เริ่มต้นเรียน Python
- 📖 นักเรียน/นักศึกษาที่ต้องการสรุปเนื้อหา
- 🔄 ผู้ที่ต้องการทบทวน Python
- 👨‍💻 Developers ที่ต้องการ reference

## 📚 แหล่งเรียนรู้เพิ่มเติม

- [Official Python Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python PEP 8 Style Guide](https://pep8.org/)

---

## 📁 โครงสร้างโปรเจคตามมาตรฐาน

```
my_project/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── modules/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
│   └── README.md
│
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

### คำอธิบายแต่ละส่วน

- **src/** - โฟลเดอร์หลักที่เก็บ source code ทั้งหมด
  - `__init__.py` ทำให้ Python รู้จักว่านี่คือ package
  - `main.py` จุดเริ่มต้นของโปรแกรม (entry point)
  - `config.py` เก็บค่า configuration ต่างๆ
  - `modules/` แยกโค้ดเป็นโมดูลย่อยตามหน้าที่
- **tests/** - เก็บไฟล์สำหรับทดสอบโค้ด (unit tests)
- **data/** - เก็บข้อมูล input และ output
- **docs/** - เอกสารประกอบโปรเจค
- **requirements.txt** - รายการ dependencies ที่ต้องติดตั้ง
- **setup.py** - สำหรับการติดตั้งโปรเจคเป็น package