def get_the_length_of_your_word(word):
    if type(word) in [int, float]:
        raise TypeError("argument must be an iterable")
    count = 0
    for _ in word:
        count += 1
    return count
