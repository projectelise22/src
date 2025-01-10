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
num_3 = [2.5, 3.5, 3.14159, 2.0, 4]
print(round(num_3[0]))  # rounds down when even integer when last digit is 5
print(round(num_3[1]))  # rounds up when odd integer when last digit is 5
print(round(num_3[2], 3))  # rounds to nearest thirds
for each in num_3:
    print(f"{each} is an integer?: {each.is_integer()}")