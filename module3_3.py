def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(False, "Мистер")
print_params(c=[1, 2, 3])
print_params(b=25)

values_list = [14, "Input", False]
values_dict = {'a': '4', 'b': True, 'c': 0.5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Ботинок', 41]
print_params(*values_list_2, 42)