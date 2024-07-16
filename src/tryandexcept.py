try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Division by zero")


def decorate(func):
    def wrapper(*args, **kwargs):
        print("**********")
        print(func(*args, **kwargs))
        print("**********")

    return wrapper


@decorate
def show_name():
    return "Janet my baby girl"


print(show_name())
