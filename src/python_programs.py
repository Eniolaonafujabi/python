def get_the_length_of_your_word(word):
    if type(word) in [int, float]:
        raise TypeError("argument must be an iterable")
    count = 0
    for _ in word:
        count += 1
    return count


def sum_up_all_the_even_element_in_a_list(a_list):
    num = 0
    if type(a_list) in [str,bool]:
        raise TypeError("argument must be an iterable")
    for number in a_list:
        if number % 2 == 0:
            num += number
        return num

def sum_up_all_odd_element_in_a_list(a_list):
    num = 0
    if type(a_list) in [str,bool]:
        raise TypeError("argument must be an iterable")
    number: int
    for number in a_list:
        if number % 2 == 1:
            num += number
        return num

def cal_the_average_of_all_elements_in_a_list(a_list):
    average = 0
    if type(a_list) in [str,bool]:
        raise TypeError("argument must be an iterable")
    total = 0
    for number in a_list:
        total += number
    average = total / len(a_list)
    return average

def multiply_every_third_position_in_a_list(a_list):
    multiplied = 0
    count = 0
    while count < len(a_list):
        multiplied * a_list[count]
        count += 3
    return multiplied

def get_the_largest_element_in_a_list(a_list):
    largest = a_list[0]
    for number in a_list:
        if number < largest:
            largest = number
    return largest

def get_the_smallest_element_in_list(a_list):
    smallest = a_list[0]
    for number in a_list:
        if number > smallest:
            smallest = number
    return smallest

def __getattr__(name):
    pass
