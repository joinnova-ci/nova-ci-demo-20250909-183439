"""Calculator module with comprehensive math functions."""
import math
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b

def divide(a: Number, b: Number) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def power(a: Number, b: Number) -> Number:
    """Raise a to the power of b."""
    return a ** b

def modulo(a: Number, b: Number) -> Number:
    """Get remainder of a divided by b."""
    if b == 0:
        raise ValueError("Modulo by zero")
    return a % b

def absolute(x: Number) -> Number:
    """Get absolute value of a number."""
    return abs(x)

def square_root(x: Number) -> float:
    """Get square root of a positive number."""
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)

def factorial(n: int) -> int:
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def max_of_two(a: Number, b: Number) -> Number:
    """Return the larger of two numbers."""
    return max(a, b)
