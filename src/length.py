def get_the_length_of_your_word(word):
    if type(word) in [int, float]:
        raise TypeError("argument must be an iterable")
    count = 0
    for _ in word:
        count += 1
    return count


print(get_the_length_of_your_word("eniola"))
print(get_the_length_of_your_word("eniola_janet"))
print(get_the_length_of_your_word([1, 4, 6, 7, 8, 9, 5]))
