import unittest

from stack_creation import MyStack


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = MyStack()
        self.stack.add_to_stack("Hello World1")
        self.stack.add_to_stack("Hello World2")
        self.stack.add_to_stack("Hello World3")
        self.stack.add_to_stack("Hello World4")
    def test_that_stack_can_add_element(self):
        self.assertEqual(len(self.stack.stack_attribute), 4)  # add assertion here

    def test_stack_removes_last_in_element(self):
        self.stack.pop_from_stack()
        self.assertEqual(self.stack.stack_attribute[-1], "Hello World3")

    def test_stack_returns_the_top_element(self):
        self.assertEqual(self.stack.return_stack_top(), "Hello World4")

    def test_that_stack_is_not_empty(self):
        self.assertFalse(self.stack.check_if_stack_is_empty())

    def test_that_stack_is_full(self):
        self.assertTrue(self.stack.check_if_stack_is_full())


if __name__ == '__main__':
    unittest.main()
