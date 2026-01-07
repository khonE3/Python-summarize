"""
=============================================================================
📘 บทที่ 3: Data Structures (โครงสร้างข้อมูล)
=============================================================================
เนื้อหา: List, Tuple, Set, Dictionary, String Operations
=============================================================================
"""

# =============================================================================
# 3.1 List (รายการ)
# =============================================================================

# --- การสร้าง List ---
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]
from_range = list(range(1, 6))  # [1, 2, 3, 4, 5]

# --- Indexing และ Slicing ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
print(fruits[0])     # apple (ตัวแรก)
print(fruits[-1])    # elderberry (ตัวสุดท้าย)
print(fruits[-2])    # date (ตัวรองสุดท้าย)

# Slicing [start:end:step]
print(fruits[1:4])   # ['banana', 'cherry', 'date']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:])    # ['cherry', 'date', 'elderberry']
print(fruits[::2])   # ['apple', 'cherry', 'elderberry'] (ทุก 2 ตัว)
print(fruits[::-1])  # กลับลำดับ

# --- List Methods ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# เพิ่มข้อมูล
numbers.append(7)          # เพิ่มท้าย [3,1,4,1,5,9,2,6,7]
numbers.insert(0, 0)       # เพิ่มที่ตำแหน่ง 0 [0,3,1,4,1,5,9,2,6,7]
numbers.extend([8, 9])     # เพิ่มหลายตัว [0,3,1,4,1,5,9,2,6,7,8,9]

# ลบข้อมูล
numbers.remove(1)          # ลบค่า 1 ตัวแรก
popped = numbers.pop()     # ลบและ return ตัวสุดท้าย
popped = numbers.pop(0)    # ลบและ return ตำแหน่งที่ 0
# del numbers[0]           # ลบตำแหน่งที่ 0
# numbers.clear()          # ลบทั้งหมด

# ค้นหาและนับ
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(numbers.index(4))    # 2 (ตำแหน่งของ 4)
print(numbers.count(1))    # 2 (จำนวน 1 ใน list)
print(4 in numbers)        # True

# เรียงลำดับ
numbers.sort()             # เรียงจากน้อยไปมาก (in-place)
numbers.sort(reverse=True) # เรียงจากมากไปน้อย
sorted_nums = sorted(numbers)  # return list ใหม่

# กลับลำดับ
numbers.reverse()          # กลับลำดับ (in-place)
reversed_nums = list(reversed(numbers))  # return iterator

# คัดลอก List
copy1 = numbers.copy()     # shallow copy
copy2 = numbers[:]         # shallow copy
copy3 = list(numbers)      # shallow copy
import copy
deep_copy = copy.deepcopy(nested)  # deep copy สำหรับ nested list

# --- List Operations ---
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)       # [1, 2, 3, 4, 5, 6] (รวม list)
print(list1 * 3)           # [1, 2, 3, 1, 2, 3, 1, 2, 3] (ทำซ้ำ)
print(len(list1))          # 3 (ความยาว)
print(min(list1))          # 1 (ค่าน้อยสุด)
print(max(list1))          # 3 (ค่ามากสุด)
print(sum(list1))          # 6 (ผลรวม)

# --- Unpacking ---
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# =============================================================================
# 3.2 Tuple (ทูเพิล)
# =============================================================================

# Tuple คล้าย List แต่เปลี่ยนแปลงไม่ได้ (immutable)

# --- การสร้าง Tuple ---
empty_tuple = ()
single = (1,)              # ต้องมี comma สำหรับ tuple ตัวเดียว
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))
from_list = tuple([1, 2, 3])

# สร้างโดยไม่ต้องมีวงเล็บ
coords = 10, 20, 30

# --- Tuple Operations ---
point = (3, 4, 5)

# Indexing และ Slicing (เหมือน List)
print(point[0])            # 3
print(point[-1])           # 5
print(point[1:])           # (4, 5)

# Methods
print(point.index(4))      # 1
print(point.count(3))      # 1
print(len(point))          # 3

# Unpacking
x, y, z = point
print(f"x={x}, y={y}, z={z}")

# --- ข้อดีของ Tuple ---
# 1. เร็วกว่า List
# 2. ใช้เป็น key ของ Dictionary ได้
# 3. ปลอดภัยกว่า (ไม่ถูกเปลี่ยนแปลงโดยบังเอิญ)

# Named Tuple (สร้าง tuple ที่มีชื่อ field)
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")
print(f"Distance: {(p.x**2 + p.y**2)**0.5}")

Person = namedtuple('Person', 'name age city')
person = Person("John", 30, "Bangkok")
print(f"{person.name} is {person.age} years old")

# =============================================================================
# 3.3 Set (เซต)
# =============================================================================

# Set เก็บค่าที่ไม่ซ้ำกัน, ไม่มีลำดับ

