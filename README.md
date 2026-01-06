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
cd src
python main.py

# รันแต่ละบทแยก
python 01_basics.py
python 02_control_flow.py
# ... และอื่นๆ
```

## 📁 โครงสร้างโปรเจค

```
Python-summarize/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── 01_basics.py         # บทที่ 1
│   ├── 02_control_flow.py   # บทที่ 2
│   ├── 03_data_structures.py # บทที่ 3
│   ├── 04_functions.py      # บทที่ 4
│   ├── 05_oop.py            # บทที่ 5
│   ├── 06_files_exceptions.py # บทที่ 6
│   ├── 07_modules.py        # บทที่ 7
│   └── 08_advanced.py       # บทที่ 8
└── README.md
```

## 📝 หัวข้อหลักแต่ละบท

### 📘 บทที่ 1: Python Basics
- Variables & Naming conventions
- Data Types (int, float, str, bool, None)
- Operators (Arithmetic, Comparison, Logical, Bitwise)
- Input/Output (print, input, f-strings)
- Type conversion & checking

### 📘 บทที่ 2: Control Flow
- if/elif/else statements
- for & while loops
- break, continue, pass
- match-case (Python 3.10+)
- List/Dict/Set comprehensions

### 📘 บทที่ 3: Data Structures
- List (methods, slicing, operations)
- Tuple (immutable sequences)
- Set (unique elements, operations)
- Dictionary (key-value pairs)
- Collections module (Counter, defaultdict, deque)

### 📘 บทที่ 4: Functions
- Parameters (*args, **kwargs)
- Lambda functions
- Decorators
- Generators & yield
- Higher-order functions

### 📘 บทที่ 5: OOP
- Classes & Objects
- Instance, Class, Static methods
- Inheritance (single, multiple)
- Polymorphism & Duck typing
- Encapsulation (public, protected, private)
- Abstract classes
- Data classes

### 📘 บทที่ 6: File I/O & Exceptions
- Reading/Writing files
- JSON, CSV handling
- try/except/else/finally
- Custom exceptions
- Context managers (with statement)

### 📘 บทที่ 7: Modules & Packages
- import statements
- Creating modules & packages
- Standard library overview
- pip & virtual environments
- __name__ == "__main__"

### 📘 บทที่ 8: Advanced Python
- Type hints & typing module
- Async/Await programming
- Testing (unittest, pytest)
- Best practices & PEP 8
- Design patterns
- Performance optimization

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

### คำอธิบายแต่ละส่วน

src/ - โฟลเดอร์หลักที่เก็บ source code ทั้งหมด

__init__.py ทำให้ Python รู้จักว่านี่คือ package
main.py จุดเริ่มต้นของโปรแกรม (entry point)
config.py เก็บค่า configuration ต่างๆ
modules/ แยกโค้ดเป็นโมดูลย่อยตามหน้าที่

tests/ - เก็บไฟล์สำหรับทดสอบโค้ด (unit tests)
data/ - เก็บข้อมูล input และ output
docs/ - เอกสารประกอบโปรเจค
requirements.txt - รายการ dependencies ที่ต้องติดตั้ง
setup.py - สำหรับการติดตั้งโปรเจคเป็น package