#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.11.4 to Present.
#    * All rights are reserved
#  ==================================================

import unittest
import warnings


class Assignment4(unittest.TestCase):

    def test_a4_ex1(self):
        try:
            from a4_ex1 import split_list
            self.assertEqual([[0, 2], [1, 3]], split_list([0, 1, 2, 3], 2))
            self.assertEqual([[0, 1, 2, 3]], split_list([0, 1, 2, 3], 1))
            self.assertEqual([[0, 3, 6], [1, 4, 7], [2, 5]], split_list([0, 1, 2, 3, 4, 5, 6, 7], 3))
            self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], split_list([0, 1, 2, 3, 4, 5, 6, 7], 0))
            self.assertEqual([[0, 2, 4], [1, 3]], split_list([0, 1, 2, 3, 4], 2))
        except ModuleNotFoundError:
            warnings.warn("You need to put the a4_ex1.py in the same directory", ImportWarning)

    def test_a4_ex2(self):
        try:
            from a4_ex2 import clip
            self.assertEqual([], clip())
            self.assertEqual([1, 1, 0.1, 0], clip(1, 2, 0.1, 0))
            self.assertEqual([0, 0.5], clip(-1, 0.5))
            self.assertEqual([-1, 0.5], clip(-1, 0.5, min_=-2))
            self.assertEqual([0, 0.3], clip(-1, 0.5, max_=0.3))
            self.assertEqual([2, 2], clip(-1, 0.5, min_=2, max_=3))
        except ModuleNotFoundError:
            warnings.warn("You need to put the a4_ex2.py in the same directory", ImportWarning)

    def test_a4_ex3(self):
        try:
            from a4_ex3 import grade_calculator
            self.assertEqual((True, 3), grade_calculator([95, 100, 39, 13, 86, 71, 20, 100, 83, 100], None, 82))
            self.assertEqual((True, 2), grade_calculator([95, 100, 39, 13, 86, 71, 20, 100, 83, 100], 51, 82))
            self.assertEqual((False, 5), grade_calculator([0, 100, 100, 13, 100, 100, 20, 100, 100, 100], 0, 100))
            self.assertEqual((True, 2), grade_calculator([0, 100, 100, 13, 100, 100, 20, 100, 100, 100], 100, 100))
            self.assertEqual((True, 2), grade_calculator([0, 100, 100, 13, 100, 100, None, 100, 100, 100], 100, 100))
            self.assertEqual((False, 5), grade_calculator([100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 100, 49))
        except ModuleNotFoundError:
            warnings.warn("You need to put the a4_ex3.py in the same directory", ImportWarning)

    def test_a4_ex4(self):
        try:
            from a4_ex4 import round_
            self.assertEqual(778, round_(777.777))
            self.assertEqual(778.0, round_(777.777, 0))
            if len(str(round_(777.777, 1))) > len(str(777.777)):
                self.assertEqual(777.8, round_(777.8000000000001, 1), msg="Can also be 777.8000000000001")
            else:
                self.assertEqual(777.8, round_(777.777, 1), msg="Can also be 777.8000000000001")
            self.assertEqual(777.78, round_(777.777, 2))
            self.assertEqual(777.777, round_(777.777, 3))
            self.assertEqual(777.777, round_(777.777, 4))
        except ModuleNotFoundError:
            warnings.warn("You need to put the a4_ex4.py in the same directory", ImportWarning)

    def test_a4_ex5(self):
        try:
            from a4_ex5 import sort
            some_list = [1, 3, 0, 4, 5]
            sort(some_list)
            self.assertEqual([0, 1, 3, 4, 5], some_list, msg="Most likely you forgott that its an inplace operation"
                                                             " so only 'elements' is changed no new object is created")
            some_list = [1, 3, 0, 4, 5]
            sort(some_list, ascending=False)
            self.assertEqual([5, 4, 3, 1, 0], some_list)
        except ModuleNotFoundError:
            warnings.warn("You need to put the a4_ex5.py in the same directory", ImportWarning)


if __name__ == '__main__':
    unittest.main()
