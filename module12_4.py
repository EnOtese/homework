import logging
from unittest import TestCase
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(TestCase):
    def test_walk(self):
        try:
            r = Runner(name='Вася', speed=-5)
            if r.speed < 0:
                raise ValueError
            for a in range(10):
                r.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            r = Runner(2)
            if r.name != type(str):
                raise TypeError
            for a in range(10):
                r.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == '__name__':
    r1 = Runner("Вася", -5)
    r2 = Runner(2)
    unittest.main()
