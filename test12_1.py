from unittest import TestCase
from runner import Runner
import unittest


class RunnerTest(TestCase):
    def test_walk(self):
        r = Runner(self)
        for a in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runner(self)
        for a in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = Runner(self)
        r2 = Runner(self)
        for a in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
