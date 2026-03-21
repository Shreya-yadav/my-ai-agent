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


def floor_number(number: float) -> float:
    """Return the floor of a number."""
    return math.floor(number)


def square_root(number: float) -> float:
    """Return the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)


def natural_logarithm(number: float) -> float:
    """Return the natural logarithm (base e) of a positive number."""
    if number <= 0:
        raise ValueError("Cannot calculate natural logarithm of a non-positive number.")
    return math.log(number)


def logarithm(number: float, base: float) -> float:
    """Return the logarithm of a positive number to a given positive base."""
    if number <= 0:
        raise ValueError("Cannot calculate logarithm of a non-positive number.")
    if base <= 0 or base == 1:
        raise ValueError("Base for logarithm must be positive and not equal to 1.")
    return math.log(number, base)


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
    print(floor_number(3.14)) # Example for floor
    print(floor_number(3.7)) # Another example for floor
    print(square_root(25)) # Example for square root
    print(square_root(2)) # Another example
    print(natural_logarithm(math.e)) # Example for natural logarithm
    print(natural_logarithm(10)) # Another example
    print(logarithm(100, 10)) # Example for logarithm base 10
    print(logarithm(8, 2)) # Example for logarithm base 2
