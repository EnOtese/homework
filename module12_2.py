from runner_and_tournament import Runner
from runner_and_tournament import Tournament
from unittest import TestCase
import unittest


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Usain", 10)
        self.Andrey = Runner("Andrey", 9)
        self.Nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for i, a in TournamentTest.all_results.items():
            print(i, a)

    def test0(self):
        a = Tournament(90, self.Usain, self.Nick)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")


    def test1(self):
        a = Tournament(90, self.Andrey, self.Nick)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")


    def test2(self):
        a = Tournament(90, self.Usain, self.Nick, self.Andrey)
        TournamentTest.all_results = Tournament.start(a)
        self.assertTrue(self.all_results[max(self.all_results)] == "Nick")


if __name__ == '__name__':
    unittest.main()
