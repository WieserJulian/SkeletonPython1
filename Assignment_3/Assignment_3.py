#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.10.18 to Present.
#    * All rights are reserved
#  ==================================================
import io
import unittest
from imp import reload
from unittest.mock import patch


class Assignment_3(unittest.TestCase):

    def test_ex1(self):
        solve_text = "   0 1 2 3\n" \
                     "  --------\n" \
                     "0| 1 0 0 0\n" \
                     "1| 0 1 0 0\n" \
                     "2| 0 0 1 0\n"
        with unittest.mock.patch('builtins.input', side_effect=[3, 4]):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a3_ex1")
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """   0 1 2 3 4 5 6 7 8 9
  --------------------
0| 1 0 0 0 0 0 0 0 0 0
1| 0 1 0 0 0 0 0 0 0 0\n"""
        with unittest.mock.patch('builtins.input', side_effect=[2, 10]):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """   0 1 2 3 4 5 6 7 8 9
  --------------------
0| 1 0 0 0 0 0 0 0 0 0
1| 0 1 0 0 0 0 0 0 0 0
2| 0 0 1 0 0 0 0 0 0 0
3| 0 0 0 1 0 0 0 0 0 0
4| 0 0 0 0 1 0 0 0 0 0
5| 0 0 0 0 0 1 0 0 0 0
6| 0 0 0 0 0 0 1 0 0 0
7| 0 0 0 0 0 0 0 1 0 0
8| 0 0 0 0 0 0 0 0 1 0
9| 0 0 0 0 0 0 0 0 0 1\n"""
        with unittest.mock.patch('builtins.input', side_effect=[10, 10]):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex1"))
        self.assertEqual(solve_text, stdout.getvalue())

    def test_ex2(self):
        solve_text = """all: []
unique (sorted): []
"""
        with unittest.mock.patch('builtins.input', side_effect=['x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a3_ex2")
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """all: ['hi', 'hello', 'hello', 'abc', 'test', 'python', 'hi', 'abc']
unique (sorted): ['abc', 'hello', 'hi', 'python', 'test']
"""
        with unittest.mock.patch('builtins.input',
                                 side_effect=['hi', 'hello', 'hello', 'abc', 'test', 'python', 'hi', 'abc', 'x']):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex2"))
        self.assertEqual(solve_text, stdout.getvalue())

    def test_ex3(self):
        solve_text = """'test' -> 448
"""
        with unittest.mock.patch('builtins.input', return_value='test'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a3_ex3")
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """'test' -> 448
"""
        with unittest.mock.patch('builtins.input', return_value='test,test,test'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex3"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """'a' -> 97
'b' -> 98
'ab' -> 195
'hello' -> 532
'holle' -> 532
'ba' -> 195
"""
        with unittest.mock.patch('builtins.input', return_value='a,b,ab,hello,holle,ba'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex3"))
        self.assertEqual(solve_text, stdout.getvalue())

    def test_ex4(self):
        solve_text = """integers: []
counts: {}
rest: ['test']
"""
        with unittest.mock.patch('builtins.input', return_value='test'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                __import__("a3_ex4")
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """integers: [512]
counts: {512: 1}
rest: []
"""
        with unittest.mock.patch('builtins.input', return_value='512'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex4"))
        self.assertEqual(solve_text, stdout.getvalue())

        solve_text = """integers: [1, 1, 12, 1, 5, 1, 5]
counts: {1: 4, 12: 1, 5: 2}
rest: ['abc', 'hello']
"""
        with unittest.mock.patch('builtins.input', return_value='abc,1,1,12,hello,1,5,1,5'):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a3_ex4"))
        self.assertEqual(solve_text, stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
