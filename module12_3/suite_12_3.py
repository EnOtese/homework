from tests_12_3 import TournamentTest
from tests_12_3 import RunnerTest
import unittest

TEST = unittest.TestSuite()
TEST.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
TEST.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TEST)