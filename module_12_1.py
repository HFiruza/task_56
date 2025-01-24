import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        jump = Runner.Runner('бегать')
        for _ in range(10):
            jump.walk()
        self.assertEqual(jump.distance, 50)

    def test_run(self):
        to_go = Runner.Runner('ходить')
        for _ in range(10):
            to_go.run()
        self.assertEqual(to_go.distance, 100)

    def test_challenge(self):
        jump_2 = Runner.Runner('бежим')
        to_go_2 = Runner.Runner('ходим')
        for _ in range(10):
            jump_2.walk()
            to_go_2.run()
        self.assertNotEqual(to_go_2.distance, jump_2.distance)


if __name__ == '__main__':
    unittest.main()