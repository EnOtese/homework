from runner_and_tournament import Runner
from runner_and_tournament import Tournament
from unittest import TestCase
import unittest


def skip_frozen(func):
    def wrapper(*args, **kwargs):
        if args[0].is_frozen:
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return func(*args, **kwargs)
    return wrapper


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Usain", 10)
        self.Andrey = Runner("Andrey", 9)
        self.Nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        #for i, a in TournamentTest.all_results.items():
        #print(i, a)
        pass

    @skip_frozen
    def test0(self):
        a = Tournament(90, self.Usain, self.Nick)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")

    @skip_frozen
    def test1(self):
        a = Tournament(90, self.Andrey, self.Nick)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")

    @skip_frozen
    def test2(self):
        a = Tournament(90, self.Usain, self.Nick, self.Andrey)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")


class RunnerTest(TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):
        r = Runner(self)
        for a in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @skip_frozen
    def test_run(self):
        r = Runner(self)
        for a in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @skip_frozen
    def test_challenge(self):
        r1 = Runner(self)
        r2 = Runner(self)
        for a in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__name__':
    unittest.main()
