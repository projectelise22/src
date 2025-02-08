# Exercise
def check_str_5():
    """Function: Check if a string has <, >, or = 5 characters."""
    in_str = input("Enter a string: ")
    if len(in_str) < 5:
        print(f"The inputted string [{in_str}] has less than 5 characters.")
    elif len(in_str) == 5:
        print(f"The inputted string [{in_str}] has exactly 5 characters.")
    else:
        print(f"The inputted string [{in_str}] has more than 5 characters.")

for i in range(3):
    check_str_5()

def check_factors(num: int):
    """Function: Check all the factors of an integer"""
    factor = 1
    while factor <= num:
        if num % factor == 0:
            print(f"{factor} is a factor of {num}")
        factor += 1

for i in range(3):
    try:
        in_factor = int(input("Enter an integer: "))
        check_factors(in_factor)
    except ValueError:
        print("You did not input an integer")    

# stop the iteration by using break
# skip the current iteration by using continue
# for .. else loop also exists 
for i in range(5):
    check_q = input("Input 'q' or 'Q' to quit: ")
    if check_q.lower() == 'q':
        break
else:
    print("Inputted incorrectly for 5 attempts.")

for n in range(1, 51):
    if n % 3 == 0:
        continue
    print(f"{n} is not a multiple of 3.")

# Exercise
in_str1 = input("Enter a string: ")

try:
    in_int = input("Enter an integer: ")
    in_int = int(in_int)
except ValueError:
    print("You did not input an integer.")

try:
    ind_value = in_str1[in_int]
    print("The value of the string on index{in_int} is {ind_value}")
except IndexError:
    print("The index is out of range.")

import random

# Exercise
def roll():
    """Function: simulates rolling a dice, returns random integer from 1 to 6"""
    res_1 = random.randint(1, 6)
    return res_1

roll_out = [0] * 6
for i in range (10_000):
    res_roll = roll()
    if res_roll == 1:
        roll_out[0] += 1
    elif res_roll == 2:
        roll_out[1] += 1
    elif res_roll == 3:
        roll_out[2] += 1
    elif res_roll == 4:
        roll_out[3] += 1
    elif res_roll == 5:
        roll_out[4] += 1
    elif res_roll == 6:
        roll_out[5] += 1
print(f"1 is rolled {roll_out[0]/10_000:.2%} of the time.")
print(f"2 is rolled {roll_out[1]/10_000:.2%} of the time.")
print(f"3 is rolled {roll_out[2]/10_000:.2%} of the time.")
print(f"4 is rolled {roll_out[3]/10_000:.2%} of the time.")
print(f"5 is rolled {roll_out[4]/10_000:.2%} of the time.")
print(f"6 is rolled {roll_out[5]/10_000:.2%} of the time.")

def coin_flip():
    """Function: simulates flipping a coin, returns 'heads' or 'tails'"""
    res_2 = random.randint(0, 1)
    if res_2 == 0:
        return 'heads'
    else:
        return 'tails'

flip_out = [0, 0]
for i in range(10_000):
    while flip_out[0] >= 0 and flip_out[1] >= 0:
        res_coin = coin_flip()
        if res_coin == 'heads':
            flip_out[0] += 1
        else:
            flip_out[1] += 1

        if flip_out[0] == flip_out[1]:
            break
    average = flip_out[0] + flip_out[1]
    print(f"The average number of flips before the number of heads and tails are equal is {average:.2f}.")
    flip_out = [0, 0]   

coordinates = 4, 5
type(coordinates)
x, y = coordinates
print(f"x: {x}, y: {y}")

# Exercise - Tuples
cardinal_numbers = ("first", "second", "third")
print(f"index 1: {cardinal_numbers[1]}")

position1, position2, position3 = cardinal_numbers

my_name  = tuple("Dolly")
check_x  = "x" in my_name
print(f"{check_x}")
my_name1 = my_name[1:]
print(my_name1)

