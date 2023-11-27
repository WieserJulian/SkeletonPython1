#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.11.26 to Present.
#    * All rights are reserved
#  ==================================================

import unittest.mock
import warnings
import io
from copy import deepcopy


class Assignment_7(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_a7_ex1(self):
        try:
            from a7_ex1 import Radian
            if len(Radian.__dict__) == 7: raise ModuleNotFoundError
            c = Radian(90)
            self.assertAlmostEqual(1.57, c.rad(), places=2)
            solve_text = "The degree is 90.00 and the radian is 1.57\n"
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                c.print()
            self.assertEqual(solve_text, stdout.getvalue())

            pass
        except ModuleNotFoundError as er:
            warnings.warn("You need to put the a7_ex1.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")

    def test_a7_ex2(self):
        try:
            from a7_ex2 import Rotate
            if len(Rotate.__dict__) == 4: raise ModuleNotFoundError
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            rotate90 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
            # Rotate 90deg
            matrix1 = deepcopy(matrix)
            c1 = Rotate(matrix1, 90)
            c11 = c1.rotation()
            self.assertEqual(rotate90, c11)
            self.assertEqual(matrix, matrix1)

            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            rotatem90 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            matrix1 = deepcopy(matrix)
            c2 = Rotate(matrix1, -90)
            c22 = c2.rotation()
            self.assertEqual(rotatem90, c22)
            self.assertEqual(matrix, matrix1)

            matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                      [21, 22, 23, 24, 25]]
            rotate180 = [[25, 24, 23, 22, 21], [20, 19, 18, 17, 16], [15, 14, 13, 12, 11], [10, 9, 8, 7, 6],
                         [5, 4, 3, 2, 1]]
            matrix1 = deepcopy(matrix)
            c3 = Rotate(matrix1, 180)
            c33 = c3.rotation()
            self.assertEqual(rotate180, c33)
            self.assertEqual(matrix, matrix1)

            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            rotatem90 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
            matrix1 = deepcopy(matrix)
            c4 = Rotate(matrix1, 90, True)
            c44 = c4.rotation()
            self.assertIsNone(c44)
            self.assertEqual(rotatem90, matrix1)

            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            rotatem90 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            matrix1 = deepcopy(matrix)
            c5 = Rotate(matrix1, -90, True)
            c55 = c5.rotation()
            self.assertIsNone(c55)
            self.assertEqual(rotatem90, matrix1)

            matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                      [21, 22, 23, 24, 25]]
            rotate180 = [[25, 24, 23, 22, 21], [20, 19, 18, 17, 16], [15, 14, 13, 12, 11], [10, 9, 8, 7, 6],
                         [5, 4, 3, 2, 1]]
            matrix1 = deepcopy(matrix)
            c6 = Rotate(matrix1, 180, inplace=True)
            c66 = c6.rotation()
            self.assertIsNone(c66)
            self.assertEqual(rotate180, matrix1)
            pass
        except ModuleNotFoundError as er:
            warnings.warn("You need to put the aa7_ex2.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")

    def test_a7_ex3(self):
        try:
            from a7_ex3 import Distance
            if len(Distance.__dict__) == 7: raise ModuleNotFoundError
            x = Distance(10)
            self.assertEqual("Distance: the number of vectors =10", x.to_string())
            with self.assertRaises(NotImplementedError):
                x.dist()
        except ModuleNotFoundError:
            warnings.warn("You need to put the aa7_ex3.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")

    def test_a7_ex4(self):
        try:
            from a7_ex4 import Minkowski
            if len(Minkowski.__dict__) == 5: raise ModuleNotFoundError
            vect1 = [1, 2, 3]
            vect2 = [4, 5, 6]
            k = Minkowski(2, vect1, vect2)
            self.assertEqual("Minkowski: the number of vectors =2, vector_1=[1, 2, 3], vector_2=[4, 5, 6]",
                             k.to_string())
            self.assertEqual(5.1962, k.dist())

        except ModuleNotFoundError:
            warnings.warn("You need to put the aa7_ex4.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")

    def test_a7_ex5(self):
        try:
            from a7_ex5 import Manhattan
            if len(Manhattan.__dict__) == 5: raise ModuleNotFoundError
            vect1 = [1, 2, 3]
            vect2 = [4, 5, 6]
            m = Manhattan(2, vect1, vect2)
            self.assertEqual("Manhattan: the number of vectors =2, vector_1=[1, 2, 3], vector_2=[4, 5, 6]",
                             m.to_string())
            self.assertEqual(9.0, m.dist())

        except ModuleNotFoundError:
            warnings.warn("You need to put the aa7_ex5.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")

    def test_a7_ex6(self):
        try:
            from a7_ex6 import Euclidean
            if len(Euclidean.__base__.__dict__) == 5: raise ModuleNotFoundError
            vect1 = [1, 2, 3]
            vect2 = [4, 5, 6]
            e = Euclidean(2, vect1, vect2)
            print("Euclidean: the number of vectors =2, vector_1=[1, 2, 3], vector_2=[4, 5, 6]", e.to_string())
            print(5.1962, e.dist())
        except ModuleNotFoundError:
            warnings.warn("You need to put the aa7_ex6.py in the same directory", ImportWarning)
            self.skipTest("Not Implemented")


if __name__ == '__main__':
    unittest.main()
