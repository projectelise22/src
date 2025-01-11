# Functions
# Anything written under the return line will not be executed
# Use docstrings """ ... """ to document the description of the function

# Sample user defined function
def multiply(x, y):
    """Function: gets two inputs and outputs their product"""
    product = x * y
    return product

# print(help(multiply))

# Exercise
def cube(in_1):
    """Function: gets 1 input and outputs it to the power of 3"""
    res_1 = in_1 ** 3
    return res_1

print(f"Cube of 3 is {cube(3):,}")
print(f"Cube of 123 is {cube(123):,}")

def greet(in_name):
    "Function: gets 1 string input, outputs a statement with the input"
    print(f"Hello {in_name}!")

greet("Dolly")
greet("Maria Eva Linette")

# Challenges
def convert_cel_to_far() -> float:
    """Function: gets celsius input, outputs it to fahrenheit"""
    in_cel  = input("Enter a temperature in degrees C: ")
    out_far = float(in_cel) * 9 / 5 + 32
    print(f"{in_cel} degrees Celsius = {out_far:.2f} degrees Fahrenheit")

def convert_far_to_cel() -> float:
    """FUnction: gets fahrenheit input, outputs it to celsius"""
    in_far  = input("Enter a temperature in degrees F: ")
    out_cel = (float(in_far) - 32) * 5 / 9
    print(f"{in_far} degrees Fahrenheit = {out_cel:.2f} degrees Celsius")

for i in range(2):
    convert_cel_to_far()
    convert_far_to_cel()

# Loops
# While loop sample
name = "John"
while name != "Dolly":
    resp_1 = input("Please input your name: ")
    name = resp_1
    print(f"Hello, I have been waiting for you {name}")

for n in range (1, 5):  # prints from 1 to 4
    print(n)

for n in range(1, 4):  # nested loop, size: 3x3
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")

# Exercise
for n in range(2, 11):
    print(f"\nNext number is [{n}].")

n = 2
while n < 11:
    print(f"\nNext number is [{n}].")
    n += 1

def doubles(in_double: int) -> int:
    """Function: gets an integer input, outputs the double of the input"""
    in_double = in_double * 2
    return in_double

double_2 = 2
for n in range(0, 3):
    double_2 = doubles(double_2)
    print(double_2)

# Challenge
# investment that tracks the growth of an investment over time
# initial deposit = principal_amt : increases annually with fixed annual_rate
def invest(principal_amt: float, annual_rate: float, years: int) -> float:
    """Function: gets principal_amt, annual_rate, years and outputs total amount"""
    total_amt = principal_amt
    for i in range(years):
        total_amt += total_amt * annual_rate
        print(f"\n year {i}: {total_amt:.2f}")

for i in range (2):
    principal_amt = input("\n Enter principal amount: ")
    annual_rate = input("\n Enter annual rate: ")
    years = input("\n Enter number of years: ")
    invest(float(principal_amt), float(annual_rate), int(years))
