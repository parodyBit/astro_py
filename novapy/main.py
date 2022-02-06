from novapy.utility import Utility
from libnova_tests import TestRunner

class CalculatorApp:

    def __init__(self):
        test = TestRunner()
        test.run_tests()


    def add(self, item1, item2):
        return item1 + item2

    def subtract(self, item1, item2):
        return item1 - item2

    def multiply(self, item1, item2):
        return item1 * item2

    def divide(self, item1, item2):
        if item2 == 0:
            return 1
        return item1 / item2

if __name__ == '__main__':
    CalculatorApp()