# --- การสร้าง Set ---
empty_set = set()          # ไม่ใช่ {} (นั่นคือ dict)
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
from_string = set("hello")  # {'h', 'e', 'l', 'o'}

# --- Set Methods ---
fruits = {"apple", "banana", "cherry"}

# เพิ่มข้อมูล
fruits.add("date")
fruits.update(["elderberry", "fig"])  # เพิ่มหลายตัว

# ลบข้อมูล
fruits.remove("banana")    # ถ้าไม่มีจะ error
fruits.discard("grape")    # ถ้าไม่มีจะไม่ error
popped = fruits.pop()      # ลบและ return ตัวใดตัวหนึ่ง
# fruits.clear()           # ลบทั้งหมด

# ตรวจสอบสมาชิก
print("apple" in fruits)   # True/False

# --- Set Operations (ตัวดำเนินการเซต) ---
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (รวม)
print(A | B)               # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))

# Intersection (ร่วม)
print(A & B)               # {4, 5}
print(A.intersection(B))

# Difference (ต่าง)
print(A - B)               # {1, 2, 3}
print(A.difference(B))

# Symmetric Difference (ต่างแบบสมมาตร)
print(A ^ B)               # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))

# Subset และ Superset
C = {1, 2, 3}
print(C <= A)              # True (C เป็น subset ของ A)
print(C.issubset(A))
print(A >= C)              # True (A เป็น superset ของ C)
print(A.issuperset(C))

# Disjoint (ไม่มีสมาชิกร่วม)
D = {10, 11, 12}
print(A.isdisjoint(D))     # True

# --- Frozen Set (set ที่เปลี่ยนแปลงไม่ได้) ---
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # Error!

# =============================================================================
# 3.4 Dictionary (พจนานุกรม)
# =============================================================================

# Dict เก็บข้อมูลแบบ key-value pairs

# --- การสร้าง Dictionary ---
empty_dict = {}
person = {"name": "John", "age": 30, "city": "Bangkok"}
from_tuples = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=25)
from_keys = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# --- Accessing Values ---
print(person["name"])      # John
print(person.get("name"))  # John
print(person.get("salary", 0))  # 0 (default value ถ้า key ไม่มี)

# --- Modifying Dictionary ---
person["age"] = 31         # อัพเดทค่า
person["email"] = "john@email.com"  # เพิ่ม key ใหม่
person.update({"phone": "0891234567", "age": 32})  # อัพเดทหลาย key

# --- Removing ---
del person["email"]        # ลบ key
age = person.pop("age")    # ลบและ return value
last = person.popitem()    # ลบและ return (key, value) ตัวล่าสุด
# person.clear()           # ลบทั้งหมด

# --- Dictionary Methods ---
person = {"name": "John", "age": 30, "city": "Bangkok"}

print(person.keys())       # dict_keys(['name', 'age', 'city'])
print(person.values())     # dict_values(['John', 30, 'Bangkok'])
print(person.items())      # dict_items([('name', 'John'), ...])

# ตรวจสอบ key
print("name" in person)    # True
print("salary" in person)  # False

# คัดลอก
copy = person.copy()       # shallow copy

# setdefault
person.setdefault("country", "Thailand")  # เพิ่มถ้าไม่มี

# --- Nested Dictionary ---
students = {
    "student1": {
        "name": "Alice",
        "grades": {"math": 90, "english": 85}
    },
    "student2": {
        "name": "Bob",
        "grades": {"math": 80, "english": 92}
    }
}

print(students["student1"]["grades"]["math"])  # 90

# --- Dictionary Comprehension ---
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- Merging Dictionaries (Python 3.9+) ---
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2     # {'a': 1, 'b': 3, 'c': 4}
dict1 |= dict2             # in-place merge

# =============================================================================
# 3.5 Collections Module (โมดูลเพิ่มเติม)
# =============================================================================

from collections import Counter, defaultdict, OrderedDict, deque

# --- Counter ---
# นับจำนวนแต่ละ element
text = "abracadabra"
counter = Counter(text)
print(counter)             # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(counter.most_common(2))  # [('a', 5), ('b', 2)]

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(word_count)          # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# --- defaultdict ---
# Dictionary ที่มี default value
from collections import defaultdict

# default = list
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")
print(dict(dd))  # {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}

# default = int (0)
dd_int = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    dd_int[word] += 1
print(dict(dd_int))  # {'apple': 2, 'banana': 1}

# --- deque (Double-Ended Queue) ---
dq = deque([1, 2, 3])

dq.append(4)           # เพิ่มขวา [1, 2, 3, 4]
dq.appendleft(0)       # เพิ่มซ้าย [0, 1, 2, 3, 4]
dq.pop()               # ลบขวา [0, 1, 2, 3]
dq.popleft()           # ลบซ้าย [1, 2, 3]
dq.rotate(1)           # หมุนขวา [3, 1, 2]
dq.rotate(-1)          # หมุนซ้าย [1, 2, 3]

