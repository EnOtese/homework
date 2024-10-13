import multiprocessing
import datetime


def read_info(name):
    all_data = []
    for i in name:
        with open(i, 'r', encoding='utf-8') as file:
            all_data += file.readlines()
    return all_data


start1 = datetime.datetime.now()
if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    read_info(filenames)
end1 = datetime.datetime.now()
print(end1 - start1)

start2 = datetime.datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=5) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        map(read_info, filenames)
end2 = datetime.datetime.now()
print(end2 - start2)
