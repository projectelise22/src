# Simple Calculator Application
# Used for testing pytests

# Addition
def add(n1, n2)->int:
    return (n1 + n2)

# Subtraction
def sub(n1, n2)->int:
    return (n1 - n2)

# Multiplication
def mul(n1, n2)->int:
    return (n1 * n2)

# Division
def div(n1, n2)->int:
    if n2 == 0: 
        raise ValueError("Cannot divide any number by 0!")
    return (n1 / n2)
