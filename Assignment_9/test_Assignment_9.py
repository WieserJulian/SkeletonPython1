#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.12.06 to Present.
#    * All rights are reserved
#  ==================================================
import io
import os
import subprocess
import sys
import unittest
import unittest.mock
import warnings
from imp import reload


class Assignment_9(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_a9_ex1(self):
        try:
            with unittest.mock.patch('builtins.input',
                                     side_effect=["a9_ex1_data.txt", "", "(d..d)", "\\d{3}", "\\d{ab12.c}", "d[^ ]+",
                                                  ""]):
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                    __import__("a9_ex1")
                if stdout.getvalue() == "":
                    raise FileExistsError
        except FileExistsError as er:
            warnings.warn("You need to put the a9_ex1.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

        solve_text = "(d..d): ['deed', 'de d']\n" \
                     "\\d{3}: ['780', '222', '341', '445', '100']\n" \
                     "\d{ab12.c}: []\n" \
                     "d[^ ]+: ['d23g780nb', 'deed', 'de', 'ddd32']\n"
        with unittest.mock.patch('builtins.input',
                                 side_effect=["a9_ex1_data.txt", "utf-8", "(d..d)", "\\d{3}", "\\d{ab12.c}", "d[^ ]+",
                                              ""]):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                reload(__import__("a9_ex1"))
            self.assertEqual(solve_text, stdout.getvalue())
        with unittest.mock.patch('builtins.input',
                                 side_effect=["a9_ex2_data.txt"]):
            with self.assertRaises(ValueError) as e:
                reload(__import__("a9_ex1"))
        self.assertEqual("'a9_ex2_data.txt' is not a file", str(e.exception))

    def test_a9_ex2(self):
        try:
            from a9_ex2 import extract_emails
            if extract_emails("") is None:
                raise Exception
        except Exception as er:
            warnings.warn("You need to put the a9_ex2.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

        from a9_ex2 import extract_emails
        t = """
Here are some email addresses:
john.doe@example.com, alice_smith123@gmail.com, ABC+@a-b-c.aBc,
contact@company.org, and info@sub.domain.co.uk.
Some invalid email addresses are:
john@, @example.com, user@domain, us/er@email.com,
invalid@domain.f and invalid.email@invalid@domain.com.
"""
        self.assertEqual(['john.doe@example.com', 'alice_smith123@gmail.com', 'ABC+@a-b-c.aBc',
                          'contact@company.org', 'info@sub.domain.co.uk'], extract_emails(t))

    def test_a9_ex3(self):
        try:
            from a9_ex3 import sum_of_fractions
            if sum_of_fractions(1, 2) is None:
                raise Exception
        except Exception as er:
            warnings.warn("You need to put the a9_ex3.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")
        result = subprocess.run([sys.executable, "a9_ex3.py", "-n 10", "-p 2"], capture_output=True)
        self.assertEqual("Euler-Mascheroni constant approximation (10 terms): 0.626383161", result.stdout.decode().strip())
        result = subprocess.run([sys.executable, "a9_ex3.py", "-n 1_000_000_000", "-p 4"], capture_output=True)
        self.assertEqual("Euler-Mascheroni constant approximation (1000000000 terms): 0.577215665", result.stdout.decode().strip())

    def test_a9_ex4(self):
        try:
            result = subprocess.run([sys.executable, "a9_ex4.py", "--args hello"], capture_output=True)
            if result.stderr.decode().replace("\r", "") == "":
                raise Exception
        except Exception as er:
            warnings.warn("You need to put the a9_ex3.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")
        solve_text = "usage: a9_ex4.py [-h] -p PROGRAM [-a [ARGS ...]] [-t TIMEOUT]\n" \
                     "a9_ex4.py: error: the following arguments are required: -p/--program\n"
        result = subprocess.run([sys.executable, "a9_ex4.py", "--args hello"], capture_output=True)
        self.assertEqual(solve_text, result.stderr.decode().replace("\r", ""))

        solve_text = "Running program 'pythn' without any arguments with a 60s timeout\n" \
                     "The specified program 'pythn' could not be found\n"
        result = subprocess.run([sys.executable, "a9_ex4.py", '--program', 'pythn'], capture_output=True,
                                encoding="utf-8")
        self.assertEqual(solve_text, result.stdout.replace("\r", ""))

        solve_text = "Running program 'python' without any arguments with a 10s timeout\n" \
                     "The program execution timed out\n"
        result = subprocess.run([sys.executable, "a9_ex4.py", "-p", "python", "--timeout", "10"], capture_output=True,
                                encoding="utf-8")
        self.assertEqual(solve_text, result.stdout.replace("\r", ""))

        solve_text = "Running program 'python' with arguments ['a9_ex3.py'] with a 60s timeout\n" \
                     "The 'python' finished with exit code 0\n" \
                     "The 'python' produced the following standard output:\n" \
                     "Euler-Mascheroni constant approximation (1000 terms): 0.577715582\n"
        result = subprocess.run([sys.executable, "a9_ex4.py", "-p", "python", "--args", "a9_ex3.py"],
                                capture_output=True,
                                encoding="utf-8")
        self.assertEqual(solve_text, result.stdout.replace("\r", ""))

        solve_text = "Running program 'python' with arguments ['a9_ex3.py', '-x 9'] with a 60s timeout\n" \
                     "The 'python' finished with exit code 2\n" \
                     "The 'python' produced the following error output:\n" \
                     "usage: a9_ex3.py [-h] [-p PROCESSES] [-n N]\n" \
                     "a9_ex3.py: error: unrecognized arguments: -x 9\n"
        result = subprocess.run([sys.executable, "a9_ex4.py", "-p", "python", "-a", "a9_ex3.py", "-x 9"],
                                capture_output=True,
                                encoding="utf-8")
        self.assertEqual(solve_text, result.stdout.replace("\r", ""))
        pass


if __name__ == '__main__':
    unittest.main()
