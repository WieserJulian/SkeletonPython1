#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.11.8 to Present.
#    * All rights are reserved
#  ==================================================
import io
import os.path
import unittest
import unittest.mock
import warnings


class Assignment_5(unittest.TestCase):
    def test_a5_ex1(self):
        try:
            from a5_ex1 import sub_summarize
            nested = [1, 2, 3, [4, [5, 6], 7], 8, [9, 10]]
            sub_sums = []
            result = sub_summarize(nested, sub_sums)
            self.assertEqual([11, 22, 19, 55], sub_sums)
            self.assertEqual(55, result)
        except ModuleNotFoundError:
            warnings.warn("You need to put the a5_ex1.py in the same directory", ImportWarning)

    def test_a5_ex2(self):
        try:
            from a5_ex2 import print_directory
            path = r"d0.zip"
            filepath = "d0"
            if os.path.exists(path):
                import zipfile
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    zip_ref.extractall("")
            print_directory(filepath)
            solve_text = f"""{filepath}
\td0.1
\t\td0.1.1
\t\tf0.1.1.txt
\t\tf0.1.2.txt
\td0.2
\t\td0.2.1
\t\t\td0.2.1.1
\t\t\t\tf0.2.1.1.1.txt
\t\t\tf0.2.1.1.txt
\t\tf0.2.1.txt
\t\tf0.2.2.txt
\tf0.1.txt
\tf0.2.txt\n"""
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                print_directory(filepath)
            self.assertEqual(solve_text, stdout.getvalue())

            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                print_directory(filepath + "/f0.1.txt")
            self.assertEqual(f"{filepath + '/f0.1.txt'} is a file not a directory\n", stdout.getvalue())

            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                print_directory(filepath + "/f0.1")
            self.assertEqual(f"{filepath + '/f0.1'} is invalid\n", stdout.getvalue())
        except ModuleNotFoundError:
            warnings.warn("You need to put the a5_ex2.py in the same directory", ImportWarning)

    def test_a5_ex3(self):
        try:
            from a5_ex3 import gen_fibonacci
            with self.assertRaises(TypeError):
                gen_fibonacci("3").__next__()
            with self.assertRaises(ValueError):
                gen_fibonacci(-1).__next__()
            self.assertEqual([0], list(gen_fibonacci(0)))
            self.assertEqual([0, 1, 1], list(gen_fibonacci(1)))
            self.assertEqual([0, 1, 1, 2, 3], list(gen_fibonacci(3)))
            self.assertEqual([0, 1, 1, 2, 3, 5, 8], list(gen_fibonacci(9.2)))
        except ModuleNotFoundError:
            warnings.warn("You need to put the a5_ex3.py in the same directory", ImportWarning)

    def test_a5_ex4(self):
        try:
            os.path.exists("a5_ex4.txt")
        except OSError:
            warnings.warn("You need to put the a5_ex4.py in the same directory", ImportWarning)


if __name__ == '__main__':
    unittest.main()
