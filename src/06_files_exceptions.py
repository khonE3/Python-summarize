"""
=============================================================================
📘 บทที่ 6: File I/O และ Exception Handling
=============================================================================
เนื้อหา: Files, Exceptions, Context Managers
=============================================================================
"""

import os
import json
import csv
import pickle

# =============================================================================
# 6.1 File Operations (การจัดการไฟล์)
# =============================================================================

# --- เปิดและอ่านไฟล์ ---

# Mode options:
# 'r'  - Read (default)
# 'w'  - Write (สร้างใหม่หรือเขียนทับ)
# 'a'  - Append (เพิ่มต่อท้าย)
# 'x'  - Create (error ถ้ามีไฟล์อยู่แล้ว)
# 'r+' - Read and Write
# 'b'  - Binary mode
# 't'  - Text mode (default)

# Basic file reading
def read_file_example():
    """ตัวอย่างการอ่านไฟล์"""
    
    # วิธีที่ 1: อ่านทั้งหมด
    # with open('file.txt', 'r', encoding='utf-8') as f:
    #     content = f.read()
    #     print(content)
    
    # วิธีที่ 2: อ่านทีละบรรทัด
    # with open('file.txt', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line.strip())
    
    # วิธีที่ 3: อ่านทั้งหมดเป็น list
    # with open('file.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    
    # วิธีที่ 4: อ่านบรรทัดเดียว
    # with open('file.txt', 'r', encoding='utf-8') as f:
    #     first_line = f.readline()
    pass

# Basic file writing
def write_file_example():
    """ตัวอย่างการเขียนไฟล์"""
    
    # เขียนไฟล์ใหม่
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write("Hello, World!\n")
        f.write("สวัสดีครับ\n")
    
    # เขียนหลายบรรทัด
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    # เพิ่มต่อท้าย
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write("Appended line\n")

# --- File Methods ---
def file_methods_example():
    """Methods ต่างๆ ของ file object"""
    
    # f.read(size)    - อ่าน size characters/bytes
    # f.readline()    - อ่านบรรทัดเดียว
    # f.readlines()   - อ่านทั้งหมดเป็น list
    # f.write(str)    - เขียน string
    # f.writelines(list) - เขียน list ของ strings
    # f.tell()        - ตำแหน่งปัจจุบัน
    # f.seek(offset)  - ย้ายไปตำแหน่งที่ต้องการ
    # f.close()       - ปิดไฟล์
    # f.closed        - True ถ้าปิดแล้ว
    pass

# =============================================================================
# 6.2 Working with Different File Types
# =============================================================================