# Exercise - Lists
universities = [
['California Institute of Technology', 2175, 37704], ['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732], ['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(univ_list):
    """Function: takes an input list of lists with 3 elements: name of university, no. of students, tuition fee
                 returns list enrollment status with number of students
                 returns list of tuition fees"""
    student_tuition = [[], []]
    for each in univ_list:
        student_tuition[0].append(each[1])
        student_tuition[1].append(each[2])
    
    return student_tuition

def list_mean(list_num: list) -> float:
    """Function: takes an input list of numbers, returns the mean"""
    if not list_num:
        raise ValueError("The input list is empty.")
    return sum(list_num)/len(list_num)

def list_med(list_num: list) -> float:
    """Function: takes an input list of numbers, returns the median"""
    if not list_num:
        raise ValueError("The input list is empty.")
    med_ind = len(list_num)//2
    list_num.sort()
    if len(list_num) % 2 == 0:
        return (list_num[med_ind-1] + list_num[med_ind])/2
    else:
        return list_num[med_ind]

total_students, total_tuition = sum(enrollment_stats(universities)[0]), sum(enrollment_stats(universities)[1])
mean_students = list_mean(enrollment_stats(universities)[0])
median_students = list_med(enrollment_stats(universities)[0])
mean_tuition = list_mean(enrollment_stats(universities)[1])
median_tuition = list_med(enrollment_stats(universities)[1])
print("******************************")
print(f"\nTotal students: {total_students}")
print(f"Total tuition: $ {total_tuition:,.2f}")
print(f"\nStudents mean: {mean_students}")
print(f"Student median: {median_students}")
print(f"\nTuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,.2f}\n")
print("******************************")

nouns_list = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs_list = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj_list = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep_list = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adv_list = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

# Randomly select 3 nouns, 3 verbs, 3 adjectives, 2 prepositions, 1 adverb
new_nouns = random.sample(nouns_list, 3)
new_verbs = random.sample(verbs_list, 3)
new_adj = random.sample(adj_list, 3)
new_prep = random.sample(prep_list, 2)
new_adv = random.sample(adv_list, 1)

if new_adj[0][0] in "aeiou":
    article_1 = "an"
else:
    article_1 = "a"

if new_adj[2][0] in "aeiou":
    article_2 = "an"
else:    
    article_2 = "a"

print(f"""\n{article_1.capitalize()} {new_adj[0]} {new_nouns[0]}\n
  {article_1.capitalize()} {new_adj[0]} {new_nouns[0]} {new_verbs[0]} {new_prep[0]} the {new_adj[1]} {new_nouns[1]}\n
  {new_adv[0]}, the {new_nouns[0]} {new_verbs[1]}\n
  the {new_nouns[1]} {new_verbs[2]} {new_prep[1]} {article_2} {new_adj[2]} {new_nouns[2]}""")

# Nested Dictionaries:
states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    }
}
print(states["California"]["capital"])
print(states["Texas"])

# Exercise - Dictionaries
# empty dictionary
captains = {}
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" in captains:
    print(f"Enterprise: {captains['Enterprise']}")
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    print(f"Discovery: {captains['Discovery']}")
else:
    captains["Discovery"] = "unknown"

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

del captains["Discovery"]
print(captains)

captains = dict()
print(captains)
captains = (("Enterprise", "Picard"), ("Voyager", "Janeway"), ("Defiant", "Sisko"))
captains = dict(captains)
print(type(captains))

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau', 
    'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 
    'California': 'Sacramento', 
    'Colorado': 'Denver', 
    'Connecticut': 'Hartford', 
    'Delaware': 'Dover', 
    'Florida': 'Tallahassee', 
    'Georgia': 'Atlanta',
}

choice_1 = random.choice(list(capitals_dict))
choice_2 = capitals_dict[choice_1]
user_in1 = input(f"What is the capital of {choice_1}?: ")
while user_in1.lower() != choice_2.lower():
    if user_in1.lower() == "exit":
        print("Goodbye.")
        break
    else:
        user_in1 = input("Incorrect. Please try again: ")
if user_in1.lower() == choice_2.lower(): print("Correct!")
print(list(capitals_dict.items()))

# Challenge - Cats with Hats
# Initially, all cats do not have hats
cats_hat = {each: False for each in range(1,11)}

# Iterate through 100 rounds
for iteration in range(1, 11):
    print(f"\nIteration {iteration}:")
    for cat in cats_hat:
        if cat >= iteration:
            if cat % iteration == 0:
                cats_hat[cat] = not cats_hat[cat]
                print(f"Changed the hat status of cat {cat}.")
        else:
            continue
    
    for cat, hat in cats_hat.items():
        if hat:
            print(f"Cat {cat} has a hat.")
    