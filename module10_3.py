import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            ran = random.randint(50, 500)
            time.sleep(0.001)
            self.balance += ran
            if self.balance >= 500 and self.lock == self.lock.locked():
                self.lock.release()
                time.sleep(0.001)
                print(f'Пополнение: {ran}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            ran = random.randint(50, 500)
            print(f'Запрос на {ran}')
            time.sleep(0.001)
            if ran <= self.balance:
                self.balance -= ran
                time.sleep(0.001)
                print(f"Снятие: {ran}. Баланс: {self.balance}")
            elif ran > self.balance:
                print("Запрос отклонён, недостаточно средств")
                time.sleep(0.001)
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
