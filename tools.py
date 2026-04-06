def multiply(a: int, b: int) -> int:
    return a * b

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

# Tool registry — maps string names to actual functions
# This is the pattern every framework uses internally
TOOL_REGISTRY = {
    "multiply": multiply,
    "add": add,
    "subtract": subtract,
}