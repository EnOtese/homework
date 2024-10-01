import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

l_func = list(map(lambda x, y: x == y, first, second))

print(l_func)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.wor = words

    def __call__(self):
        return random.choice(self.wor)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
