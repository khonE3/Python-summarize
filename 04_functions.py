"""
=============================================================================
📘 บทที่ 4: Functions (ฟังก์ชัน)
=============================================================================
เนื้อหา: Functions, Parameters, Arguments, Lambda, Decorators, Generators
=============================================================================
"""

# =============================================================================
# 4.1 Basic Functions (ฟังก์ชันพื้นฐาน)
# =============================================================================

# --- การสร้าง Function ---
def greet():
    """ฟังก์ชันง่ายๆ ไม่มี parameter"""
    print("สวัสดี!")

greet()  # เรียกใช้ function

# Function with parameters
def greet_person(name):
    """ฟังก์ชันที่รับ parameter"""
    print(f"สวัสดี {name}!")

greet_person("John")

# Function with return value
def add(a, b):
    """ฟังก์ชันที่ return ค่า"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# Multiple return values
def calculate(a, b):
    """Return หลายค่า (เป็น tuple)"""
    sum_val = a + b
    diff = a - b
    product = a * b
    quotient = a / b if b != 0 else None
    return sum_val, diff, product, quotient

s, d, p, q = calculate(10, 3)
print(f"Sum: {s}, Diff: {d}, Product: {p}, Quotient: {q}")

# =============================================================================
# 4.2 Function Parameters (พารามิเตอร์)
# =============================================================================

# --- Default Parameters ---
def greet_with_default(name, greeting="สวัสดี"):
    """Parameter ที่มีค่า default"""
    print(f"{greeting} {name}!")

greet_with_default("Alice")              # สวัสดี Alice!
greet_with_default("Bob", "Hello")       # Hello Bob!

# --- Keyword Arguments ---
def describe_person(name, age, city):
    """ใช้ keyword arguments"""
    print(f"{name} อายุ {age} ปี อาศัยอยู่ที่ {city}")

describe_person("Alice", 25, "Bangkok")                    # positional
describe_person(name="Bob", age=30, city="Chiang Mai")     # keyword
describe_person(age=35, name="Charlie", city="Phuket")     # ลำดับไม่สำคัญ

# --- *args (Variable Positional Arguments) ---
def sum_all(*args):
    """รับ arguments จำนวนไม่จำกัด"""
    print(f"Args: {args}")  # เป็น tuple
    return sum(args)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# --- **kwargs (Variable Keyword Arguments) ---
def print_info(**kwargs):
    """รับ keyword arguments จำนวนไม่จำกัด"""
    print(f"Kwargs: {kwargs}")  # เป็น dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25, city="Bangkok")

# --- รวม *args และ **kwargs ---
def mixed_function(a, b, *args, **kwargs):
    """รวมทุกแบบ"""
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

mixed_function(1, 2, 3, 4, 5, x=10, y=20)

# --- Keyword-only Arguments ---
def greet_formal(name, *, greeting="Hello", punctuation="!"):
    """Arguments หลัง * ต้องเป็น keyword เท่านั้น"""
    print(f"{greeting} {name}{punctuation}")

greet_formal("John", greeting="Hi", punctuation=".")

# --- Positional-only Arguments (Python 3.8+) ---
def power(base, exp, /):
    """Arguments ก่อน / ต้องเป็น positional เท่านั้น"""
    return base ** exp

print(power(2, 3))  # 8
# print(power(base=2, exp=3))  # Error!

# --- รวม Positional-only และ Keyword-only ---
def hybrid(a, b, /, c, d, *, e, f):
    """
    a, b: positional-only
    c, d: positional or keyword
    e, f: keyword-only
    """
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

hybrid(1, 2, 3, d=4, e=5, f=6)

# =============================================================================
# 4.3 Scope และ Lifetime
# =============================================================================

# --- Local vs Global ---
global_var = "I am global"

def test_scope():
    local_var = "I am local"
    print(global_var)   # อ่าน global ได้
    print(local_var)    # อ่าน local ได้

test_scope()
# print(local_var)  # Error! ไม่สามารถเข้าถึง local จากนอก function

# --- global keyword ---
counter = 0

def increment():
    global counter  # ประกาศว่าจะใช้ตัวแปร global
    counter += 1

increment()
increment()
print(f"Counter: {counter}")  # 2

# --- nonlocal keyword (nested function) ---
def outer():
    count = 0
    
    def inner():
        nonlocal count  # ใช้ตัวแปรจาก enclosing function
        count += 1
        return count
    
    return inner

counter_func = outer()
print(counter_func())  # 1
print(counter_func())  # 2
print(counter_func())  # 3

# =============================================================================
# 4.4 Lambda Functions (Anonymous Functions)
# =============================================================================

# Lambda = ฟังก์ชันไม่มีชื่อ, เขียนบรรทัดเดียว

# --- Basic Lambda ---
add = lambda x, y: x + y
print(add(3, 5))  # 8

square = lambda x: x ** 2
print(square(4))  # 16

# --- Lambda with built-in functions ---

# sort with key
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students.sort(key=lambda x: x[1])  # sort by score
print(students)

students.sort(key=lambda x: x[1], reverse=True)  # high to low
print(students)

# map - apply function to each element
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"Squares: {squares}")

# filter - keep elements that pass condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# reduce - combine elements
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")  # 1*2*3*4*5 = 120

# --- เปรียบเทียบ Lambda vs Regular Function ---
# Lambda
double_lambda = lambda x: x * 2

# Regular
def double_regular(x):
    return x * 2

# ผลลัพธ์เหมือนกัน
print(double_lambda(5))   # 10
print(double_regular(5))  # 10

# =============================================================================
# 4.5 Decorators (ตกแต่งฟังก์ชัน)
# =============================================================================

# Decorator = ฟังก์ชันที่รับฟังก์ชันอื่นเป็น input และ return ฟังก์ชันใหม่

# --- Basic Decorator ---
def uppercase_decorator(func):
    """Decorator ที่แปลงผลลัพธ์เป็นตัวพิมพ์ใหญ่"""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello world"

print(say_hello())  # HELLO WORLD

# --- Decorator with Arguments ---
def repeat(times):
    """Decorator factory ที่รับ argument"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet_repeat(name):
    print(f"Hello, {name}!")

