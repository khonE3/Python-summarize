"""
=============================================================================
📘 บทที่ 2: Control Flow (การควบคุมการทำงาน)
=============================================================================
เนื้อหา: Conditionals, Loops, Match-Case
=============================================================================
"""

# =============================================================================
# 2.1 Conditional Statements (เงื่อนไข)
# =============================================================================

# --- if Statement ---
age = 18
if age >= 18:
    print("คุณเป็นผู้ใหญ่")

# --- if-else Statement ---
age = 15
if age >= 18:
    print("คุณเป็นผู้ใหญ่")
else:
    print("คุณยังเป็นเด็ก")

# --- if-elif-else Statement ---
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"เกรดของคุณคือ: {grade}")

# --- Nested if ---
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("คุณสามารถขับรถได้")
    else:
        print("คุณต้องมีใบขับขี่")
else:
    print("คุณอายุไม่ถึงเกณฑ์")

# --- Ternary Operator (Conditional Expression) ---
age = 20
status = "ผู้ใหญ่" if age >= 18 else "เด็ก"
print(f"สถานะ: {status}")

# ซ้อนกันได้
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# --- Logical Operators in Conditions ---
age = 25
income = 50000

# and - ทั้งสองเงื่อนไขต้องเป็นจริง
if age >= 20 and income >= 30000:
    print("สามารถสมัครบัตรเครดิตได้")

# or - อย่างน้อยหนึ่งเงื่อนไขเป็นจริง
if age < 18 or age >= 60:
    print("ได้รับส่วนลดพิเศษ")

# not - กลับค่าความจริง
is_student = False
if not is_student:
    print("ราคาปกติ")

# =============================================================================
# 2.2 Loops (การวนรอบ)
# =============================================================================

# --- for Loop ---
# วนรอบ List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"ผลไม้: {fruit}")

# วนรอบ String
for char in "Python":
    print(char, end=" ")  # P y t h o n
print()

# วนรอบด้วย range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i, end=" ")
print()

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step = 2)
    print(i, end=" ")
print()

for i in range(10, 0, -2):  # 10, 8, 6, 4, 2 (นับถอยหลัง)
    print(i, end=" ")
print()

# วนรอบด้วย enumerate() - ได้ทั้ง index และ value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for index, fruit in enumerate(fruits, start=1):  # เริ่มที่ 1
    print(f"{index}: {fruit}")

# วนรอบ Dictionary
student = {"name": "John", "age": 20, "grade": "A"}

# วนรอบ keys
for key in student:
    print(key)

# วนรอบ keys และ values
for key, value in student.items():
    print(f"{key}: {value}")

# วนรอบเฉพาะ values
for value in student.values():
    print(value)

# วนรอบหลาย List พร้อมกันด้วย zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# --- while Loop ---
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# while with condition
password = ""
attempts = 0
# while password != "secret" and attempts < 3:
#     password = input("Enter password: ")
#     attempts += 1

# Infinite loop (ใช้ด้วยความระวัง!)
# while True:
#     print("This will run forever!")
#     break  # ต้องมี break เพื่อออกจาก loop

# --- Loop Control Statements ---

# break - ออกจาก loop ทันที
print("\n--- break example ---")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")  # 0 1 2 3 4
print()

# continue - ข้ามไปรอบถัดไป
print("\n--- continue example ---")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")  # 1 3 5 7 9
print()

# pass - ไม่ทำอะไร (placeholder)
print("\n--- pass example ---")
for i in range(5):
    if i == 2:
        pass  # TODO: implement later
    print(i, end=" ")  # 0 1 2 3 4
print()

# else with loops
print("\n--- for-else example ---")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed normally!")

# else ไม่ทำงานถ้า break
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("\nThis won't print")  # ไม่ print เพราะมี break
print()

# --- Nested Loops ---
print("\n--- Nested loops (สูตรคูณ) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

# Pattern printing
print("\n--- Pattern printing ---")
for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

# =============================================================================
# 2.3 Match-Case (Python 3.10+)
# =============================================================================

# Match-case คล้าย switch-case ในภาษาอื่น
def check_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # default case
            return "Unknown Status"

print(f"\nStatus 200: {check_status(200)}")
print(f"Status 404: {check_status(404)}")
print(f"Status 999: {check_status(999)}")

# Pattern matching with values
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

print(f"\n{describe_point((0, 0))}")
print(f"{describe_point((0, 5))}")
print(f"{describe_point((3, 0))}")
print(f"{describe_point((3, 4))}")

# Pattern matching with guards
def check_number(num):
    match num:
        case n if n < 0:
            return "Negative"
        case n if n == 0:
            return "Zero"
        case n if n > 0:
            return "Positive"

print(f"\n-5: {check_number(-5)}")
print(f"0: {check_number(0)}")
print(f"10: {check_number(10)}")

# Pattern matching with OR (|)
def check_day(day):
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Invalid day"

print(f"\nSunday: {check_day('Sunday')}")
print(f"Monday: {check_day('Monday')}")

# =============================================================================
# 2.4 Comprehensions (การสร้าง Collection แบบย่อ)
# =============================================================================

# --- List Comprehension ---
# แบบปกติ
squares = []
for x in range(10):
    squares.append(x ** 2)

# แบบ comprehension
squares = [x ** 2 for x in range(10)]
print(f"\nSquares: {squares}")

# with condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# with if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# flatten matrix
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# --- Dictionary Comprehension ---
squares_dict = {x: x**2 for x in range(5)}
print(f"\nSquares dict: {squares_dict}")

# swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# with condition
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even dict: {even_dict}")

# --- Set Comprehension ---
unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
print(f"\nUnique lengths: {unique_lengths}")

# --- Generator Expression ---
# ไม่สร้าง list ทั้งหมดในหน่วยความจำ
gen = (x ** 2 for x in range(10))
print(f"\nGenerator: {gen}")
print(f"Next: {next(gen)}")  # 0
print(f"Next: {next(gen)}")  # 1
print(f"Sum: {sum(x ** 2 for x in range(10))}")  # ใช้กับ function ได้เลย

# =============================================================================
# 2.5 ตัวอย่างโปรแกรม
# =============================================================================

def guess_number_game():
    """เกมทายตัวเลข"""
    import random
    
    print("\n=== เกมทายตัวเลข ===")
    secret = random.randint(1, 10)
    guesses = [3, 7, 5, 8]  # จำลองการทาย (ในจริงใช้ input)
    
    for i, guess in enumerate(guesses, 1):
        print(f"ครั้งที่ {i}: ทาย {guess}")
        if guess == secret:
            print(f"ถูกต้อง! ตัวเลขคือ {secret}")
            break
        elif guess < secret:
            print("น้อยไป!")
        else:
            print("มากไป!")
    else:
        print(f"หมดโอกาส! ตัวเลขคือ {secret}")

def fizzbuzz():
    """FizzBuzz - ตัวอย่างคลาสสิก"""
    print("\n=== FizzBuzz (1-20) ===")
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

def prime_checker():
    """ตรวจสอบจำนวนเฉพาะ"""
    print("\n=== จำนวนเฉพาะ 1-50 ===")
    primes = []
    for num in range(2, 51):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(primes)

# เรียกใช้งาน
if __name__ == "__main__":
    guess_number_game()
    fizzbuzz()
    prime_checker()
    
    print("\n" + "="*50)
    print("📘 บทที่ 2: Control Flow - เสร็จสมบูรณ์!")
    print("="*50)
