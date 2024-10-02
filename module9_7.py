def is_prime(func):
    def wrapper(a, b, c):
        result_ = func(a, b, c)
        if result_ % result_ == 0 and result_ != 0:
            return "Простое" + f'\n{result_}'
        else:
            return "Составное" + f'\n{result_}'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