greet_repeat("Alice")  # พิมพ์ 3 ครั้ง

# --- Practical Decorators ---

import time

# 1. Timer decorator
def timer(func):
    """วัดเวลาการทำงานของ function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# 2. Debug decorator
def debug(func):
    """แสดง input และ output ของ function"""
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def multiply(x, y):
    return x * y

multiply(3, 4)

# 3. Memoization decorator (caching)
def memoize(func):
    """Cache ผลลัพธ์เพื่อไม่ต้องคำนวณซ้ำ"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(30): {fibonacci(30)}")  # เร็วมากเพราะ cache

# --- Using functools.wraps ---
from functools import wraps

def better_decorator(func):
    @wraps(func)  # รักษา metadata ของ function เดิม
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def my_function():
    """This is my docstring"""
    pass

print(my_function.__name__)  # my_function (ไม่ใช่ wrapper)
print(my_function.__doc__)   # This is my docstring

# =============================================================================
# 4.6 Generators (ตัวสร้างค่า)
# =============================================================================

# Generator = ฟังก์ชันที่ yield ค่าทีละตัว (ประหยัด memory)

# --- Basic Generator ---
def count_up_to(n):
    """Generator ที่นับจาก 1 ถึง n"""
    i = 1
    while i <= n:
        yield i  # ใช้ yield แทน return
        i += 1

# การใช้งาน
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# ใช้ใน for loop
for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5
print()

# --- Generator Expression ---
# คล้าย list comprehension แต่ใช้ ()
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ประหยัด memory มากกว่า list
sum_squares = sum(x**2 for x in range(1000000))  # ไม่สร้าง list ทั้งหมด

# --- Infinite Generator ---
def infinite_sequence():
    """Generator ที่ไม่มีวันจบ"""
    i = 0
    while True:
        yield i
        i += 1

gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# ใช้กับ itertools
from itertools import islice
first_10 = list(islice(infinite_sequence(), 10))
print(first_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Generator with send() ---
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)  # เริ่ม generator
gen.send("Hello")   # Received: Hello
gen.send("World")   # Received: World

# --- yield from ---
def chain_generators(*iterables):
    for iterable in iterables:
        yield from iterable  # delegate to sub-generator

result = list(chain_generators([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]

# =============================================================================
# 4.7 Higher-Order Functions
# =============================================================================

# Higher-order function = ฟังก์ชันที่รับหรือ return ฟังก์ชัน

# --- Function as Parameter ---
def apply_operation(x, y, operation):
    """รับ function เป็น parameter"""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))       # 8
print(apply_operation(5, 3, multiply))  # 15

# --- Function as Return Value ---
def make_multiplier(n):
    """Return function ที่คูณด้วย n"""
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# --- Closures ---
def make_counter():
    """Closure ที่เก็บ state"""
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3

# =============================================================================
# 4.8 Built-in Functions
# =============================================================================

# --- Math functions ---
print(abs(-5))           # 5 (ค่าสัมบูรณ์)
print(round(3.7))        # 4 (ปัดเศษ)
print(round(3.14159, 2)) # 3.14 (2 ทศนิยม)
print(pow(2, 3))         # 8 (ยกกำลัง)
print(pow(2, 3, 5))      # 3 (2^3 % 5)
print(divmod(17, 5))     # (3, 2) (ผลหารและเศษ)

# --- Sequence functions ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers))      # 8
print(min(numbers))      # 1
print(max(numbers))      # 9
print(sum(numbers))      # 31
print(sorted(numbers))   # [1, 1, 2, 3, 4, 5, 6, 9]
print(reversed(numbers)) # iterator

# --- Type functions ---
print(type(42))          # <class 'int'>
print(isinstance(42, int))  # True
print(callable(print))   # True

# --- Iterator functions ---
print(list(range(5)))    # [0, 1, 2, 3, 4]
print(list(zip([1,2], [3,4])))  # [(1, 3), (2, 4)]
print(list(enumerate(['a','b'])))  # [(0, 'a'), (1, 'b')]
print(any([False, False, True]))  # True
print(all([True, True, True]))    # True

# =============================================================================
# 4.9 ตัวอย่างโปรแกรม
# =============================================================================

def factorial_recursive(n):
    """Factorial แบบ recursive"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Factorial แบบ iterative"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@memoize
def fibonacci_memoized(n):
    """Fibonacci with memoization"""
    if n < 2:
        return n
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

def prime_generator(limit):
    """Generator ที่สร้างจำนวนเฉพาะ"""
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# เรียกใช้งาน
if __name__ == "__main__":
    print("\n=== Factorial ===")
    print(f"5! = {factorial_recursive(5)}")
    print(f"10! = {factorial_iterative(10)}")
    
    print("\n=== Fibonacci ===")
    fib_list = [fibonacci_memoized(i) for i in range(15)]
    print(f"First 15 Fibonacci: {fib_list}")
    
    print("\n=== Prime Generator ===")
    primes = list(prime_generator(50))
    print(f"Primes up to 50: {primes}")
    
    print("\n" + "="*50)
    print("📘 บทที่ 4: Functions - เสร็จสมบูรณ์!")
    print("="*50)
