class WordsFinder():
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                for line in file:
                    rem_obj = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for obj in rem_obj:
                        line = line.replace(obj, '')
                    words = file.split()
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            position = words.index(word.lower())
            result[name] = position + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word.lower())
            result[name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
