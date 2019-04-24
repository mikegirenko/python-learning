import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('m', 'g', 3000)

    def test_give_default_raise(self):
        self.assertEqual(self.employee.give_raise(), 8000)

    def test_give_custom_raise(self):
        self.assertEqual(self.employee.give_raise(10000), 13000)


unittest.main()
