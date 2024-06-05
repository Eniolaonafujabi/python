import unittest

from length import get_the_length_of_your_word


class MyTestCase(unittest.TestCase):
    def test_that_length_function_get_strings(self):
        self.assertEqual(6, get_the_length_of_your_word("eniola"))

    def  test_that_length_function_get_list(self):
        self.assertEqual(0, get_the_length_of_your_word([]))

    def test_that_length_fuction_can_trough_exception(self):
        self.assertRaises(TypeError, get_the_length_of_your_word, 0)

# add assertion here
if __name__ == '__main__':
    unittest.main()
