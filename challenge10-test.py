#!env python3.7

import unittest
from challenge10 import ch10, describe_the_number


class MyFirstTests(unittest.TestCase):
    a = [1, 11, 21, 1211, 111221]
    b = [1, 11, 21, 1211, 111221, 1012211, 1110112221]


    def test_part1(self):
        for ii in range(2):
            self.a.append(ch10(self.a[-1]))
            print(f"{ii}: a has {len(self.a)} elements, last has length {len(self.a[-1])}")

        self.assertEqual(int(self.a[5]), self.b[5])

    # def test_part2(self):
    #     self.assertEqual(part2(self.test_input), 4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
