# Inputs 2 lists of lists compared against each other
# list can be empty of contain a minimum of 1 array of 2 integers to maximum of 100 arrays
# if array contains only 1 integer > exit, display invalid input
# if array contains more than 1 integer > exit, display invalid input
# if list contains more than 100 arrays > exit, display maximum input

def same(arr_a, arr_b):
    is_arr_ok = check_arr_size(arr_a) and check_arr_size(arr_b)
    
    if is_arr_ok:
        if len(arr_a) == 0:
            return f"{arr_a} and {arr_b} are the same"
        elif len(arr_a) != len(arr_b):
            return f"arr_a and arr_b are not the same, different sizes"
        else:
            arr_b_check = [1] * len(arr_b)
            for i in range(len(arr_a)):
                for j in range(len(arr_b)):
                    if arr_a[i].sort() == arr_b[j].sort():
                        arr_b_check[j] = 0
                        continue
            if sum(arr_b_check) > 0:
                return f"sum > 0 {arr_a} and {arr_b} are not the same"
            else:
                return f"{arr_a} and {arr_b} are the same"
    else:
        return "invalid input"
        

def check_arr_size(arr_in):
    if len(arr_in) == 0:
        is_useable = True
    else:
        if len(arr_in) > 100:
            print("Exiting due to max array input...cannot compare more than 100 arrays")
            is_useable = False
        else:
            is_useable = True
            for each in arr_in:
                if len(each) != 2:
                    print("Exiting due to invalid input...one of the arrays have less or more than 2 integers")
                    is_useable = False
                    break
    return is_useable

def sect_sort(sort_list, ind_start, *opt_end):
    ind_end = len(sort_list) if not opt_end else ind_start+opt_end[0]
    new_list = sorted(sort_list[ind_start:ind_end])
    sort_list[ind_start:ind_end] = new_list
    print(sort_list)


def distances_from_average(test_list):
    average = sum(test_list) / len(test_list)
    dist_list = list(map(lambda value: average - value, test_list))
    dist_list = [round(each, 2) for each in dist_list]
    return dist_list

print(distances_from_average([55, 95, 62, 36, 48]))

def duplicate_count(text):
    unique_list = list(set(text))
    count_list = [text.count(each) for each in unique_list]
    return sum(1 for each in count_list if each > 1)

rawtext_color = """Abbreviation        Color 
AL                  Aluminum 
AM                  Amber 
BG                  Beige 
BK                  Black 
BL                  Blue 
BN                  Brown 
BZ                  Bronze 
CH                  Charcoal 
CL                  Clear 
GD                  Gold 
GN                  Green 
GY                  Gray 
GT                  Granite 
IV                  Ivory 
LT                  Light  
OL                  Olive 
OP                  Opaque 
OR                  Orange 
PK                  Pink 
RD                  Red 
SM                  Smoke 
TL                  Translucent 
TN                  Tan 
TP                  Transparent 
VT                  Violet 
WT                  White 
YL                  Yellow"""
dict_color = [line.split() for line in rawtext_color.split("\n")]
dict_color = dict(dict_color)

import math

def find_prob(balls_set, event):
    # Identify equation parameters
    total_balls = len(balls_set)
    color_list  = [dict_color[key] for key in list(set(event))]
    total_color = dict([[each,balls_set.count(each)] for each in color_list])
    prob_n = 1
    prob_d = 1

    # Find the probability:
    for each in event:
        if dict_color[each] in total_color:
            if total_color[dict_color[each]] > 0:
                prob_n = prob_n * total_color[dict_color[each]]
                prob_d = prob_d * total_balls
                total_color[dict_color[each]] -= 1
                total_balls -= 1
        else:
            return("Impossible")
    return (list(map(lambda result: result // math.gcd(prob_n, prob_d), [prob_n, prob_d])))


balls1 = ["Red","Red","Blue","Yellow","Yellow","Yellow","Red", "Yellow","Yellow","Blue","Yellow","Red","Blue","Yellow","Blue","Yellow","Blue","Yellow"]
e1 =["RD", "YL", "YL", "BL"]
print(find_prob(balls1, e1))

with open('practice_input_output.txt', "r") as txt_f:
    sample = txt_f.read()
    sample = sample.split()
    sample = list(map(lambda string1:  string1 + "0", sample))
    print(sample)

import json
with open("practice_input_output.json", "r") as jf_1:
    data = json.load(jf_1)
    print(data)


hello = ((1,2), (1,2))
print(hello[0][0])