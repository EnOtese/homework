def is_prime(func):
    def wrapper(a, b, c):
        result_ = func(a, b, c)
        if result_ <= 1:
            return "Составное" + f'\n{result_}'
        for i in range(2, int(result_**0.5) + 1):
            if result_ % i == 0:
                return "Составное" + f'\n{result_}'
        return "Простое" + f'\n{result_}'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
