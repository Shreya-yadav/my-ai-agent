# My AI-enhanced Python project

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


if __name__ == "__main__":
    print(greet("World"))
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
    print(floor_divide(10, 3)) # Example for floor division
    print(exponentiate(2, 3))
