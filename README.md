# Summative_Python

📘 README – FULL PRACTICE SET (30 QUESTIONS)
🎯 Goal

Implement or fix all functions.

You must:

Return correct values (no unnecessary prints)
Handle edge cases
Pass ALL unit tests
🧩 QUESTIONS
🔹 BASICS (1–10)
1. sum_to_n(n)

Return sum from 1 → n

2. count_even(numbers)

Return how many even numbers exist

3. find_max(numbers)

Return largest number

4. reverse_string(text)

Reverse a string

5. is_palindrome(word)

Return True if palindrome

6. remove_duplicates(lst)

Return list without duplicates

7. factorial(n)

Return factorial of n

8. fizz_buzz_variant(n)
3 → "Fizz"
5 → "Buzz"
both → "FizzBuzz"
9. sum_list(lst)

Return sum of list

10. find_min(lst)

Return smallest value

🔹 INTERMEDIATE (11–20)
11. filter_odds(lst)

Return only odd numbers

12. count_vowels(text)

Return number of vowels

13. merge_lists(a, b)

Merge two lists

14. word_count(sentence)

Return number of words

15. square_numbers(lst)

Return list of squares

16. find_index(lst, value)

Return index or -1

17. flatten_list(lst)

Flatten nested list (1 level)

18. common_elements(a, b)

Return common elements

19. dict_sum_values(d)

Sum all dictionary values

20. invert_dict(d)

Swap keys and values

🔹 ADVANCED (21–30)
21. longest_word(sentence)

Return longest word

22. char_frequency(text)

Return dict of character counts

23. second_largest(lst)

Return second largest number

24. prime_check(n)

Return True if prime

25. fibonacci_list(n)

Return first n Fibonacci numbers

26. group_by_even_odd(lst)

Return:

{"even": [...], "odd": [...]}
27. batch_process(lst, size)

Split into chunks

28. running_total(lst)

Return cumulative sum list

29. inventory_runout(stock, sales)

Return day stock runs out

30. password_checker(password)

Return:

Weak
Medium
Strong
🐞 DEBUGGING SECTION (VERY IMPORTANT)
31. Fix this:
def buggy_sum(n):
    total = 0
    for i in range(n):
        total =+ i
    return total
32. Fix this:
def buggy_even(lst):
    result = []
    for i in lst:
        if i % 2 = 0:
            result.append(i)
    return result
33. Fix this:
def buggy_max(lst):
    max = 0
    for i in lst:
        if i > max:
            max == i
    return max
34. Fix this:
def buggy_factorial(n):
    if n == 0:
        return 0
    return n * buggy_factorial(n-1)
35. Fix this:
def buggy_password(p):
    if len(p) > 6:
        return "Strong"
    elif len(p) > 3:
        return "Medium"
    return "Weak"