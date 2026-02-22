# Type Annotations

## Normal Dictionary

```python
movie = {"name": "Avengers Endgame", "year": 2019}
```

- Allows for efficient data retrieval based on unique keys.
- Flexible and easy to implement
- Leads to challenges in ensuring that the data is a particular structure especially for larger projects
- Doesn't check if the data is the correct type or structure.

## Typed Dictionary

```python
from typing import TypedDict

class Movie(TypedDict):
  name: str
  year: int

movie = Movie(name="Avengers Endgame", year=2019)
```

- **Type Safety** - we defined explicitly what the data structures are, reducing runtime errors
- **Enhanced Readability** - Makes debugging easier and makes code naturally understandable.

## Union

```python
from typing import Union

def square(x: Union[int, float]) -> float:
  return x * x

x = 5               # ✅ This is fine because it is an integer
x = 1.234           # ✅ This is also fine because it is a float
x = "I am a string" # ❌ This will fail because it is a string
```

- Union lets you say that a value can be more than one type
- Flexible and easy to code
- Type Safety as it can provide hints to help catch incorrect usage

## Optional

```python
from typing import Optional

def nice_message(name: Optional[str]) -> None:
  if name is None:
    print("Hello, stranger!")
  else:
    print(f"Hello, {name}!")
```

- In this case "name" can be either String or None!
- It cannot be anything else

## Any

```python
from typing import Any

def print_value(x: Any):
  print(x)
```

- Anything and everything is allowed

## Lambda Function

```python
square = lambda x: x * x
print(square(5))  # Output: 25

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
```

- Lambda is just a shortcut to writing small functions!
- A lambda function is an anonymous function that can take any number of arguments but can only have one expression.
