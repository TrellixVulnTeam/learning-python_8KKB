import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """是否能正确处理像Angus Liu这样的名字"""
        formatted_name = get_formatted_name('angus', 'liu')
        self.assertEqual(formatted_name, 'Angus Liu')

    def test_first_middle_last(self):
        """是否能够处理An Guang Liu这样的名字"""
        formatted_name = get_formatted_name('an', 'liu', 'guang')
        self.assertEqual(formatted_name, 'An Guang Liu')


unittest.main()
