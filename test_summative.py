import unittest
from summative import *

class TestAll(unittest.TestCase):

    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_count_even(self):
        self.assertEqual(count_even([1,2,3,4]), 2)

    def test_find_max(self):
        self.assertEqual(find_max([1,5,2]), 5)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1,1,2]), [1,2])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_sum_list(self):
        self.assertEqual(sum_list([1,2,3]), 6)

    def test_find_min(self):
        self.assertEqual(find_min([3,1,2]), 1)

    def test_filter_odds(self):
        self.assertEqual(filter_odds([1,2,3]), [1,3])

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_merge(self):
        self.assertEqual(merge_lists([1],[2]), [1,2])

    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_square(self):
        self.assertEqual(square_numbers([2,3]), [4,9])

    def test_find_index(self):
        self.assertEqual(find_index([1,2,3],2), 1)

    def test_common(self):
        self.assertEqual(common_elements([1,2],[2,3]), [2])

    def test_dict_sum(self):
        self.assertEqual(dict_sum_values({"a":1,"b":2}), 3)

    def test_invert(self):
        self.assertEqual(invert_dict({"a":1}), {1:"a"})

    def test_prime(self):
        self.assertTrue(prime_check(7))

    def test_fibonacci(self):
        self.assertEqual(fibonacci_list(5), [0,1,1,2,3])

    def test_group(self):
        self.assertEqual(group_by_even_odd([1,2]), {"even":[2],"odd":[1]})

    def test_batch(self):
        self.assertEqual(batch_process([1,2,3,4],2), [[1,2],[3,4]])

    def test_running_total(self):
        self.assertEqual(running_total([1,2,3]), [1,3,6])

    def test_inventory(self):
        self.assertEqual(inventory_runout(10,[3,3,5]), "Day 3")

    def test_password(self):
        self.assertEqual(password_checker("abc123!"), "Strong")


if __name__ == "__main__":
    unittest.main()