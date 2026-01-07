"""
=============================================================================
📘 บทที่ 7: Modules และ Packages
=============================================================================
เนื้อหา: Modules, Packages, Standard Library, Virtual Environments
=============================================================================
"""

# =============================================================================
# 7.1 Modules (โมดูล)
# =============================================================================

# Module = ไฟล์ Python ที่มี code (.py)
# สามารถ import มาใช้งานในไฟล์อื่นได้

# --- Basic Import ---
import math
print(f"pi = {math.pi}")
print(f"sqrt(16) = {math.sqrt(16)}")

# Import specific items
from math import sqrt, pi
print(f"pi = {pi}")
print(f"sqrt(25) = {sqrt(25)}")

# Import with alias
import math as m
print(f"sin(90°) = {m.sin(m.radians(90))}")

from math import factorial as fact
print(f"5! = {fact(5)}")

# Import all (ไม่แนะนำ)
# from math import *

# --- Module Search Path ---
import sys
print("\nModule search path:")
for path in sys.path[:3]:
    print(f"  {path}")

# --- Module Attributes ---
print(f"\nModule name: {math.__name__}")
print(f"Module file: {math.__file__}")
# print(f"Module doc: {math.__doc__[:100]}...")

# =============================================================================
# 7.2 Creating Your Own Modules
# =============================================================================

# สมมติว่าเรามีไฟล์ mymodule.py:
"""
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159

class Calculator:
    def multiply(self, a, b):
        return a * b

# Code ที่ไม่ต้องการให้รันเมื่อ import
if __name__ == "__main__":
    print("This runs only when executed directly")
    print(greet("World"))
"""

# การใช้งาน:
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.add(3, 5))
# print(mymodule.PI)

# from mymodule import greet, Calculator
# print(greet("Bob"))
# calc = Calculator()

# =============================================================================
# 7.3 Packages (แพ็คเกจ)
# =============================================================================

# Package = ไดเรกทอรีที่มี __init__.py

"""
โครงสร้าง Package:

mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

# __init__.py อาจว่างเปล่าหรือมี code เช่น:
# mypackage/__init__.py
from .module1 import function1
from .module2 import function2
__all__ = ['function1', 'function2']
"""

# การ import:
# import mypackage
# from mypackage import module1
# from mypackage.module1 import function1
# from mypackage.subpackage import module3

# =============================================================================
# 7.4 Standard Library (ไลบรารีมาตรฐาน)
# =============================================================================

# --- os - ระบบปฏิบัติการ ---
import os
print("\n=== os module ===")
print(f"Current directory: {os.getcwd()}")
print(f"OS name: {os.name}")
# os.listdir(), os.path.join(), os.makedirs(), etc.

# --- sys - ระบบ Python ---
import sys
print("\n=== sys module ===")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
# sys.argv, sys.path, sys.exit(), etc.

# --- datetime - วันที่และเวลา ---
from datetime import datetime, date, time, timedelta
print("\n=== datetime module ===")
now = datetime.now()
print(f"Now: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Date: {date.today()}")
print(f"Tomorrow: {date.today() + timedelta(days=1)}")

# Parsing
parsed = datetime.strptime("2024-01-15", "%Y-%m-%d")
print(f"Parsed: {parsed}")

# --- random - ตัวเลขสุ่ม ---
import random
print("\n=== random module ===")
print(f"Random float: {random.random()}")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['a', 'b', 'c'])}")
print(f"Random sample: {random.sample(range(10), 3)}")
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(f"Shuffled: {items}")

# --- collections - โครงสร้างข้อมูลพิเศษ ---
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict
print("\n=== collections module ===")
counter = Counter("abracadabra")
print(f"Counter: {counter}")
print(f"Most common: {counter.most_common(2)}")

# --- itertools - Iterator functions ---
import itertools
print("\n=== itertools module ===")
print(f"Count: {list(itertools.islice(itertools.count(1), 5))}")
print(f"Cycle: {list(itertools.islice(itertools.cycle('AB'), 6))}")
print(f"Repeat: {list(itertools.repeat('x', 3))}")
print(f"Chain: {list(itertools.chain([1,2], [3,4]))}")
print(f"Permutations: {list(itertools.permutations('AB', 2))}")
print(f"Combinations: {list(itertools.combinations('ABC', 2))}")

# --- functools - Higher-order functions ---
from functools import reduce, partial, lru_cache
print("\n=== functools module ===")

# reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(f"Product: {product}")

# partial
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
print(f"Square of 5: {square(5)}")

# lru_cache
@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(f"Fib(30): {fib(30)}")

