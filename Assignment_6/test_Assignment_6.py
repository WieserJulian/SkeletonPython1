#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.11.15 to Present.
#    * All rights are reserved
#  ==================================================

import unittest
import unittest.mock
import os
import warnings
import io
import pickle


class MyTestCase(unittest.TestCase):
    filepath = "Examples"
    maxDiff = None

    def setUp(self) -> None:
        path = r"Examples.zip"
        if os.path.exists(path):
            import zipfile
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(self.filepath)

    def test_a6_ex1(self):
        try:
            from a6_ex1 import file_statistics
            solve_text = """Statistics of file ex1_1.txt:
Number of lines: 79
Number of words: 3578
Number of characters: 21966
Number of digits: 0\n"""
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                file_statistics(os.path.join(self.filepath, "ex1_1.txt"))
            self.assertEqual(solve_text, stdout.getvalue())

            solve_text = """Statistics of file ex1_2.txt:
Number of lines: 612
Number of words: 22308
Number of characters: 140742
Number of digits: 193\n"""
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                file_statistics(os.path.join(self.filepath, "ex1_2.txt"))
            self.assertEqual(solve_text, stdout.getvalue())

            solve_text = """Statistics of file ex1_3.txt:
Number of lines: 124453
Number of words: 901325
Number of characters: 5458195
Number of digits: 3190\n"""
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                file_statistics(os.path.join(self.filepath, "ex1_3.txt"))
            self.assertEqual(solve_text, stdout.getvalue())

            with self.assertRaises(ValueError) as exc:
                file_statistics(os.path.join(self.filepath, "ex1_4.py"))
            self.assertEqual(str(exc.exception), "Path ex1_4.py is not a text file")
            with self.assertRaises(OSError) as exc:
                file_statistics(os.path.join(self.filepath, "ex1_5.txt"))
            self.assertEqual(str(exc.exception), "Path ex1_5.txt does not exist")
        except ModuleNotFoundError:
            warnings.warn("You need to put the a6_ex1.py in the same directory", ImportWarning)

    def test_a6_ex2(self):
        try:
            from a6_ex2 import chunks
            solve_text = [
                b'12 w 21  d23g780nb deed e',
                b'2 21.87\r\n43 91 - . 222 mf',
                b'tg 21 bx .1 3 g d e 6 de ',
                b'ddd32 3412\r\n0.3 0 0. 0 0 ',
                b'1\r\n\r\n70\r\n\r\nn 12 1    9   ',
                b' m1 1m 445\r\nx 100\r\n'
            ]
            for i, c in enumerate(chunks(os.path.join(self.filepath, "ex2_example.txt"), 25, mode="rb")):
                self.assertEqual(solve_text[i], c)
            with self.assertRaises(ValueError) as exc:
                chunks(os.path.join(self.filepath, "ex2_example.txt"), size=-1).__next__()
            with self.assertRaises(ValueError):
                chunks(self.filepath, size=1).__next__()
        except ModuleNotFoundError:
            warnings.warn("You need to put the a6_ex2.py in the same directory", ImportWarning)

    def test_a6_ex3(self):
        try:
            from a6_ex3 import merge_csv_files
            paths = [
                os.path.join(self.filepath, "ex3_1.csv"),
                os.path.join(self.filepath, "ex3_2.csv"),
                os.path.join(self.filepath, "ex3_3.csv"),
            ]
            os.remove("merged.csv")
            merge_csv_files(*paths)
            with open("merged_all.csv", "r") as merged:
                with open(os.path.join(self.filepath, "merged_all.csv"), "r") as all:
                    # all has a empty line to much
                    for a, m in zip(all.readlines()[0:-1], merged.readlines()):
                        self.assertEqual(a, m)

            merge_csv_files(*paths, only_shared_columns=True)
            with open("merged_shared.csv", "r") as merged:
                with open(os.path.join(self.filepath, "merged_shared.csv"), "r") as shared:
                    for a, m in zip(shared.readlines()[0:-1], merged.readlines()):
                        self.assertEqual(a, m)

        except ModuleNotFoundError:
            warnings.warn("You need to put the a6_ex3.py in the same directory", ImportWarning)

    def test_a6_ex4(self):
        try:
            from a6_ex4 import create_user, login, change_password

            files = ["Franz Kafka.pkl", "George Orwell.pkl", "H. P. Lovecraft.pkl", "William Golding.pkl"]
            for path in files:
                if os.path.exists(path):
                    os.remove(path)
            open("logs.txt", 'w').close()
            for file in files:
                try:
                    os.remove(file)
                except Exception:
                    pass
            create_user('Franz Kafka', 'Die Verwandlung', 'fkafka')
            create_user('H. P. Lovecraft', 'The Call of Cthulhu', 'lcrft')
            create_user('William Golding', 'Lord of the Flies', 'password')
            create_user('George Orwell', '1984', 'orwell1948')
            login('Franz Kafka', 'fkafks')
            login('Franz Kafka', 'fkafka')
            login('H. P. Lovecraft', 'lcrft')
            login('William Golding', 'password')
            change_password('William Golding', 'password', 'wigold')
            login('George Orwell', 'orwell1984')
            login('George Orwell', 'orwell1948')
            change_password('George Orwell', 'orwell1984', 'orwell1984')
            change_password('George Orwell', 'orwell1948', 'orwell1984')
            login('George Orwel', 'orwell1984')
            create_user('George Orwell', '1984', 'orwell1984')

            for file in files:
                with open(file, "rb") as pkl_in:
                    pkl_in = pickle.load(pkl_in)
                    with open(os.path.join(self.filepath, file), "rb") as pkl_test:
                        pkl_test = pickle.load(pkl_test)
                        for key in list(pkl_test.keys())[0:-1]:
                            # This is because the example.zip is false
                            pkl_test[key] = pkl_test[key].replace("H.P.", "H. P.")
                            self.assertEqual(pkl_test[key], pkl_in[key])

            with open("logs.txt", "r") as log_in:
                with open(os.path.join(self.filepath, "logs.txt"), "r") as log_test:
                    for a, m in zip(log_test.readlines(), log_in.readlines()):
                        self.assertEqual(a.split("at ")[0], m.split("at ")[0])

        except ModuleNotFoundError:
            warnings.warn("You need to put the a6_ex2.py in the same directory", ImportWarning)


if __name__ == '__main__':
    unittest.main()
