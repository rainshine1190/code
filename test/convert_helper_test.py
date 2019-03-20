#coding:utf-8



import datetime
import unittest
from common import convert_helper


class ConverHelperTest(unittest.TestCase):
    """转换操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------ini---------')

    def tearDown(self):
        """清理测试环境"""


    def test_to_int(self):
        self.assertEqual(convert_helper.to_int('1'),1)
        self.assertEqual(convert_helper.to_int('1.0'), 0)
        self.assertEqual(convert_helper.to_int(''), 0)
        self.assertEqual(convert_helper.to_int('a'), 0)
        self.assertEqual(convert_helper.to_int(None), 0)
        self.assertEqual(convert_helper.to_int('1a'), 0)
        self.assertEqual(convert_helper.to_int('bbb'), 0)
        self.assertEqual(convert_helper.to_int(-1), -1)
        self.assertEqual(convert_helper.to_int(0), 0)
        self.assertEqual(convert_helper.to_int(-10), -10)


if __name__ == '__main__':
    unittest.main()
