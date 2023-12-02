#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2023.11.29 to Present.
#    * All rights are reserved
#  ==================================================

import math
import unittest.mock
import warnings


class Assignment_8(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_a8_ex1(self):
        try:
            from a8_ex1 import Angle
            a1 = Angle(degree=45)
            a2 = Angle(radian=math.pi / 4)
            a3 = Angle(30, math.pi / 6)
            a1.degree
            self.assertEqual("45.00 deg = 0.79 rad", a1.__str__())
            self.assertEqual("Angle(degree=45.000, radian=0.785)", a2.__repr__())
            self.assertEqual("Angle(degree=30.000, radian=0.524)", repr(a3))
            self.assertEqual(a1, a2)
            self.assertEqual("90.00 deg = 1.57 rad", (a1 + a2).__str__())
            a1 += a3
            self.assertEqual("75.00 deg = 1.31 rad", str(a1))
            sum_angle = Angle.add_all(a1, a2, a3)
            self.assertEqual("150.00 deg = 2.62 rad", str(sum_angle))

            with self.assertRaises(ValueError) as e:
                a4 = Angle()
            self.assertEqual("Either degree or radian must be specified.", str(e.exception))

            with self.assertRaises(ValueError) as e:
                a4 = Angle(degree=45, radian=1)
            self.assertEqual("Degree and radian are not consistent.", str(e.exception))



        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            print(er)
            warnings.warn("You need to put the a8_ex1.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

    def test_a8_ex2(self):
        try:
            from a8_ex2 import Power, Square
            x = 3
            square = Square()
            cube = Power(3)
            cube.exponent

            self.assertEqual(2, square.exponent)
            self.assertEqual(9, square(x))
            self.assertEqual(3, cube.exponent)
            self.assertEqual(27, cube(x))
            m1 = square * 2
            self.assertEqual(4, m1.exponent)
            self.assertEqual(81, m1.__call__(x))
            m2 = square * cube
            self.assertEqual(5, m2.exponent)
            self.assertEqual(243, m2.__call__(x))
            with self.assertRaises(TypeError) as e:
                square("foo")
            self.assertEqual("Input must be a numerical value.", str(e.exception))

            with self.assertRaises(TypeError) as e:
                Power("foo")
            self.assertEqual("The exponent must be a numerical value.", str(e.exception))


        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a8_ex2.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

    def test_a8_ex3(self):
        try:
            from a8_ex3 import StandardScaler
            feats1 = [0, 2, 4, 6, 8, 10]
            feats2 = [1, 3, 5, 7, 9]
            s = StandardScaler()
            StandardScaler().fit(feats1)
            self.assertIsNone(s.mu)
            self.assertIsNone(s.sig)
            s.fit(feats1)
            self.assertEqual(5.0, s[0])
            self.assertEqual(3.7416573867739413, s[1])
            feats1_scaled = s.transform(feats1)
            self.assertEqual(
                [-1.3363062095621219, -0.8017837257372732, -0.2672612419124244, 0.2672612419124244, 0.8017837257372732,
                 1.3363062095621219], feats1_scaled)
            feats2_scaled = s.transform(feats2)
            self.assertEqual([-1.0690449676496976, -0.5345224838248488, 0.0, 0.5345224838248488, 1.0690449676496976],
                             feats2_scaled)
            s = StandardScaler()
            feats2_scaled = s.fit_transform(feats2)
            self.assertEqual([-1.2649110640673518, -0.6324555320336759, 0.0, 0.6324555320336759, 1.2649110640673518],
                             feats2_scaled)
            self.assertEqual(5.0, s[0])
            self.assertEqual(3.1622776601683795, s[1])
            s = StandardScaler()

            with self.assertRaises(ValueError) as e:
                s.transform(feats2)
            self.assertEqual("Scaler has not been fitted.", str(e.exception))

            with self.assertRaises(TypeError) as e:
                s["foo"]
            self.assertEqual("Indices must be integers", str(e.exception))

            with self.assertRaises(IndexError) as e:
                s[2]
            self.assertEqual("Index out of range", str(e.exception))

        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a8_ex3.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")


if __name__ == '__main__':
    unittest.main()
