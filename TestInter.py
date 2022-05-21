import unittest
from Inter import Inter
from Parser import Parser


class MyTestCase(unittest.TestCase):

    def testUnaryMinus(self):
        """
        Test the minus simplification
        """
        parser = Parser('---7')
        lists = parser.token()
        inter = Inter(lists)
        result = inter.expression()

        self.assertEqual(result, -7.0)

    def testMultipleParenthesis(self):
        """
        Test the behavior with many parenthesis in input
        """
        parser = Parser('((4+5)x(4-4))+ (((1)))')
        lists = parser.token()
        inter = Inter(lists)
        result = inter.expression()

        self.assertEqual(result, 1.0)

