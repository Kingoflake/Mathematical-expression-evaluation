
class Inter:

    def __init__(self, token):
        self.token = token
        self.currentToken = None
        self.indices = -1

    def hasNext(self):
        """
        Enable to know if the indices is not out of range

        :return:
            boolean: If indices is not out of range of token list
        """
        return self.indices < len(self.token)

    def expression(self):
        """
        Enable to evaluate all value's terms e.g '+' and '-' operation.

        :return:
            float: The sum of all value's terms
        """
        self.indices += 1
        values = [self.term()]

        while self.hasNext():
            self.currentToken = self.token[self.indices]
            if self.currentToken[0] == '+':
                self.indices += 1
                values.append(self.term())

            elif self.currentToken[0] == '-':
                self.indices += 1
                values.append(-1 * self.term())

            else:
                break

        evaluation = 0
        for i in values:
            evaluation += i

        return evaluation

    def term(self):
        """
        Enable to evaluate all value's factor e.g 'x' and '÷' operations.

        :return:
            float: Multiplication of all value's factors
        """
        values = [self.factor()]

        while self.hasNext():
            self.currentToken = self.token[self.indices]
            if self.currentToken[0] == "x":
                self.indices += 1
                values.append(self.factor())

            elif self.currentToken[0] == "÷":
                self.indices += 1
                denominator = self.factor()

                if denominator == 0:
                    raise Exception("Divide by zero is forbidden")

                values.append(1.0/denominator)

            else:
                break

        evaluation = 1.0
        for i in values:
            evaluation *= i

        return evaluation

    def factor(self):
        """
        Enable to find numbers or factors

        :return:
            float: Numbers of the mathematical expression
        """
        self.currentToken = self.token[self.indices]

        if self.currentToken[0] == '(':
            values = self.expression()
            self.currentToken = self.token[self.indices]

            if self.currentToken[0] != ')':
                raise Exception("Expression is not valid")
            self.indices += 1
            return values

        elif self.currentToken[0] == 'NUMBER':
            values = self.currentToken[1]

            if self.hasNext():
                self.indices += 1

            return values

        elif self.currentToken[0] == '-':
            values = -1.0
            if self.hasNext():
                self.indices += 1

            return values * self.factor()



