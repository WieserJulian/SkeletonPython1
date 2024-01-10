#  ==================================================
#    * Copyright (c) 2023 Julian Wieser From 2024.01.10 to Present.
#    * All rights are reserved
#  ==================================================

import unittest.mock
import warnings

import numpy as np


class Assignment_10(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_a10_ex1(self):
        from a10_ex1 import extend
        try:
            if extend(np.array([[1, 2, 3], [2, 3, 4]]), 2, 3) is None:
                raise AttributeError
        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a10_ex1.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")
        m1 = np.arange(2 * 3).reshape(2, -1)
        self.assertTrue(np.array_equal(np.array([[0, 1, 2], [3, 4, 5]]), extend(m1, 2, 3)))
        self.assertTrue(np.array_equal(np.array([[0, 1, 2, 1, 1],
                                                 [3, 4, 5, 4, 4],
                                                 [1, 2, 3, 2, 2],
                                                 [1, 2, 3, 2, 2]]), extend(m1, 4, 5)))
        with self.assertRaises(ValueError) as e:
            extend(m1, 2, 1)
        self.assertEqual("invalid cols", str(e.exception))
        with self.assertRaises(ValueError) as e:
            extend(m1, 1, 2)
        self.assertEqual("invalid rows", str(e.exception))
        m2 = np.arange(2 * 3, dtype=float).reshape(2, -1)
        self.assertTrue(np.array_equal(np.array([[0., 1., 2., 1., 1., ],
                                                 [3., 4., 5., 4., 4., ],
                                                 [1.5, 2.5, 3.5, 2.5, 2.5],
                                                 [1.5, 2.5, 3.5, 2.5, 2.5]],
                                                ), extend(m2, 4, 5)))
        self.assertTrue(np.array_equal(np.array([[0, 1, 2, 10, 10],
                                                 [3, 4, 5, 10, 10],
                                                 [10, 10, 10, 10, 10],
                                                 [10, 10, 10, 10, 10]]
                                                ), extend(m1, 4, 5, fill=10)))
        with self.assertRaises(ValueError) as e:
            extend(m2, 4, 4, fill="foo")
        self.assertEqual("invalid fill", str(e.exception))
        m3 = np.ones(1)
        with self.assertRaises(ValueError) as e:
            extend(m3, 2, 3)
        self.assertEqual("can only extend 2D arrays, not 1D", str(e.exception))

    def test_a10_ex2(self):
        from a10_ex2 import elements_wise
        try:
            x = np.array([1, 2, 3])
            def func(x):
                return x + 1
            elements_wise(x, func)
            if np.array_equal(x, np.array([1, 2, 3])):
                raise AttributeError
            pass
        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a10_ex2.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

        def func(x):
            return x * x + 3 * x + 2

        s1 = np.array([[[2., 6., 12.],
                        [20., 30., 42.]],
                       [[56., 72., 90.],
                        [110., 132., 156.]]]
                      )
        s2 = np.array([[2., 6., 12.],
                       [20., 30., 42.]])
        a1 = np.array(range(2 * 2 * 3), dtype=float).reshape(2, 2, -1)
        a2 = np.array(range(2 * 3), dtype=float).reshape(2, -1)
        elements_wise(a1, func)
        elements_wise(a2, func)
        np.testing.assert_equal(a1, s1)
        np.testing.assert_equal(a2, s2)

    def test_a10_ex3(self):
        from a10_ex3 import one_hot_encoding
        try:
            if one_hot_encoding(np.array([])) is None:
                raise AttributeError()
        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a10_ex3.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")
        a = np.array(["a", "a", "b", "c"])
        np.testing.assert_equal(one_hot_encoding(a), np.array([[1., 0., 0.],
                                                               [1., 0., 0.],
                                                               [0., 1., 0.],
                                                               [0., 0., 1.]]
                                                              ))
        a = np.array([10, 5, 15, 20])
        np.testing.assert_equal(one_hot_encoding(a), np.array([[0., 1., 0., 0.],
                                                               [1., 0., 0., 0.],
                                                               [0., 0., 1., 0.],
                                                               [0., 0., 0., 1.]]
                                                              ))
        a = np.array([[1, 2], [3, 4]])
        with self.assertRaises(ValueError) as e:
            one_hot_encoding(a)
        self.assertEqual("The function can work for 1D matrices, not 2D", str(e.exception))

    def test_a10_ex4(self):
        from a10_ex4 import moving_average_2D
        try:
            if moving_average_2D(np.array([[1, 2], [3, 4]]), 1) is None:
                raise AttributeError
        except (AttributeError, ImportError, ModuleNotFoundError) as er:
            warnings.warn("You need to put the a10_ex4.py in the same directory", ImportWarning, source=er)
            self.skipTest("Possible not implemented")

        arr = np.arange(4 * 5).reshape(4, -1)
        result = moving_average_2D(arr, 3)
        np.testing.assert_equal(result, np.array([[6., 7., 8.],
                                                  [11., 12., 13.]]
                                                 ))
        with self.assertRaises(ValueError) as e:
            moving_average_2D(arr, 5)
        self.assertEqual("Invalid window size", str(e.exception))
        with self.assertRaises(TypeError) as e:
            moving_average_2D(np.array([["a", "b"], ["c", "d"]]), 2)
        self.assertEqual("Invalid data type", str(e.exception))


if __name__ == '__main__':
    unittest.main()
