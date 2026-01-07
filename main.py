"""
=============================================================================
[PYTHON] Python Summary Project - Summary of all Python content in detail
=============================================================================

This project contains all Python content in 8 chapters:

[Ch.1] Python Basics (01_basics.py)
   - Variables, Data Types, Operators, Input/Output

[Ch.2] Control Flow (02_control_flow.py)
   - Conditionals, Loops, Match-Case, Comprehensions

[Ch.3] Data Structures (03_data_structures.py)
   - List, Tuple, Set, Dictionary, Collections

[Ch.4] Functions (04_functions.py)
   - Parameters, Lambda, Decorators, Generators

[Ch.5] OOP (05_oop.py)
   - Classes, Inheritance, Polymorphism, Encapsulation

[Ch.6] File I/O & Exceptions (06_files_exceptions.py)
   - Files, JSON/CSV, Exception Handling, Context Managers

[Ch.7] Modules & Packages (07_modules.py)
   - Modules, Packages, Standard Library, Virtual Environments

[Ch.8] Advanced Python (08_advanced.py)
   - Type Hints, Async/Await, Testing, Best Practices

=============================================================================
Usage: Run python main.py or run each file separately
=============================================================================
"""

import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import os
import sys
import importlib

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

def print_header(title: str):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def run_chapter(chapter_name: str, module_name: str):
    """Run a specific chapter's main code"""
    print_header(f"[CHAPTER] {chapter_name}")
    try:
        module = importlib.import_module(module_name)
        print(f"[OK] Module {module_name} loaded successfully")
    except ImportError as e:
        print(f"[X] Error loading {module_name}: {e}")

def show_menu():
    """Show interactive menu"""
    chapters = [
        ("1", "Chapter 1: Python Basics", "01_basics"),
        ("2", "Chapter 2: Control Flow", "02_control_flow"),
        ("3", "Chapter 3: Data Structures", "03_data_structures"),
        ("4", "Chapter 4: Functions", "04_functions"),
        ("5", "Chapter 5: OOP", "05_oop"),
        ("6", "Chapter 6: File I/O & Exceptions", "06_files_exceptions"),
        ("7", "Chapter 7: Modules & Packages", "07_modules"),
        ("8", "Chapter 8: Advanced Python", "08_advanced"),
        ("a", "Run all chapters", "all"),
        ("q", "Quit", "quit"),
    ]
    
    print("\n" + "="*60)
    print("  [PYTHON] Python Summary - Main Menu")
    print("="*60)
    
    for key, name, _ in chapters:
        print(f"  [{key}] {name}")
    
    print("-"*60)
    
    choice = input("\nSelect chapter (1-8, a=all, q=quit): ").strip().lower()
    
    if choice == 'q':
        return None
    elif choice == 'a':
        for key, name, module in chapters[:-2]:  # ไม่รวม 'all' และ 'quit'
            run_chapter(name, module)
        return True
    else:
        for key, name, module in chapters:
            if key == choice:
                run_chapter(name, module)
                return True
    
    print("[X] Invalid choice. Please try again.")
    return True

def quick_demo():
    """Quick demonstration of Python concepts"""
    print_header("[>>>] Quick Python Demo")
    
    # 1. Variables and Types
    print("\n[1] Variables & Types:")
    name = "Python"
    version = 3.12
    features = ["easy", "powerful", "versatile"]
    print(f"   {name} {version} is {', '.join(features)}")
    
    # 2. Control Flow
    print("\n[2] Control Flow:")
    for i in range(1, 4):
        status = "[v]" if i % 2 == 0 else "[ ]"
        print(f"   {status} Item {i}")
    
    # 3. Functions
    print("\n[3] Functions:")
    square = lambda x: x ** 2
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(square, numbers))
    print(f"   Squares of {numbers} = {squares}")
    
    # 4. List Comprehension
    print("\n[4] List Comprehension:")
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"   Even numbers: {evens}")
    
    # 5. Dictionary
    print("\n[5] Dictionary:")
    student = {"name": "Alice", "score": 95, "grade": "A"}
    for key, value in student.items():
        print(f"   {key}: {value}")
    
    # 6. Classes
    print("\n[6] Classes:")
    class Counter:
        def __init__(self):
            self.count = 0
        def increment(self):
            self.count += 1
            return self.count
    
    counter = Counter()
    for _ in range(3):
        print(f"   Count: {counter.increment()}")
    
    # 7. Exception Handling
    print("\n[7] Exception Handling:")
    try:
        result = 10 / 2
        print(f"   10 / 2 = {result}")
    except ZeroDivisionError:
        print("   Cannot divide by zero!")
    
    # 8. Generators
    print("\n[8] Generators:")
    def fib_gen(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    fib_list = list(fib_gen(10))
    print(f"   Fibonacci: {fib_list}")

def main():
    """Main entry point"""
    print(__doc__)
    
    # Show quick demo
    quick_demo()
    
    # Interactive menu (optional)
    print("\n" + "-"*60)
    run_menu = input("Show chapter menu? (y/n): ").strip().lower()
    
    if run_menu == 'y':
        while True:
            result = show_menu()
            if result is None:
                break
    
    print("\n" + "="*60)
    print("  Thank you for using Python Summary!")
    print("  Learn more at: https://docs.python.org/")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