# --- re - Regular Expressions ---
import re
print("\n=== re module ===")
text = "Contact: john@email.com, jane@gmail.com"

# Search
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(f"Found: {match.group()}")

# Find all
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"All emails: {emails}")

# Substitute
clean = re.sub(r'\w+@\w+\.\w+', '[EMAIL]', text)
print(f"Cleaned: {clean}")

# Split
parts = re.split(r'\s*,\s*', text)
print(f"Split: {parts}")

# --- json - JSON handling ---
import json
print("\n=== json module ===")
data = {"name": "John", "age": 30}
json_str = json.dumps(data, indent=2)
print(f"JSON string: {json_str}")
parsed = json.loads(json_str)
print(f"Parsed: {parsed}")

# --- urllib - URL handling ---
from urllib.parse import urlparse, urlencode
print("\n=== urllib module ===")
url = "https://www.example.com:8080/path?query=value#section"
parsed = urlparse(url)
print(f"Scheme: {parsed.scheme}")
print(f"Host: {parsed.netloc}")
print(f"Path: {parsed.path}")
print(f"Query: {parsed.query}")

# --- hashlib - Hashing ---
import hashlib
print("\n=== hashlib module ===")
text = "Hello, World!"
md5 = hashlib.md5(text.encode()).hexdigest()
sha256 = hashlib.sha256(text.encode()).hexdigest()
print(f"MD5: {md5}")
print(f"SHA256: {sha256[:32]}...")

# --- logging - Logging ---
import logging
print("\n=== logging module ===")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")

# =============================================================================
# 7.5 Third-Party Packages
# =============================================================================

"""
การติดตั้ง packages ด้วย pip:

# ติดตั้ง
pip install package_name
pip install package_name==1.2.3  # specific version
pip install -r requirements.txt  # from file

# ดู packages ที่ติดตั้ง
pip list
pip show package_name

# อัพเดท
pip install --upgrade package_name

# ถอนการติดตั้ง
pip uninstall package_name

# สร้าง requirements.txt
pip freeze > requirements.txt
"""

# Popular packages:
# - requests: HTTP library
# - numpy: Numerical computing
# - pandas: Data analysis
# - matplotlib: Plotting
# - flask/django: Web frameworks
# - pytest: Testing
# - sqlalchemy: Database ORM

# =============================================================================
# 7.6 Virtual Environments
# =============================================================================

"""
Virtual Environment = สภาพแวดล้อม Python แยกอิสระสำหรับแต่ละโปรเจค

# สร้าง virtual environment
python -m venv myenv

# Activate (Windows)
myenv\\Scripts\\activate

# Activate (macOS/Linux)
source myenv/bin/activate

# Deactivate
deactivate

# ติดตั้ง packages ใน virtual environment
pip install package_name

# Requirements
pip freeze > requirements.txt
pip install -r requirements.txt
"""

# =============================================================================
# 7.7 __name__ และ __main__
# =============================================================================

def main():
    """ฟังก์ชันหลัก"""
    print("\nThis is the main function")

# __name__ = "__main__" เมื่อ run ไฟล์โดยตรง
# __name__ = "module_name" เมื่อถูก import
if __name__ == "__main__":
    print(f"Module name: {__name__}")
    main()

# Best practice structure:
"""
# myprogram.py

import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    
    # Main logic here
    print(f"Arguments: {args}")
    return 0  # Exit code

if __name__ == "__main__":
    sys.exit(main())
"""

# =============================================================================
# 7.8 ตัวอย่างโปรแกรม
# =============================================================================

def utility_functions():
    """รวม utility functions ที่ใช้บ่อย"""
    
    import os
    import json
    from datetime import datetime
    
    print("\n=== Utility Examples ===")
    
    # 1. Get file info
    def get_file_info(filepath):
        if os.path.exists(filepath):
            stat = os.stat(filepath)
            return {
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime),
                "is_file": os.path.isfile(filepath)
            }
        return None
    
    # 2. Pretty print JSON
    def pretty_json(data):
        return json.dumps(data, indent=2, ensure_ascii=False, default=str)
    
    # 3. Generate random string
    def random_string(length=8):
        import string
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    # 4. Timing decorator
    def timer(func):
        import time
        from functools import wraps
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end-start:.4f}s")
            return result
        return wrapper
    
    # Test
    print(f"Random string: {random_string(12)}")
    print(f"JSON: {pretty_json({'name': 'สมชาย', 'age': 25})}")

# เรียกใช้งาน
if __name__ == "__main__":
    utility_functions()
    
    print("\n" + "="*50)
    print("📘 บทที่ 7: Modules & Packages - เสร็จสมบูรณ์!")
    print("="*50)
