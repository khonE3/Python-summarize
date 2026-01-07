"""
=============================================================================
📘 บทที่ 8: Advanced Python
=============================================================================
เนื้อหา: Type Hints, Async/Await, Testing, Best Practices
=============================================================================
"""

# =============================================================================
# 8.1 Type Hints (การบอกใบ้ชนิดข้อมูล)
# =============================================================================

from typing import (
    List, Dict, Set, Tuple, Optional, Union, 
    Any, Callable, Iterable, Generator,
    TypeVar, Generic, Literal
)

# --- Basic Type Hints ---
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Variables
name: str = "John"
age: int = 30
height: float = 175.5
is_active: bool = True

# --- Collections ---
def process_items(items: List[str]) -> None:
    for item in items:
        print(item)

def get_scores() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 85}

def get_unique_numbers() -> Set[int]:
    return {1, 2, 3}

def get_coordinates() -> Tuple[float, float]:
    return (10.5, 20.3)

# --- Optional และ Union ---
def find_user(user_id: int) -> Optional[str]:
    """Return str หรือ None"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def process_input(value: Union[str, int]) -> str:
    """รับได้ทั้ง str หรือ int"""
    return str(value)

# Python 3.10+: ใช้ | แทน Union
def process_input_new(value: str | int) -> str:
    return str(value)

# --- Callable ---
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    """รับ function ที่รับ 2 int และ return int"""
    return func(a, b)

result = apply_function(lambda x, y: x + y, 3, 5)

# --- Type Variables (Generics) ---
T = TypeVar('T')

def first_element(items: List[T]) -> T:
    """Return element แรก ชนิดเดียวกับ input"""
    return items[0]

# Generic Class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)

# --- Literal Types ---
def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    print(f"Status set to: {status}")

set_status("active")  # OK
# set_status("unknown")  # Type checker จะ warning

# --- TypedDict (Python 3.8+) ---
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    email: str

user: UserDict = {
    "name": "Alice",
    "age": 25,
    "email": "alice@email.com"
}

# --- dataclasses with type hints ---
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

point = Point(3.0, 4.0)
print(f"Distance: {point.distance_from_origin()}")

# =============================================================================
# 8.2 Async/Await (Asynchronous Programming)
# =============================================================================

import asyncio

# --- Basic Async Function ---
async def say_hello():
    """Async function พื้นฐาน"""
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking sleep
    print("World")

# Run: asyncio.run(say_hello())

# --- Multiple Async Tasks ---
async def fetch_data(name: str, delay: float) -> str:
    """จำลองการ fetch data"""
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Got {name}!")
    return f"Data from {name}"

async def main():
    """รัน async tasks พร้อมกัน"""
    # Sequential (ช้า)
    # result1 = await fetch_data("API 1", 2)
    # result2 = await fetch_data("API 2", 2)
    
    # Concurrent (เร็ว)
    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 1),
        fetch_data("API 3", 1.5)
    )
    print(f"Results: {results}")

# asyncio.run(main())

# --- Async with timeout ---
async def slow_operation():
    await asyncio.sleep(10)
    return "Done"

async def with_timeout():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
    except asyncio.TimeoutError:
        print("Operation timed out!")

# --- Async Context Manager ---
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource...")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource...")
        await asyncio.sleep(0.1)
    
    async def do_something(self):
        print("Doing something...")

async def use_resource():
    async with AsyncResource() as resource:
        await resource.do_something()

# --- Async Generator ---
async def async_counter(n: int):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def consume_counter():
    async for num in async_counter(5):
        print(num)

# --- Task Management ---
async def task_example():
    # สร้าง task
    task = asyncio.create_task(fetch_data("Task", 2))
    
    # ทำงานอื่นในระหว่างที่รอ
    print("Doing other work...")
    await asyncio.sleep(1)
    
    # รอ task เสร็จ
    result = await task
    print(f"Task result: {result}")

# =============================================================================
# 8.3 Testing (การทดสอบ)
# =============================================================================

# --- unittest ---
import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """รันก่อนแต่ละ test"""
        self.calc = Calculator()
    
    def tearDown(self):
        """รันหลังแต่ละ test"""
        pass
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333, places=2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# Run: python -m unittest test_file.py

# --- pytest (ติดตั้ง: pip install pytest) ---
"""
# test_calculator.py

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    import pytest
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# Fixtures
@pytest.fixture
def calculator():
    return Calculator()

def test_with_fixture(calculator):
    assert calculator.add(1, 1) == 2

