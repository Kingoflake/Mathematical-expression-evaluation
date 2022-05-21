# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Parser import Parser
from Inter import Inter
if __name__ == '__main__':
    while True:
        text = input("expression mathématiques\n")
        parser = Parser(text)
        lists = parser.token()
        print(lists)
        inter = Inter(lists)
        print(inter.expression())
