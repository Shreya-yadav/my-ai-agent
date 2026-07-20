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


def degrees_to_radians(degrees: float) -> float:
    """Convert an angle from degrees to radians."""
    return math.radians(degrees)


def radians_to_degrees(radians: float) -> float:
    """Convert an angle from radians to degrees."""
    return math.degrees(radians)


def sine(angle_radians: float) -> float:
    """Return the sine of an angle given in radians."""
    return math.sin(angle_radians)


def cosine(angle_radians: float) -> float:
    """Return the cosine of an angle given in radians."""
    return math.cos(angle_radians)


def tangent(angle_radians: float) -> float:
    """Return the tangent of an angle given in radians."""
    return math.tan(angle_radians)