# --- JSON Files ---
def json_example():
    """ตัวอย่างการทำงานกับ JSON"""
    
    data = {
        "name": "John",
        "age": 30,
        "city": "Bangkok",
        "skills": ["Python", "JavaScript", "SQL"]
    }
    
    # เขียน JSON
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # อ่าน JSON
    with open('data.json', 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(f"Loaded: {loaded_data}")
    
    # String to JSON และ JSON to String
    json_string = json.dumps(data, ensure_ascii=False)
    parsed = json.loads(json_string)
    
    return loaded_data

# --- CSV Files ---
def csv_example():
    """ตัวอย่างการทำงานกับ CSV"""
    
    # เขียน CSV
    data = [
        ["Name", "Age", "City"],
        ["Alice", 25, "Bangkok"],
        ["Bob", 30, "Chiang Mai"],
        ["Charlie", 35, "Phuket"]
    ]
    
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    # อ่าน CSV
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
    # ใช้ DictWriter/DictReader
    data_dict = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    
    with open('data_dict.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["name", "age"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_dict)
    
    with open('data_dict.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(dict(row))

# --- Binary Files (Pickle) ---
def pickle_example():
    """ตัวอย่างการทำงานกับ Pickle (binary serialization)"""
    
    data = {
        "numbers": [1, 2, 3, 4, 5],
        "nested": {"a": 1, "b": 2}
    }
    
    # เขียน pickle
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)
    
    # อ่าน pickle
    with open('data.pkl', 'rb') as f:
        loaded = pickle.load(f)
    
    print(f"Pickle loaded: {loaded}")

# =============================================================================
# 6.3 OS และ Path Operations
# =============================================================================

def os_operations():
    """ตัวอย่างการใช้ os module"""
    
    # Current directory
    print(f"Current dir: {os.getcwd()}")
    
    # List files
    print(f"Files: {os.listdir('.')}")
    
    # Check existence
    print(f"file.txt exists: {os.path.exists('file.txt')}")
    print(f"Is file: {os.path.isfile('file.txt')}")
    print(f"Is dir: {os.path.isdir('.')}")
    
    # Path operations
    path = os.path.join('folder', 'subfolder', 'file.txt')
    print(f"Joined path: {path}")
    print(f"Dirname: {os.path.dirname(path)}")
    print(f"Basename: {os.path.basename(path)}")
    print(f"Split: {os.path.split(path)}")
    print(f"Splitext: {os.path.splitext('file.txt')}")
    
    # Create directory
    # os.mkdir('new_folder')          # สร้าง folder เดียว
    # os.makedirs('a/b/c')            # สร้าง nested folders
    # os.makedirs('a/b/c', exist_ok=True)  # ไม่ error ถ้ามีอยู่แล้ว
    
    # Remove
    # os.remove('file.txt')           # ลบไฟล์
    # os.rmdir('folder')              # ลบ folder ว่าง
    # shutil.rmtree('folder')         # ลบ folder และเนื้อหา
    
    # Rename/Move
    # os.rename('old.txt', 'new.txt')

# --- pathlib (Modern approach) ---
from pathlib import Path

def pathlib_example():
    """ตัวอย่างการใช้ pathlib (Python 3.4+)"""
    
    # Create path
    p = Path('.')
    
    # List files
    for item in p.iterdir():
        print(item)
    
    # Glob pattern
    # for py_file in p.glob('**/*.py'):
    #     print(py_file)
    
    # Path operations
    path = Path('folder') / 'subfolder' / 'file.txt'
    print(f"Path: {path}")
    print(f"Parent: {path.parent}")
    print(f"Name: {path.name}")
    print(f"Stem: {path.stem}")
    print(f"Suffix: {path.suffix}")
    
    # Check existence
    # path.exists()
    # path.is_file()
    # path.is_dir()
    
    # Read/Write
    # content = path.read_text(encoding='utf-8')
    # path.write_text('content', encoding='utf-8')
    
    # Create
    # path.mkdir(parents=True, exist_ok=True)

# =============================================================================
# 6.4 Exception Handling (การจัดการข้อผิดพลาด)
# =============================================================================

# --- Basic try-except ---
def basic_exception():
    """ตัวอย่าง Exception พื้นฐาน"""
    
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
    # Multiple exceptions
    try:
        value = int("abc")
    except ValueError:
        print("Invalid value")
    except TypeError:
        print("Type error")
    
    # Catch multiple exceptions
    try:
        value = int("abc")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    
    # Catch all exceptions
    try:
        result = 10 / 0
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

# --- try-except-else-finally ---
def complete_exception():
    """ตัวอย่าง try-except-else-finally"""
    
    try:
        file = open('test.txt', 'r')
        content = file.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        # ทำงานถ้าไม่มี exception
        print(f"File content: {content}")
    finally:
        # ทำงานเสมอ ไม่ว่าจะมี exception หรือไม่
        print("Cleanup completed")
        # file.close()  # ถ้า file ถูกเปิด

# --- Raising Exceptions ---
def validate_age(age):
    """ตัวอย่างการ raise exception"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# --- Re-raising Exceptions ---
def process_data():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Logging error...")
        raise  # Re-raise the same exception

# --- Custom Exceptions ---
class ValidationError(Exception):
    """Custom exception สำหรับ validation"""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """Custom exception สำหรับเงินไม่พอ"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        message = f"Cannot withdraw {amount}. Balance: {balance}, Deficit: {self.deficit}"
        super().__init__(message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"Need {e.deficit} more")

# --- Exception Chaining ---
def process():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("Processing failed") from e

# try:
#     process()
# except RuntimeError as e:
#     print(f"Error: {e}")
#     print(f"Original: {e.__cause__}")

# =============================================================================
# 6.5 Context Managers
# =============================================================================

# --- Using with statement ---
def with_example():
    """ตัวอย่างการใช้ with statement"""
    
    # File context manager
    with open('test.txt', 'w') as f:
        f.write("Hello")
    # file จะถูกปิดอัตโนมัติ
    
    # Multiple context managers
    # with open('input.txt') as fin, open('output.txt', 'w') as fout:
    #     content = fin.read()
    #     fout.write(content.upper())

# --- Creating Custom Context Manager ---

# วิธีที่ 1: ใช้ class
class Timer:
    """Context manager สำหรับวัดเวลา"""
    
    def __init__(self, name="Timer"):
        self.name = name
    
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"{self.name}: {self.end - self.start:.4f} seconds")
        return False  # ไม่ suppress exception

# ใช้งาน
# with Timer("My operation"):
#     time.sleep(0.5)

# วิธีที่ 2: ใช้ contextlib
from contextlib import contextmanager

@contextmanager
def timer(name="Timer"):
    """Context manager ด้วย decorator"""
    import time
    start = time.time()
    try:
        yield  # ตรงนี้คือจุดที่ with block ทำงาน
    finally:
        end = time.time()
        print(f"{name}: {end - start:.4f} seconds")

# ใช้งาน
# with timer("Function"):
#     time.sleep(0.5)

# --- Suppress exceptions ---
from contextlib import suppress

# แทนที่จะเขียน try-except ที่ไม่ทำอะไร
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')

# =============================================================================
# 6.6 Common Exception Types
# =============================================================================

"""
Built-in Exceptions:
- BaseException
  - Exception
    - ArithmeticError
      - ZeroDivisionError
      - FloatingPointError
      - OverflowError
    - AssertionError
    - AttributeError
    - EOFError
    - ImportError
      - ModuleNotFoundError
    - LookupError
      - IndexError
      - KeyError
    - NameError
    - OSError
      - FileNotFoundError
      - FileExistsError
      - PermissionError
    - RuntimeError
      - RecursionError
    - StopIteration
    - SyntaxError
      - IndentationError
    - TypeError
    - ValueError
  - GeneratorExit
  - KeyboardInterrupt
  - SystemExit
"""

def exception_examples():
    """ตัวอย่าง Exceptions ที่พบบ่อย"""
    
    examples = [
        # ZeroDivisionError
        ("1 / 0", "ZeroDivisionError"),
        # TypeError
        ("'hello' + 5", "TypeError"),
        # ValueError
        ("int('abc')", "ValueError"),
        # IndexError
        ("[1, 2, 3][10]", "IndexError"),
        # KeyError
        ("{'a': 1}['b']", "KeyError"),
        # AttributeError
        ("'hello'.foo()", "AttributeError"),
        # NameError
        ("undefined_variable", "NameError"),
    ]
    
    for code, expected_error in examples:
        try:
            eval(code)
        except Exception as e:
            print(f"{code} -> {type(e).__name__}: {e}")

# =============================================================================
# 6.7 ตัวอย่างโปรแกรม
# =============================================================================

class ConfigManager:
    """จัดการ config file"""
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}
    
    def load(self):
        """โหลด config จากไฟล์"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"Config loaded from {self.config_file}")
        except FileNotFoundError:
            print(f"Config file not found. Using defaults.")
            self.config = {"debug": False, "version": "1.0"}
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in config file: {e}")
        return self.config
    
    def save(self):
        """บันทึก config ลงไฟล์"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2)
        print(f"Config saved to {self.config_file}")
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value

