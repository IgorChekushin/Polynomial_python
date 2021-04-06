import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    a = Polynomial([1, 2])
    b = Polynomial([1, 2, 3])
    c = 79

    # Test init
    def test_init_const(self):
        self.assertEqual(str(Polynomial(2)), "2")

    def test_init_tuple(self):
        self.assertEqual(str(Polynomial((2, 3))), "2x+3")

    def test_init_list(self):
        self.assertEqual(str(Polynomial([2, 3])), "2x+3")

    def test_init_empty_args_raise_TypeError(self):
        with self.assertRaises(TypeError):
            Polynomial()

    def test_init_empty_list_raise_TypeError(self):
        with self.assertRaises(ValueError):
            a = Polynomial([])

    def test_init_empty_tuple_raise_ValueError(self):
        with self.assertRaises(ValueError):
            Polynomial(())

    def test_init_invalid_args_raise_TypeError(self):
        with self.assertRaises(TypeError):
            Polynomial("Invalid str")

    # Tests for add
    def test_add_polynomial(self):
        self.assertEqual(self.a + self.b, Polynomial([1, 3, 5]))

    def test_add_right_const(self):
        self.assertEqual(self.a + self.c, Polynomial([1, 81]))

    def test_add_left_const(self):
        self.assertEqual(self.c + self.a, Polynomial([1, 81]))

    def test_add_raise_TypeError(self):
        with self.assertRaises(TypeError):
            self.a + "3"

    # Tests for mul
    def test_mul_polynomial(self):
        self.assertEqual(self.a * self.b, Polynomial([1, 4, 7, 6]))

    def test_mul_right_const(self):
        self.assertEqual(self.a * self.c, Polynomial([79, 158]))

    def test_mul_left_const(self):
        self.assertEqual(self.c * self.a, Polynomial([79, 158]))

    def test_mul_raise(self):
        with self.assertRaises(TypeError):
            self.b * [1, 2]

    # Tests for sub
    def test_sub_polynomial(self):
        self.assertEqual(self.a - self.b, Polynomial([-1, -1, -1]))

    def test_sub_right_const(self):
        self.assertEqual(self.a - self.c, Polynomial([1, -77]))

    def test_sub_left_const(self):
        self.assertEqual(self.c - self.a, Polynomial([-1, 77]))

    def test_sub_raise(self):
        with self.assertRaises(TypeError):
            self.b - (1, "")

    # Test str
    def test_str(self):
        self.assertEqual(str(self.a), "x+2")

    # Tests for eq
    def test_eq_polynom_False(self):
        self.assertEqual(self.a == self.b, False)

    def test_eq_polynom_True(self):
        self.assertEqual(self.a == Polynomial((1, 2)), True)

    def test_eq_const_False(self):
        self.assertEqual(self.a == 10, False)

    def test_eq_const_True(self):
        self.assertEqual(Polynomial(10) == 10, True)

    # Test repr
    def test_repr(self):
        self.assertEqual(repr(self.a), "Polynomial([1, 2])")


if __name__ == '__main__':
    unittest.main()
