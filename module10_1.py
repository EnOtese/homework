import threading
import time
import datetime

time_start_func = datetime.datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f'Какое-то слово №{i}' + '\n')
        print(f'Завершилась запись в файл {file_name}')


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end_func = datetime.datetime.now()
time_res_func = time_end_func - time_start_func
print(f'Работа потоков: {time_res_func}')
time_start_thr = datetime.datetime.now()

thr_1 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thr_2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thr_3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thr_4 = threading.Thread(target=write_words, args=(100, "example8.txt"))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end_thr = datetime.datetime.now()
time_res_thr = time_end_thr - time_start_thr
print(f'Работа потоков: {time_res_thr}')