#  ==================================================
#    * Copyright (c) 2023 Julian Wieser to Present.
#    * All rights are reserved
#  ==================================================

import io
import unittest
from unittest.mock import patch
from importlib import reload


class Assignment_2(unittest.TestCase):

    def test_ex1(self):
        solve_text = "Invalid subscription duration\n"
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('builtins.input', return_value='-1'):
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                    reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "Invalid subscription duration\n"
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('builtins.input', return_value='0'):
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                    reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "The price per month is 6.50\nThe full price for 4 months is 26.00\n"
        with unittest.mock.patch('builtins.input', side_effect=['4']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a2_ex1")
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "The price per month is 5.90\nThe full price for 10 months is 59.00\n"
        with unittest.mock.patch('builtins.input', return_value='10'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "Invalid postal code\n"
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('builtins.input', return_value='123'):
                with unittest.mock.patch('builtins.input', return_value='14'):
                    with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                        reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "Invalid postal code\n"
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('builtins.input', return_value='12345'):
                with unittest.mock.patch('builtins.input', return_value='14'):
                    with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                        reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = "The price per month is 4.02\nThe full price for 14 months is 56.28\n"
        with unittest.mock.patch('builtins.input', side_effect=['14', '4020']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

    def test_ex2(self):
        solve_text = "Empty sequence\n"
        with unittest.mock.patch('builtins.input', side_effect=['x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a2_ex2")
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "All numbers had the same digit in the ones place\n"
        with unittest.mock.patch('builtins.input', side_effect=['12', 'x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex2"))
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = solve_text = "All numbers had the same digit in the ones place\n"
        with unittest.mock.patch('builtins.input', side_effect=['12', '622', '502', 'x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex2"))
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "622 and 47 differ in the ones place\n"
        with unittest.mock.patch('builtins.input', side_effect=['12', '622', '47', 'x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex2"))
        self.assertEqual(stdout.getvalue(), solve_text)

    def test_ex3(self):
        solve_text = "Even number count = 0\nSum of odd numbers = 0\n"
        with unittest.mock.patch('builtins.input', side_effect=['3', '2', '1']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a2_ex3")
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "Number in iteration 0 = 0\nNumber in iteration 1 = 2\nNumber in iteration 2 = 4\nNumber in iteration 3 = 6\nNumber in iteration 4 = 8\nEven number count = 5\nSum of odd numbers = 0\n"
        with unittest.mock.patch('builtins.input', side_effect=['0', '10', '2']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex3"))
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "Number in iteration 0 = 1\nNumber in iteration 1 = 5\nNumber in iteration 2 = 9\nEven number count = 0\nSum of odd numbers = 15\n"
        with unittest.mock.patch('builtins.input', side_effect=['1', '10', '4']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex3"))
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "Number in iteration 0 = 10\nNumber in iteration 1 = 13\nNumber in iteration 2 = 16\nNumber in iteration 3 = 19\nNumber in iteration 4 = 22\nEven number count = 7\nSum of odd numbers = 217\n"
        with unittest.mock.patch('builtins.input', side_effect=['10', '50', '3']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex3"))
        self.assertEqual(stdout.getvalue(), solve_text)

    def test_ex4(self):
        solve_text = "---\n| |\n---\n"
        with unittest.mock.patch('builtins.input', side_effect=['3']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a2_ex4")
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "-----\n|   |\n|   |\n|   |\n-----\n"
        with unittest.mock.patch('builtins.input', side_effect=['5']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex4"))
        self.assertEqual(stdout.getvalue(), solve_text)

        solve_text = "-------\n|     |\n|     |\n|     |\n|     |\n|     |\n-------\n"
        with unittest.mock.patch('builtins.input', side_effect=['7']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a2_ex4"))
        self.assertEqual(stdout.getvalue(), solve_text)


if __name__ == '__main__':
    unittest.main()
