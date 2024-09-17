def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    for i, s in enumerate(strings, start=1):
        cursor = file.tell()
        file.write(s + '\n')
        strings_positions[(i, cursor)] = s
    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text_file1.txt', info)
for elem in result.items():
    print(elem)
