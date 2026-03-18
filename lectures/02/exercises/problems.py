
"""Lecture 02 exercises (classes) - implement from scratch.
Any 14 / 16 problems solved count as 100%
"""

"""
1) Create class User with:
    name,
    method say_hi() which prints "Hello, I am {name}"
"""
class User:
  def __init__(self, name):
    self.name = name
  
  def say_hi(self):
    print(f"Hello, I am {self.name}")
    

"""
2) BankAccount
Create class `BankAccount` with:
- `__init__(self, owner: str, balance: float = 0.0) -> None`
- `deposit(self, amount: float) -> None`
- `withdraw(self, amount: float) -> None`
Rules:
- Initial negative balance becomes `0.0`.
- Non-positive `deposit`/`withdraw` amounts are ignored.
- `withdraw` bigger than current balance is ignored.
"""
class BankAccount:
  def __init__(self, owner: str, balance: float = 0.0) -> None:
    self.owner = owner
    self.balance = balance
    if balance <= 0:
      self.balance = 0.0
    
  def deposit(self, amount: float) -> None:
    self.amount = amount
    if amount <= 0:
      return
    else:
      self.balance += amount
      
  def withdraw(self, amount: float) -> None:
    self.amount = amount
    if amount <= 0:
      return
    if amount > self.balance:
     return 
    else:
      self.balance -= amount

"""
3) Team
Create class `Team` with:
- `__init__(self) -> None`
- `add(self, name: str) -> None`
- `__len__(self) -> int`
Rules:
- Members are stored in insertion order.
- Each instance has independent member storage.
"""
class Team:
  def __init__(self) -> None:
    self.members = []
    
  def add(self, name: str) -> None:
    self.name = name
    self.members.append(self.name)
    
  def __len__(self) -> int:
    return len(self.members)

""" (Advanced, optional)
5) QueueState
Create class `QueueState`:
- `__init__(self) -> None` (initialize empty `items` list)
Methods:
- `push(self, item: str) -> None`
- `pop(self) -> str | None`
Rules:
- FIFO behavior.
- `pop` returns `None` when empty.
"""


""" (Advanced, optional)
6) Wallet + custom errors
Create:
- `class PaymentError(Exception): ...`
- `class InsufficientFunds(PaymentError): ...`
- `class Wallet` with:
  - `__init__(self, balance: float = 0.0) -> None`
  - `top_up(self, amount: float) -> None`
  - `pay(self, amount: float) -> None`
Rules:
- Initial balance must be >= 0.
- `top_up` and `pay` require amount > 0.
- If `pay` exceeds balance, raise `InsufficientFunds`.
"""


"""
7) ShoppingCart
Create class `ShoppingCart` with:
- `__init__(self) -> None`
- `add_item(self, name: str, price: float, qty: int = 1) -> None`
- `total_items(self) -> int`
- `total_price(self) -> float`
Rules:
- `price < 0` or `qty <= 0` items are ignored.
- `repr` must include `ShoppingCart`.
"""
class ShoppingCart:
  def __init__(self) -> None:
    self.qt = 0
    self.pr = 0.0
    
  def add_item(self, name: str, price: float, qty: int = 1) -> None:
    self.name = name
    if qty <= 0 or price <= 0:
      return
    else:
      self.qty = qty
      self.qt += self.qty
      self.price = price
      self.pr += (self.price * self.qty)
      
  def total_items(self) -> int:
    return self.qt
  
  def total_price(self) -> float:
    return self.pr
  
  def __repr__(self):
    return f"ShoppingCart({self.qt}, {self.pr})"
      
"""
8) Classroom (class attribute)
Create class `Classroom` with class attribute:
- `school_name = "Harbour Space"`
Methods:
- `__init__(self, group_name: str) -> None`
- `add_student(self, name: str) -> None`
- `__len__(self) -> int`
- `set_school_name(self, new_name: str) -> None`
Rules:
- `set_school_name` must update shared class attribute for all instances.
"""
class Classroom:
  school_name = "Harbour Space"
  def __init__(self, group_name: str) -> None:
    self.group_name = group_name
    self.cls = []
  def add_student(self, name: str) -> None:
    self.cls.append(name)
  def __len__(self) -> int:
    return len(self.cls)
  def set_school_name(self, new_n: str):
    Classroom.school_name = new_n

"""
9) Rectangle
Create class `Rectangle` with:
- `__init__(self, width: float, height: float) -> None`
- `area(self) -> float`
- `perimeter(self) -> float`
Rules:
- Store positive dimensions using absolute values.
"""
class Rectangle:
  def __init__(self, width: float, height: float) -> None:
    self.width = width
    self.height = height
  def area(self) -> float:
    if self.height < 0:
      return -1 * self.width * self.height 
    if self.width < 0:
      return -1 * self.width * self.height 
    return self.width * self.height
  def perimeter(self) -> float:
    if self.height < 0:
      return 2 * (self.width + self.height * (-1))
    if self.width < 0:
      return 2 * ((-1) * self.width + self.height)
    return 2 * (self.width + self.height)
  def __repr__(self):
    return f"Rectangle({self.width}, {self.height})"
  

