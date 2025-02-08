
def findNum(num_list:list) -> int:
    if num_list:
        check_list = list(set(num_list))
        check_list = sorted(check_list)
        i = len(check_list) - 1
        while i > 0:
            if (check_list[i] - check_list [i-1]) != 1:
                return check_list[i-1] + 1
            i -= 1

def test_findNum() -> int:
    """Find the missing number in the list"""
    assert findNum([1,2,4,5]) == 3, "Missing number should be 3"
    assert findNum([0,0,1,3]) == 2, "Missing number should 2"
    assert findNum([-1,1,2]) == 1, "Missing number should be 1"

def isPalindrome(phrase: str) -> bool:
    """Check if input phrase palindrome"""
    clean_phrase = phrase.replace(" ", "").lower()
    rev_phrase = "".join(reversed(clean_phrase))

    return True if clean_phrase == rev_phrase else False

def countWords(tf) -> dict:
    with open (tf, "r") as text:
        word_list = text.read().lower().split()
        unq_words = list(set(word_list))
        dict_count = {}
        for each in unq_words:
            dict_count[each] = word_list.count(each)
        text.close()
    return dict_count

print(countWords("file2.txt"))

data = {"apple": 3, "banana": 1, "cherry": 2}

# Sort by values
sorted_dict = sorted(data.items(), key=lambda item: item[1])
print(sorted_dict)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3}
