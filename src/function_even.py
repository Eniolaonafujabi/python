def func_that_give_even_number(passed_in_list: list) -> list:
    even: list = []
    for number in passed_in_list:
        if number % 2 == 0:
            even.append(number)
    return even

def even_list2(numbers):
    return [number for number in numbers if number % 2 == 0]

number_passed_to_the_list = list(range(1, 51))
number_to_be_passed = list(range(51))
# for number_needed in range(51):
#     number_passed_to_the_list.append(number_needed)
print(func_that_give_even_number(number_passed_to_the_list))
print(even_list2(number_to_be_passed))