# ใช้เป็น fixed-size queue
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
    print(list(recent))  # จะเก็บแค่ 3 ตัวล่าสุด

# =============================================================================
# 3.6 String Operations (เพิ่มเติม)
# =============================================================================

text = "  Hello, Python World!  "

# --- Trimming ---
print(text.strip())        # ลบ whitespace ทั้งสองฝั่ง
print(text.lstrip())       # ลบ whitespace ซ้าย
print(text.rstrip())       # ลบ whitespace ขวา

# --- Case ---
text = "Hello, World!"
print(text.upper())        # HELLO, WORLD!
print(text.lower())        # hello, world!
print(text.capitalize())   # Hello, world!
print(text.title())        # Hello, World!
print(text.swapcase())     # hELLO, wORLD!

# --- Checking ---
print("hello".isalpha())   # True (ตัวอักษรทั้งหมด)
print("12345".isdigit())   # True (ตัวเลขทั้งหมด)
print("hello123".isalnum())# True (ตัวอักษรหรือตัวเลข)
print("   ".isspace())     # True (whitespace ทั้งหมด)
print("Hello".isupper())   # False
print("hello".islower())   # True

# --- Finding and Replacing ---
text = "Hello, World! Hello!"
print(text.find("Hello"))      # 0 (ตำแหน่งแรก)
print(text.rfind("Hello"))     # 14 (ตำแหน่งสุดท้าย)
print(text.find("xyz"))        # -1 (ไม่เจอ)
print(text.count("Hello"))     # 2
print(text.replace("Hello", "Hi"))  # Hi, World! Hi!

# --- Splitting and Joining ---
text = "apple,banana,cherry"
fruits = text.split(",")       # ['apple', 'banana', 'cherry']
joined = "-".join(fruits)      # apple-banana-cherry
print(fruits)
print(joined)

lines = "line1\nline2\nline3"
print(lines.splitlines())      # ['line1', 'line2', 'line3']

# --- Justifying ---
text = "Python"
print(text.ljust(10, '-'))     # Python----
print(text.rjust(10, '-'))     # ----Python
print(text.center(10, '-'))    # --Python--
print(text.zfill(10))          # 0000Python

# --- Checking Start/End ---
filename = "document.pdf"
print(filename.startswith("doc"))  # True
print(filename.endswith(".pdf"))   # True
print(filename.endswith((".pdf", ".doc")))  # True (หลายค่า)

# =============================================================================
# 3.7 ตัวอย่างโปรแกรม
# =============================================================================

def word_frequency():
    """นับความถี่คำ"""
    print("\n=== Word Frequency ===")
    text = "the quick brown fox jumps over the lazy dog the fox"
    words = text.lower().split()
    
    # วิธีที่ 1: ใช้ dict
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    # วิธีที่ 2: ใช้ Counter
    freq2 = Counter(words)
    
    print(f"Word frequency: {dict(freq)}")
    print(f"Most common: {freq2.most_common(3)}")

def remove_duplicates():
    """ลบค่าซ้ำจาก list"""
    print("\n=== Remove Duplicates ===")
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    
    # วิธีที่ 1: ใช้ set (ไม่รักษาลำดับ)
    unique1 = list(set(numbers))
    
    # วิธีที่ 2: ใช้ dict (รักษาลำดับ - Python 3.7+)
    unique2 = list(dict.fromkeys(numbers))
    
    print(f"Original: {numbers}")
    print(f"Unique (set): {unique1}")
    print(f"Unique (ordered): {unique2}")

def student_grades():
    """จัดการเกรดนักเรียน"""
    print("\n=== Student Grades ===")
    
    students = {
        "Alice": [90, 85, 92, 88],
        "Bob": [75, 80, 78, 82],
        "Charlie": [95, 92, 98, 96]
    }
    
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "F"
        print(f"{name}: Average = {avg:.2f}, Grade = {grade}")

def shopping_cart():
    """ตะกร้าสินค้า"""
    print("\n=== Shopping Cart ===")
    
    cart = []
    products = {
        "apple": 30,
        "banana": 20,
        "orange": 25
    }
    
    # เพิ่มสินค้า
    cart.append({"item": "apple", "qty": 3})
    cart.append({"item": "banana", "qty": 5})
    cart.append({"item": "orange", "qty": 2})
    
    # คำนวณราคา
    total = 0
    for item in cart:
        price = products[item["item"]] * item["qty"]
        total += price
        print(f"{item['item']}: {item['qty']} x {products[item['item']]} = {price} บาท")
    
    print(f"รวมทั้งหมด: {total} บาท")

# เรียกใช้งาน
if __name__ == "__main__":
    word_frequency()
    remove_duplicates()
    student_grades()
    shopping_cart()
    
    print("\n" + "="*50)
    print("📘 บทที่ 3: Data Structures - เสร็จสมบูรณ์!")
    print("="*50)
