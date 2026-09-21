A **constructor** in Python is the code that initializes a new object when you create an instance of a class.

In everyday Python terminology, this usually means the special method:

```python
__init__
```

Technically, `__new__` creates the object and `__init__` initializes it, but `__init__` is commonly called the constructor. [typing.python](https://typing.python.org/en/latest/spec/constructors.html)

## Basic example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

When you create an object:

```python
person = Person("Alice", 30)
```

Python effectively calls:

```python
Person.__init__(person, "Alice", 30)
```

The object now contains:

```python
print(person.name)
# Alice

print(person.age)
# 30
```

## Meaning of `self`

`self` refers to the particular object being initialized:

```python
self.name = name
self.age = age
```

Here:

- `name` and `age` are constructor arguments.
- `self.name` and `self.age` are attributes stored inside the object.

## Default constructor values

Arguments can have defaults:

```python
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age
```

Now all of these are valid:

```python
p1 = Person("Alice", 30)
p2 = Person("Bob")
p3 = Person()
```

Their values are:

```python
print(p1.name, p1.age)
# Alice 30

print(p2.name, p2.age)
# Bob 0

print(p3.name, p3.age)
# Unknown 0
```