class Logger:
    """Simple file logger"""
    
    def __init__(self, log_file):
        self.log_file = log_file
    
    def log(self, message, level="INFO"):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        print(log_entry.strip())
    
    def info(self, message):
        self.log(message, "INFO")
    
    def error(self, message):
        self.log(message, "ERROR")
    
    def warning(self, message):
        self.log(message, "WARNING")

# เรียกใช้งาน
if __name__ == "__main__":
    print("\n=== File I/O Examples ===")
    
    # JSON example
    print("\n--- JSON Example ---")
    json_example()
    
    # CSV example
    print("\n--- CSV Example ---")
    csv_example()
    
    # Exception examples
    print("\n--- Exception Examples ---")
    exception_examples()
    
    # Config Manager
    print("\n--- Config Manager ---")
    config = ConfigManager('config.json')
    config.load()
    config.set('debug', True)
    config.save()
    
    # Logger
    print("\n--- Logger ---")
    logger = Logger('app.log')
    logger.info("Application started")
    logger.warning("Low memory")
    logger.error("Connection failed")
    
    # Cleanup test files
    for f in ['output.txt', 'data.json', 'data.csv', 'data_dict.csv', 
              'data.pkl', 'config.json', 'app.log']:
        with suppress(FileNotFoundError):
            os.remove(f)
    
    print("\n" + "="*50)
    print("📘 บทที่ 6: File I/O & Exceptions - เสร็จสมบูรณ์!")
    print("="*50)
