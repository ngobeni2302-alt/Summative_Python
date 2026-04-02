# ============================
# BASICS (1–10)
# ============================

def sum_to_n(n: int) -> int:
    sum = 0

    for i in range(n + 1):
        sum += i
    return sum

def count_even(numbers: list) -> int:
    even_count = 0
    for i in numbers:
        if i % 2 == 0:
            even_count += 1
    return even_count

def find_max(numbers: list) -> int:
    largest = 0

    for number in numbers:
        if number > largest:
            largest = number
    return largest

def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(word: str) -> bool:
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


def remove_duplicates(lst: list) -> list:
    new_lst = set()

    for i in lst:
        new_lst.add(i)
    return list(new_lst)


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fizz_buzz_variant(n: int) -> list:
    """
    3 → "Fizz"
5 → "Buzz"
both → "FizzBuzz"
    """
    new_lst = []
    for i in range(n + 1):
        if i % 3 == 0 and i % 5 == 0:
            new_lst.append("FizzBuzz")
        elif i % 3 == 0:
            new_lst.append("Fizz")
        elif i % 5 == 0:
            new_lst.append("Buzz")
        else:
            new_lst.append(i)
    return new_lst


def sum_list(lst: list) -> int:
    return sum(lst)


def find_min(lst: list) -> int:
    for i in lst:
        lowest = i
        for x in lst:
            if x < i:
                lowest = x
    return lowest


# ============================
# INTERMEDIATE (11–20)
# ============================

def filter_odds(lst: list) -> list:
    odd_list = []

    for i in lst:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


def count_vowels(text: str) -> int:
    vowel_count = 0
    text = text.lower()
    for i in text:
        if i in "aieou":
            vowel_count += 1
    return vowel_count


def merge_lists(a: list, b: list) -> list:
    return (a + b)


def word_count(sentence: str) -> int:
    count = 0

    sentence = sentence.split()

    for i in sentence:
        count += 1
    return count 


def square_numbers(lst: list) -> list:
    squared_numbers = []

    for i in lst:
        squared_numbers.append(i * i)

    return squared_numbers


def find_index(lst: list, value) -> int:
    return lst.index(value)


def common_elements(a: list, b: list) -> list:
    common_list = []

    for i in a:
        for x in b:
            if i == x:
                common_list.append(x)
    return common_list


def dict_sum_values(d: dict) -> int:
    sum = 0
    for key, value in d.items():
        sum += value
    return sum 


def invert_dict(d: dict) -> dict:
    new_dict = {}

    for key, value in d.items():
        new_dict[value] = key
    return new_dict


# ============================
# ADVANCED (21–30)
# ============================
def prime_check(n: int) -> bool:
    
    for i in range(n):
        if i != 0 and i != 1 and n % i == 0:
            return False
    return True


def fibonacci_list(n: int) -> list:
    fibo = [0,1]

    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


def group_by_even_odd(lst: list) -> dict:
    dict = {}
    lst1 =[]
    for i in lst:
        if i % 2 == 0:
            lst1.append("even")
        else:
            lst1.append("odd")
        
        for x in lst1:
            if x not in dict:
                dict[x] = []
        dict[x].append(i)
    return dict
print(group_by_even_odd([3,2]))



def batch_process(lst: list, size: int) -> list:
    lis = []

    for i in range(0, len(lst), size):
        lis.append(lst[i : i + size])
    return lis
