data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(arg):
    sum_ = 0
    if isinstance(arg, set):
        for i in arg:
            sum_ += calculate_structure_sum(i)
    if isinstance(arg, list):
        for i in arg:
            sum_ += calculate_structure_sum(i)
    elif isinstance(arg, dict):
        for key, value in arg.items():
            sum_ += len(key)
            sum_ += calculate_structure_sum(value)
    elif isinstance(arg, tuple):
        for i in arg:
            sum_ += calculate_structure_sum(i)
    elif isinstance(arg, str):
        sum_ += len(arg)
    elif isinstance(arg, (int, float)):
        sum_ += arg

    return sum_


result = calculate_structure_sum(data_structure)
print(result)
