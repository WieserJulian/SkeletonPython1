#  ==================================================
#    * Copyright (c) 2023 Julian Wieser to Present.
#    * All rights are reserved
#  ==================================================

import io
import unittest
from unittest.mock import patch


class Assignment_1(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ex1(self, stdout):
        solveText = "True\n" \
                    "00012\n" \
                    "     1.500\n" \
                    "hellohellohello\n"
        import a1_ex1
        a1_ex1
        self.assertEqual(solveText, stdout.getvalue())

    @patch('sys.stdin', io.StringIO('20\n19\n18\n17\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ex2(self, stdout):
        solve_text = "a: " \
                     "b: " \
                     "c: " \
                     "d: " \
                     "Sum of a, b and d: 56\n" \
                     "Product of all numbers: 116280\n" \
                     "The sum of a and b times the sum of c and d: 1365\n" \
                     "a divided by d (int): 1\n" \
                     "a divided by d (float): 1.1764705882352942\n" \
                     "Remainder of a divided by b: 1\n" \
                     "c to the power of -a: 7.844222393007239e-26\n" \
                     "b to the power of 1/2 (square root): 4.358898943540674\n" \
                     "Complex equation: 1.7624222759183791e+37\n"
        import a1_ex2
        a1_ex2
        self.assertEqual(solve_text, stdout.getvalue())

    @patch('sys.stdin', io.StringIO('5.6\n4.5\n2.7\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ex3(self, stdout):
        solve_text = "Length (meters): " \
                     "Width (meters): " \
                     "Height (meters): " \
                     "Circumference: 20.20 meters\n" \
                     "Volume: 68.04 cubic meters\n" \
                     "Wall area: 54.54 square meters\n" \
                     "Number of windows: 4\n" \
                     "Needed paint: 34.91 liters\n"
        import a1_ex3
        a1_ex3
        self.assertEqual(solve_text, stdout.getvalue())

    @patch('sys.stdin', io.StringIO('25\n5\n20\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ex4(self, stdout):
        solve_text = "==================================================\n" \
                     "PC Parts Store - Order\n" \
                     "==================================================\n" \
                     "Number of cables: " \
                     "Number of monitors: " \
                     "Number of keyboards: " \
                     " 25 cables (9.90 EUR each) = 247.50 EUR\n" \
                     "  5 monitors (249.99 EUR each) = 1249.95 EUR\n" \
                     " 20 keyboards (27.50 EUR each) = 550.00 EUR\n" \
                     "--------------------------------------------------\n" \
                     "Total: 2047.45 EUR\n" \
                     "==================================================\n"
        import a1_ex4
        a1_ex4
        self.assertEqual(solve_text, stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
