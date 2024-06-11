import unittest

from python_programs import *


class MyTestCase(unittest.TestCase):
    def test_the_average_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(3.0, average_numbers(numbers))  # add assertion here

    def test_the_third_element_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEqual(18, multiply_the_third_elements(numbers))  # add assertion here

    def test_the_odd_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(9, odd_numbers(numbers))  # add assertion here

    def test_the_even_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(6, even_numbers(numbers))  # add assertion here

    def test_the_length_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(5, length_of_numbers(numbers))  # add assertion here

    def test_the_largest_of_the_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(5, largest_of_numbers(numbers))  # add assertion here

    def test_the_smallest_of_the_numbers(self):
        numbers = [9, 2, 3, 4, 5]
        self.assertEqual(2, smallest_of_numbers(numbers))  # add assertion here

    def test_the_length_of_a_string(self):
        words = ["dad", "semi", "ii"]
        self.assertEqual(["dad"], length_of_strings(words))

    def test_numbers_in_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], numbers_in_a_list())

    def test_duplicate_of_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], numbers_in_a_list_without_duplicate(numbers))

    def test_numbers_are_do_not_appear_twice(self):
        numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        self.assertEqual({1, 2, 3, 4, 5}, test_number_to_not_appear_twice(numbers))

    def test_the_sum_of_the_third_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(18, test_the_addition_of_third_numbers(numbers))

    def test_that_the_sum_of_the_first_middle_last(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(16, the_sum_of_the_first_middle_last(numbers))

    def test_the_length_of_numbers_in_a_set(self):
        numbers = (1, 2, 3, 4, 5)
        self.assertEqual(5, length_of_a_set(numbers))

    def test_the_addition_of_two_sets(self):
        first_set = (2, 1, 4, 3)
        second_set = (1, 6, 8, 3)
        self.assertEqual({1, 2, 3, 4, 6, 8}, addition_of_two_sets(first_set, second_set))

    def test_if_the_first_set_is_a_subset_of_the_second(self):
        super_set = (1, 3)
        second_set = (1, 6, 8, 3)
        self.assertTrue(check_if_the_first_set_is_a_subset_of_the_second(super_set, second_set))

    def test_the_tuple_is_empty(self):
        self.assertEqual((), create_an_empty_Tuple())

    def test_add_numbers_in_a_tuple(self):
        numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        self.assertEqual(numbers, add_numbers_in_a_tuple(numbers))

    def test_odd_numbers_in_a_tuple(self):
        numbers = (1, 2, 3, 4, 5)
        self.assertEqual(6, add_the_odd_numbers(numbers))

    def test_even_numbers_in_a_tuple(self):
        numbers = (1, 2, 3, 4, 5)
        self.assertEqual(9, add_the_even_numbers(numbers))

    def test_add_the_smallest_and_the_largest(self):
        numbers = (2, 8, 3, 4, 10)
        self.assertEqual(12, add_the_smallest_and_the_largest_in_tuple(numbers))

    def test_unpacking_elements_in_a_tuple(self):
        numbers = (1, 2, 3, 4, 5)
        self.assertEqual(unpacking_elements_in_a_tuple(numbers))

    def test_check_if_the_dictionary_is_empty(self):
        self.assertEqual({}, check_if_the_dictionary_is_empty())

    def test_adding_values_in_a_dictionary(self):
        self.assertEqual(10, len(adding_values_in_a_dictionary()))

    def test_collection_of_numbers(self):
        numbers = (1, 4, 2, 3, 4, 5, 6, 1)
        self.assertEqual({1, 2, 3, 4, 5, 6}, collection_of_numbers(numbers))

    def test_addition_collection_of_numbers(self):
        numbers = (1, 4, 2, 3, 4, 5, 6, 1)
        self.assertEqual(21, addition_collection_of_numbers(numbers))

    def test_remove_all_elements_in_the_first_set(self):
        first_set = (1, 2, 3, 4, 5)
        self.assertEqual(set(), remove_all_elements_in_the_first_set(first_set))

    def test_remove_only_the_elements_in_the_first_set(self):
        first_set = (1, 2, 3, 4, 5)
        second_set = (9, 8, 6, 3, 2, 1)
        self.assertEqual((None, {9, 8, 6, 3, 2, 1}), remove_only_the_elements_in_the_first_set(first_set, second_set))
