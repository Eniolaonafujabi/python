number_varies_after_getting_next_result = 0
number_varies_to_the_last_digit_use_to_add = 1
count = 0
temp_varable = 0
print(f'{number_varies_after_getting_next_result} ', end='')
print(f'{number_varies_to_the_last_digit_use_to_add}  ', end='')
while count<9:
    temp_varable = number_varies_to_the_last_digit_use_to_add
    number_varies_to_the_last_digit_use_to_add += number_varies_after_getting_next_result
    print(f'{number_varies_to_the_last_digit_use_to_add} ',end='')
    number_varies_after_getting_next_result = temp_varable
    count+=1