# Parametrize
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add_parametrize(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
"""

# Run: pytest test_file.py -v

# --- Mocking ---
from unittest.mock import Mock, patch, MagicMock

def test_mocking():
    # Create mock
    mock_func = Mock(return_value=42)
    result = mock_func(1, 2, 3)
    
    # Assertions
    mock_func.assert_called_once()
    mock_func.assert_called_with(1, 2, 3)
    
    # Side effects
    mock_func.side_effect = ValueError("Error!")
    # mock_func()  # Raises ValueError

# Patching
class APIClient:
    def fetch(self, url):
        # Real API call
        import requests
        return requests.get(url)

def test_with_patch():
    with patch.object(APIClient, 'fetch') as mock_fetch:
        mock_fetch.return_value = Mock(status_code=200, json=lambda: {"data": "test"})
        
        client = APIClient()
        response = client.fetch("http://api.example.com")
        
        assert response.status_code == 200

# =============================================================================
# 8.4 Best Practices
# =============================================================================

# --- PEP 8 Style Guide ---
"""
1. Indentation: 4 spaces
2. Line length: 79 characters (code), 72 (docstrings)
3. Blank lines:
   - 2 between top-level definitions
   - 1 between methods in class
4. Imports: 
   - One per line
   - Grouped: standard library, third-party, local
5. Naming:
   - Functions/variables: snake_case
   - Classes: PascalCase
   - Constants: UPPER_CASE
   - Private: _leading_underscore
"""

# --- Code Organization ---
"""
my_project/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
"""

# --- Documentation ---
def calculate_total(items: List[Dict[str, float]], tax_rate: float = 0.07) -> float:
    """
    Calculate total price with tax.
    
    Args:
        items: List of items with 'price' and 'quantity' keys.
        tax_rate: Tax rate as decimal (default: 0.07 = 7%).
    
    Returns:
        Total price including tax.
    
    Raises:
        ValueError: If any item has negative price or quantity.
    
    Examples:
        >>> items = [{'price': 100, 'quantity': 2}]
        >>> calculate_total(items)
        214.0
    """
    subtotal = 0
    for item in items:
        if item['price'] < 0 or item['quantity'] < 0:
            raise ValueError("Price and quantity must be non-negative")
        subtotal += item['price'] * item['quantity']
    
    return subtotal * (1 + tax_rate)

# --- Error Handling Best Practices ---
class ApplicationError(Exception):
    """Base exception for application"""
    pass

class ValidationError(ApplicationError):
    """Raised when validation fails"""
    pass

class NotFoundError(ApplicationError):
    """Raised when resource not found"""
    pass

def get_user(user_id: int) -> Dict[str, Any]:
    """Best practice error handling"""
    if not isinstance(user_id, int):
        raise TypeError("user_id must be an integer")
    
    if user_id < 0:
        raise ValueError("user_id must be non-negative")
    
    users = {1: {"name": "Alice"}}
    
    if user_id not in users:
        raise NotFoundError(f"User {user_id} not found")
    
    return users[user_id]

# --- Logging Best Practices ---
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    # filename='app.log'  # Optional: log to file
)

logger = logging.getLogger(__name__)

def process_order(order_id: int) -> bool:
    logger.info(f"Processing order {order_id}")
    
    try:
        # Process order
        logger.debug(f"Order {order_id} details loaded")
        logger.info(f"Order {order_id} processed successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to process order {order_id}: {e}", exc_info=True)
        return False

# =============================================================================
# 8.5 Design Patterns
# =============================================================================

# --- Singleton ---
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(f"Same instance: {s1 is s2}")  # True

# --- Factory ---
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create(animal_type: str) -> Animal:
        animals = {
            "dog": Dog,
            "cat": Cat
        }
        if animal_type not in animals:
            raise ValueError(f"Unknown animal type: {animal_type}")
        return animals[animal_type]()

dog = AnimalFactory.create("dog")
print(dog.speak())

# --- Observer ---
class Subject:
    def __init__(self):
        self._observers: List[Callable] = []
    
    def attach(self, observer: Callable) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Callable) -> None:
        self._observers.remove(observer)
    
    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer(message)

def email_observer(message: str) -> None:
    print(f"Email: {message}")

def sms_observer(message: str) -> None:
    print(f"SMS: {message}")

subject = Subject()
subject.attach(email_observer)
subject.attach(sms_observer)
subject.notify("Order shipped!")

# --- Decorator Pattern (ไม่ใช่ Python decorator) ---
class Coffee:
    def cost(self) -> float:
        return 50.0
    
    def description(self) -> str:
        return "Coffee"

class MilkDecorator:
    def __init__(self, coffee: Coffee):
        self._coffee = coffee
    
    def cost(self) -> float:
        return self._coffee.cost() + 10.0
    
    def description(self) -> str:
        return self._coffee.description() + " + Milk"

coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
print(f"{coffee_with_milk.description()}: {coffee_with_milk.cost()} THB")

# =============================================================================
# 8.6 Performance Tips
# =============================================================================

import time

# --- List vs Generator ---
def performance_comparison():
    n = 1000000
    
    # List (ใช้ memory มาก)
    start = time.time()
    squares_list = [x**2 for x in range(n)]
    _ = sum(squares_list)
    list_time = time.time() - start
    
    # Generator (ประหยัด memory)
    start = time.time()
    squares_gen = (x**2 for x in range(n))
    _ = sum(squares_gen)
    gen_time = time.time() - start
    
    print(f"List: {list_time:.4f}s, Generator: {gen_time:.4f}s")

# --- String Concatenation ---
def string_performance():
    n = 10000
    
    # Slow: += in loop
    start = time.time()
    result = ""
    for i in range(n):
        result += str(i)
    method1_time = time.time() - start
    
    # Fast: join()
    start = time.time()
    result = "".join(str(i) for i in range(n))
    method2_time = time.time() - start
    
    print(f"+= : {method1_time:.4f}s, join: {method2_time:.4f}s")

# --- Use Built-in Functions ---
"""
# Slow
total = 0
for num in numbers:
    total += num

# Fast
total = sum(numbers)

# Slow
for i in range(len(items)):
    print(i, items[i])

# Fast
for i, item in enumerate(items):
    print(i, item)
"""

# --- Caching ---
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(n: int) -> int:
    """ผลลัพธ์ถูก cache"""
    time.sleep(0.01)  # Simulate expensive operation
    return n * n

# =============================================================================
# 8.7 ตัวอย่างโปรแกรม
# =============================================================================

@dataclass
class Task:
    """Task model with type hints"""
    id: int
    title: str
    completed: bool = False
    priority: Literal["low", "medium", "high"] = "medium"
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

class TaskManager:
    """Task management system"""
    
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def add_task(self, title: str, priority: str = "medium", tags: List[str] = None) -> Task:
        task = Task(
            id=self._next_id,
            title=title,
            priority=priority,
            tags=tags or []
        )
        self._tasks[task.id] = task
        self._next_id += 1
        self.logger.info(f"Added task: {task.title}")
        return task
    
    def complete_task(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            raise NotFoundError(f"Task {task_id} not found")
        
        self._tasks[task_id].completed = True
        self.logger.info(f"Completed task {task_id}")
        return True
    
    def get_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        tasks = list(self._tasks.values())
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]
        return tasks
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        return [t for t in self._tasks.values() if t.priority == priority]

# Tests
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
    
    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(task.title, "Test task")
        self.assertFalse(task.completed)
    
    def test_complete_task(self):
        task = self.manager.add_task("Test")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager._tasks[task.id].completed)
    
    def test_complete_nonexistent_task(self):
        with self.assertRaises(NotFoundError):
            self.manager.complete_task(999)

# เรียกใช้งาน
if __name__ == "__main__":
    print("\n=== Task Manager Demo ===")
    
    manager = TaskManager()
    
    # Add tasks
    task1 = manager.add_task("Learn Python", "high", ["programming", "study"])
    task2 = manager.add_task("Buy groceries", "medium", ["shopping"])
    task3 = manager.add_task("Read book", "low", ["hobby"])
    
    # Complete task
    manager.complete_task(task1.id)
    
    # List tasks
    print("\nAll tasks:")
    for task in manager.get_tasks():
        status = "✓" if task.completed else "○"
        print(f"  [{status}] {task.id}. {task.title} ({task.priority})")
    
    print("\nPending tasks:")
    for task in manager.get_tasks(completed=False):
        print(f"  ○ {task.title}")
    
    # Performance demo
    print("\n=== Performance Comparison ===")
    performance_comparison()
    string_performance()
    
    # Run tests
    print("\n=== Running Tests ===")
    # unittest.main(argv=[''], exit=False, verbosity=2)
    
    print("\n" + "="*50)
    print("📘 บทที่ 8: Advanced Python - เสร็จสมบูรณ์!")
    print("="*50)
