DIGIT = '0123456789ABCDE'
HEXA = '0123456789ABCDE'

OPERATOR = '()+-÷x'


def convertHexToDeci(number):
    """
    Enable to convert a base 16 number into base 10 number.

    :param
        number: Base 16 number

    :return:
        float: The base 10 number corresponding of base 16 number
    """
    conv = 0
    for i in range(len(number)):
        conv += float(HEXA.index(number[i]) * 16 ** (len(number) - i - 1))
    return conv


class Parser:

    def __init__(self, text):
        self.text = text
        self.indices = -1
        self.chars = ''

    def hasNext(self):
        """
        Enable to know if the indices is not out of range

        :return:
            boolean: If indices is not out of range of token list
        """
        return self.indices < len(self.text)

    def whiteSpace(self):
        """
        Detect whitespace

        :return:
            boolean: If chars is a whitespace
        """
        return self.chars in ' /n/t/r'

    def token(self):
        """
        Enable to create a list of token

        :return:
            list: List of tuple that contains a type or symbol link with a value
        """
        dic = []
        self.indices += 1
        while self.hasNext():
            chars = self.text[self.indices]
            number = ''
            if chars in OPERATOR:
                dic.append((chars, None))
                self.indices += 1

            elif chars in DIGIT:

                while chars in DIGIT and self.hasNext():
                    number += chars
                    self.indices += 1

                    if self.hasNext():
                        chars = self.text[self.indices]

                    else:
                        break

                test = False
                for i in number:
                    if i in 'ABCDEF':
                        test = True
                        break

                if test:
                    dic.append(('NUMBER', convertHexToDeci(number)))

                else:
                    dic.append(('NUMBER', float(number)))

            elif self.whiteSpace():
                self.indices += 1

            else:
                raise Exception("Input not valid")
        return dic
