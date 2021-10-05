#!/ust/bin/python3
"""
6-max_integer_test.py
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test class for max_integer"""
    def test_module_docstring(self):
        """test for doc"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """test for function doc"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """test for empty lists"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """test for no argument passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """test for one element in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """test for all positive with max at the end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """test for all positive with max at the middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_begginig(self):
        """test for all positive with max at the begginig"""
        b =[200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """test for one negative"""
        one = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(one), 200)

    def test_all_negative(self):
        """test for all negative"""
        al = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(al), -1)

    def test_none(self):
        """test for none as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """test for not integer argument"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
