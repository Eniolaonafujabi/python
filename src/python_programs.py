import random
from os import remove


def random_numbers(numbers):
    for num in range(10):
        return random.randrange(1, 50)


for num in range(11):
    print(random_numbers(random.randrange(1, 50)))


def average_numbers(numbers):
    counter = 0
    average_numbers = 0
    for count in numbers:
        counter = counter + 1
        sum = 0
    for num in numbers:
        sum = sum + num
        average_numbers = sum / counter
    return average_numbers


def multiply_the_third_elements(numbers):
    sum = 1
    for num in numbers:
        if num % 3 == 0:
            sum *= num
    return sum

def odd_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num % 2 == 1):
            odd = num
            sum += odd
    return sum


def even_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num % 2 == 0):
            even = num
            sum += even
    return sum


def length_of_numbers(numbers):
    counter = 0
    for count in numbers:
        counter = counter + 1
    return counter


def largest_of_numbers(numbers):
    largest = 0
    for num in numbers:
        if (num > largest):
            largest = num
    return largest


def smallest_of_numbers(numbers):
    smallest = numbers[0]
    for num in numbers:
        if (num < smallest):
            smallest = num
    return smallest


def length_of_strings(words_in_a_list):
    words = []
    counter = 0
    for word in words_in_a_list:
        if length_of_numbers(word) > 2:
            if word[0] == word[length_of_numbers(word) - 1]:
                words.append(word)
    return words


def numbers_in_a_list():
    numbers = []
    for count in range(1, 16):
        numbers.append(count)
    return numbers


def numbers_in_a_list_without_duplicate(numbers):
    numbers += numbers
    return numbers


def test_number_to_not_appear_twice(number):
    result = set(number)
    return result


def test_the_addition_of_third_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 3 == 0:
            sum += num
    return sum


def the_sum_of_the_first_middle_last(numbers):
    sum = 0
    middle_number = len(numbers) // 2
    last_number = len(numbers)
    sum = numbers[0] + middle_number + last_number
    return sum


def length_of_a_set(numbers):
    counter = 0
    for count in numbers:
        counter = counter + 1
    return counter


def addition_of_two_sets(first_set, second_set):
    first_set = set(first_set)
    second_set = set(second_set)
    return first_set.union(second_set)


def check_if_the_first_set_is_a_subset_of_the_second(first_set, second_set):
    super_set = set(first_set)
    second_set = set(second_set)
    return super_set.union(second_set)


def remove_all_elements_in_the_first_set(first_number):
    first_set = set(first_number)
    first_set.clear()
    return first_set

def remove_only_the_elements_in_the_first_set(first_number,second_number):
    first_set = set(first_number)
    second_set = set(second_number)
    result = first_set.union(second_set)
    removed_set = first_set.clear()
    return removed_set, second_set


def create_an_empty_Tuple():
    tuple = ()
    return tuple


def add_numbers_in_a_tuple(numbers):
    tuple = ()
    for count in range(20):
        tuple += numbers
        return tuple


def add_the_odd_numbers(numbers):
    odd = 0
    counter = 0
    for number in numbers:
        if counter % 2 == 1:
            odd += numbers[counter]
        counter += 1
    return odd


def add_the_even_numbers(numbers):
    even = 0
    counter = 0
    for number in numbers:
        if counter % 2 == 0:
            even += numbers[counter]
        counter += 1
    return even


def add_the_smallest_and_the_largest_in_tuple(numbers):
    smallest = numbers[0]
    largest = 0
    sum = 0
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        sum = largest + smallest
    return sum


def unpacking_elements_in_a_tuple(numbers):
    a, b, c, d, e = numbers
    return numbers


def check_if_the_dictionary_is_empty():
    dictionary = {}
    return dictionary


def adding_values_in_a_dictionary():
    names_of_students_and_age = {
        "Janet": 17,
        "Ade": 67,
        "make": 66,
        "Chiaki": 45,
        "Chinned": 89,
        "Kart": 15,
        "Chul": 22,
        "Bunch": 45,
        "Azeem": 90,
        "Gladiola": 12
    }
    return names_of_students_and_age


def collection_of_numbers(numbers):
    result = set(numbers)
    return result


def addition_collection_of_numbers(numbers):
    result = set(numbers)
    sum = set(result)
    final_result = result + sum
    return final_result