"""
10) Playlist
Create class `Playlist` with:
- `__init__(self) -> None`
- `add(self, song: str) -> None`
- `__len__(self) -> int`
- `__iter__(self)`
- `__contains__(self, song: str) -> bool`
Rules:
- Preserve insertion order.
"""
class Playlist:
  def __init__(self):
    self.list = []
  
  def add(self, song: str):
    self.song = song
    self.list.append(self.song)
    
  def __len__(self):
    return len(self.list)
  
  def __iter__(self):
    return iter(self.list)
  
  def __contains__(self, song):
    return song in self.list

"""
11) Product
Create class `Product` with:
- `__init__(self, name: str, price: float) -> None`
- `get_price(self) -> float`
- `set_price(self, value: float) -> None`
- `apply_discount(self, percent: float) -> None`
Rules:
- Negative price is clamped to `0`.
- Discount percent is clamped to `[0, 100]`.
"""
class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    
  def get_price(self):
    return self.price
  
  def set_price(self, value):
    if value < 0:
      self.price = 0
    else:
      self.price = value
    
  def apply_discount(self, percent):
    if 0 <= percent <= 100:
      self.price = float(self.price - ((self.price * percent) / 100))
    else:
      self.price = 0.0
    
      
      

"""
12) Person + Student (inheritance)
Create:
- `class Person` with `__init__(name)` and `describe()`
- `class Student(Person)` with `__init__(name, group)` and overridden `describe()`
Required format:
- `Person(name=Ana)`
- `Student(name=Bo, group=G2)`
"""

class Person:
  def __init__(self, name):
    self.name = name
  def describe(self):
    return f"Person(name={self.name})"
  
class Student:
    def __init__(self, name, group):
      self.name = name
      self.group = group
    def describe(self):
      return f"Student(name={self.name}, group={self.group})"
    

"""
13) Point2D (magic methods)
Create class `Point2D` with:
- `__init__(self, x: float, y: float) -> None`
- `distance_to(self, other: "Point2D") -> float`
- `__eq__(self, other: object) -> bool`
Rules:
- Euclidean distance.
- `repr` format: `Point2D(x, y)`.
"""
class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance_to(self, other):
    return ((self.x - other.x)**2 + (self.y - other.y)**2) ** (1/2)
  def __eq__(self, other):
    return isinstance(other, Point2D) and self.x == other.x and self.y == other.y
  def __repr__(self):
    return f"Point2D({self.x}, {self.y})"
"""
14) Inventory
Create class `Inventory` with:
- `__init__(self) -> None`
- `add(self, name: str, qty: int = 1) -> None`
- `remove(self, name: str, qty: int = 1) -> None`
- `count(self, name: str) -> int`
- `__contains__(self, name: str) -> bool`
- `__len__(self) -> int`
Rules:
- Non-positive `qty` is ignored.
- Removing too much removes item completely (count becomes `0`).
"""

class Inventory:
  def __init__(self):
    self.items = {}
    
  def add(self, name, qty: int = 1):
    if name in self.items.keys():
      if qty <= 0:
        return
      else:
        self.items[name] += qty
    else:
      if qty <= 0:
        return
      else:
        self.items[name] = qty

    
  def remove(self, name, qty: int = 1):
    if name in self.items.keys():
      if self.items[name] >= qty:
        self.items[name] -= qty
        if self.items[name] == 0:
          del self.items[name]  
    else:
      return
    
  def count(self, name):
    if name in self.items.keys():
      return self.items[name]
    else:
      return 0
  
  def __contains__(self, name):
    return name in self.items.keys()
  
  def __len__(self):
    return len(self.items)
      

"""
15) CourseCatalog
Create class `CourseCatalog` with:
- `__init__(self) -> None`
- `add_course(self, code: str, title: str) -> None`
- `get_title(self, code: str) -> str | None`
- `__iter__(self)` returning `(code, title)` sorted by code
- `__len__(self) -> int`
"""
class CourseCatalog:
  def __init__(self):
    self.cat = {}
  
  def add_course(self, code, title):
    self.cat[code] = title
  
  def get_title(self, code):
    return self.cat[code]
  def __iter__(self):
    return iter(sorted(self.cat.items(), key = lambda x: x[0]))
  def __len__(self):
    return len(self.cat)
"""
16) DefaultDict (magic methods)
Create class `DefaultDict` with:
- `__init__(self, default_factory=None) -> None`
- `__getitem__(self, key)`
- `__setitem__(self, key, value) -> None`
- `__contains__(self, key) -> bool`
- `__len__(self) -> int`
Rules:
- On missing key:
  - if `default_factory` is `None`, return `None`.
  - otherwise create value using `default_factory()`, store, return.
- If `default_factory` is not callable, treat it as `None`.
"""
class DefaultDict:
  def __init__(self, default_factory=None):
      self.default_factory = default_factory
      self.items = {}
  def __getitem__(self, key):
    if key in self.items.keys():
      return self.items[key]
    if callable(self.default_factory):
      self.items[key] = self.default_factory()
      return self.items[key]
    return None
  
  def __setitem__(self, key, value):
    self.items[key] = value
    
  def __contains__(self, key):
    return key in self.items.keys()
  
  def __len__(self):
    return len(self.items)
