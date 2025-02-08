# Strings
# Check the type of the following variable

str_1 = "Hello, World!"
type_str_1 = type(str_1)
print(type_str_1)

# Check the length of the string
len_str_1 = len(str_1)
print(len_str_1)

# Use backslash \ for paragraphs in editor
# PEP 8 says one line should contain 79 characters or less
str_2 = "Whatever the case, this shows multiple lines \
this is another line \
and this is another line"
print(str_2)

# Use """ for paragraphs in output
str_3 = """Check the output to see how this
paragraph is displayed against the paragraph
written above"""
print(str_3)

# Concatenating strings
str_4 = str_2 + str_2
print(str_4)

# Indexing (positive) from 0 to last string
str_5 = "fig pie"
for i in range(0, len(str_5)):
  print(str_5[i])

# Indexing (negative) from -1 to first string
for i in range(0, len(str_5)):
  print(str_5[-1-i])

# Slicing strings
print(str_5[0:3])     # returns index 0, 1, 2
print(str_5[:3])      # returns index from first string to 2
print(str_5[3:])      # returns index 3 to last string
print(str_5[3:15])    # doesn't raise error, will return from index 3 to last string
print(str_5[20:30])   # doesn't raise error, will return empty string (be cautious)
print(str_5[-7:0])    # doesn't raise error, will return empty (be mindful that 0 index is first string)
print(str_5[-10:-1])  # doesn't raise error, but will return until second to the last, because of above
print(str_5[-7:])     # omit the second number of range to return until last string
print(str_5[-10:-9])  # same concept as for the positive indexing

# Strings are immutable - cannot be changed once you created them
# when you try to change by
# str_5[0] = "d", it will result to a runtime error
# you can modify the string by concatening or by changing the whole string itself
str_5 = "apple" + str_5[3:] 
print(str_5)

str_5 = "peach pie"
print(str_5)

# Removing spaces in string
str_5 = "       " + str_5 + "               " 
print(len(str_5))           # returns total length of string with left and right spaces
print(len(str_5.lstrip()))  # returns length with left spaces removed
print(len(str_5.rstrip()))  # returns length with right spaces removed
print(len(str_5.strip()))   # returns length with left and right spaces removed, in between are conserved

# Checking pattern of string
str_5 = str_5.strip()        # to keep the result of the string function, either you assign to new variable or reassign it
print(str_5.startswith("p")) # case sensitive
print(str_5.endswith("E"))   # case sensitive

# To see all the methods of a string, type "<variable string>.", click tab

# Exercise: Get the first letter of the input and capitalize it
resp_1 = input("Tell me your password: ")
print("The first letter you entered was: " + resp_1.upper()[0])

# Strings and Operators
str_6 = "20"
print(str_6 * 3)      # triples the string and concatenates it
print(str_6 + str_6)  # concatenates the string

print(int(str_6) / 2)    # convert string to integer 
print(float(str_6) / 3)  # convert string to float

num_1 = 5
print("I have " + str(num_1) + " books")  #convert integer to string

# f-strings
print(f"I have {str_6} novels and {num_1} fiction")

# Exercise: formatting strings
num_2 = 0.2
str_7 = "newt"

print("CONCAT: " + str(num_2) + " is the weight of the " + str_7)
print(".format: {} is the weight of the {}".format(num_2, str_7))
print(f"f-string: {num_2} is the weight of the {str_7}")

# Finding and replacing strings
str_8 = "I have the number 88888-8888-998"
print(str_8.find("9"))         # finds the first string only, returns index
print(str_8.find("0"))         # returns -1 when not found
print(str_8.replace("8", "1")) # replaces all instances
print(str_8)

# Exercise: find "n" in the statement entered by the user
resp_2 = input("\n Best thing that ever happened today?: ")
resp_3 = resp_2.find("n") 
print(f"There is a letter {resp_2[resp_3]} in your statement")

# Challenge: encoding a sentence
resp_4 = input("\n \nEnter a sentence: ")
res_1 = resp_4
find_list = ["a", "b", "e", "l", "o", "s", "t"]
repl_list = ["4", "8", "3", "1", "0", "5", "7"]
for i in range(len(find_list)):
  res_1 = res_1.replace(find_list[i], repl_list[i])
print(f"What you wrote: {resp_4}")
print(f"What was encoded: {res_1}")


def removeDuplicates(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  unique_nums = list(set(nums))
  new_nums = unique_nums
  nums = new_nums + [1] * (len(nums) - len(new_nums))
  return len(new_nums), nums

print(removeDuplicates([1,2,2,2,3,4,5,6,6,6]))

x = [1, 2, 3]
print(x[1])



