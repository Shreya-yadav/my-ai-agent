# My AI-enhanced Python project
import math

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def floor_divide(a: float, b: float) -> float:
    """Perform floor division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b


def exponentiate(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot perform modulo with zero divisor.")
    return a % b


def absolute(number: float) -> float:
    """Return the absolute value of a number."""
    return abs(number)


def round_number(number: float, ndigits: int = 0) -> float:
    """Round a number to a given precision in decimal digits."""
    return round(number, ndigits)


def ceil_number(number: float) -> float:
    """Return the ceiling of a number."""
    return math.ceil(number)


def square_root(number: float) -> float:
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


if __name__ == "__main__":
    print(greet("World"))
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
    print(floor_divide(10, 3)) # Example for floor division
    print(exponentiate(2, 3))
    print(modulo(10, 3)) # Example for modulo operation
    print(absolute(-7.5)) # Example for absolute value
    print(round_number(3.14159, 2)) # Example for rounding
    print(round_number(3.7)) # Example for rounding to nearest integer
    print(ceil_number(3.14)) # Example for ceiling
    print(ceil_number(3.7)) # Another example for ceiling
    print(square_root(25)) # Example for square root
    print(square_root(2)) # Another example
