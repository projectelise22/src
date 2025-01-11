# Integers, Floating Numbers

num_1 = 25000000
num_2 = 25_000_000
print(f"Number 1: {num_1}, Number 2: {num_2}")

num_3 = 1.75e+5
print(f"Number 3: {num_3}")

print(5 / 2)       # returns float
print(int(5 / 2))  # returns integer
print(5 // 2)      # integer division

print(0.1 + 0.2)  # approximation because it is stored in binary representation

# Challenge
resp_1 = input("\nEnter a base: ")
resp_2 = input("Enter an exponent: ")
res_1  = float(resp_1) ** float(resp_2)
print(f"{resp_1} to the power of {resp_2} = {res_1}")

# Number methods
num_3 = [2.5, 3.5, 3.14159, 2.0, 4, 0.887]
print(round(num_3[0]))  # rounds down when even integer when last digit is 5
print(round(num_3[1]))  # rounds up when odd integer when last digit is 5
print(round(num_3[2], 3))  # rounds to nearest thirds
for each in num_3:
    print(f"{each} is an integer?: {each.is_integer()}")

# Exercise: 2 inputs and check the difference if an integer
for i in range(3):
    resp_3 = input("\n \nEnter number 1: ")
    resp_4 = input("Enter number 2: ")
    res_2 = round(float(resp_3) - 1,1)
    print(f"The difference between {resp_3} and {resp_4} is {res_2}. Is it an integer? {res_2.is_integer()}!")

print(f"\n{num_3[2]:.2f}")       # shows 2 decimals to the left
print(f"{num_3[0]:.3f}")         # shows 3 decimals to the left
print(f"{num_3[-1]:.0%}")        # shows percentage with 0 decimals to the left
print(f"{num_3[-1]:.2%}")        # shows percentage with 2 decimals to the left
print(f"{num_3[1] ** 15:,.2f}")  #shows number with comma as separator