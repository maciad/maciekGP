from .Node2 import Node
from .Interfaces import *
import random


class Operator(Node, IMutable):
    operators = ['+', '-', '*', '/', '%']

    def __init__(self, operator):
        super().__init__()
        if operator not in self.operators:
            raise ValueError(f'Unknown operator: {operator}')
        self.operator = operator

    def __str__(self):
        return self.operator

    def evaluate(self, value1, value2):
        if self.operator == '+':
            return value1 + value2
        elif self.operator == '-':
            return value1 - value2
        elif self.operator == '*':
            return value1 * value2
        elif self.operator == '%':
            # return value1 % value2
            return value1 % value2 if value2 != 0 else value1
        elif self.operator == '/':
            if value2 < 0.00001:
                return value1
            return value1 / value2
        else:
            raise ValueError(f'Unknown operator: {self.operator}')

    def mutate(self, ctx):
        self.operator = random.choice(self.operators)

    @staticmethod
    def new_operator(ctx):
        return Operator(random.choice(Operator.operators))
