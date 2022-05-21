import unittest
from Parser import Parser


class MyTestCase(unittest.TestCase):
    def testStringVoid(self):
        """
        Test if an input of a void string give an empty list
        """
        parser = Parser('')
        list = parser.token()
        self.assertEqual(list, [])  # add assertion here

    def testDeciToHexadec(self):
        """
        Test conversion from base 16 number to base 10 number
        """
        parser = Parser('B5')
        list = parser.token()
        self.assertEqual(list, [('NUMBER', 181.0)])

    def testWhiteSpace(self):
        """
        Test if whitespaces are removed from the list of token
        """
        parser = Parser('B5 234 576      57578      BA3')
        list = parser.token()
        self.assertEqual(list, [('NUMBER', 181.0), ('NUMBER', 234.0), ('NUMBER', 576.0), ('NUMBER', 57578.0),
                                ('NUMBER', 2979.0)])


