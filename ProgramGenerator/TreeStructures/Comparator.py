from .Node2 import Node
from .Interfaces import *
from .Expressions import Expression
import random


class Comparator(Node, IMutable):
    comparators = ['<', '>', '==', '!=', '<=', '>=']

    def __init__(self, comparator):
        super().__init__()
        if comparator not in self.comparators:
            raise ValueError(f'Unknown comparator: {comparator}')
        self.comparator = comparator
        # print(self.comparator + 'asdfasdf')

    def __str__(self):
        return self.comparator

    @staticmethod
    def new_comparator(ctx):
        return Comparator(random.choice(Comparator.comparators))

    def mutate(self, ctx):
        self.comparator = random.choice(self.comparators)


class Condition(Node, IGrowable):
    TOLERANCE = 0.00001

    def __init__(self, expression, comparator, expression2):
        super().__init__()
        self.children = [expression, comparator, expression2]

    @property
    def expression(self):
        return self.children[0]

    @expression.setter
    def expression(self, value):
        self.children[0] = value

    @property
    def comparator(self):
        return self.children[1]

    @property
    def expression2(self):
        return self.children[2]

    @expression2.setter
    def expression2(self, value):
        self.children[2] = value

    def __str__(self):
        return f'({self.expression} {self.comparator} {self.expression2})'

    def evaluate(self, prc):
        # print(str(self.comparator) == '==')
        prc.increment_execution_time()
        if str(self.comparator) == '<':
            return self.expression.evaluate(prc) < self.expression2.evaluate(prc)
        elif str(self.comparator) == '>':
            return self.expression.evaluate(prc) > self.expression2.evaluate(prc)
        elif str(self.comparator) == '==':
            return abs(self.expression.evaluate(prc) - self.expression2.evaluate(prc)) < self.TOLERANCE
        elif str(self.comparator) == '!=':
            return abs(self.expression.evaluate(prc) - self.expression2.evaluate(prc)) > self.TOLERANCE
        elif str(self.comparator) == '<=':
            return self.expression.evaluate(prc) <= self.expression2.evaluate(prc)
        elif str(self.comparator) == '>=':
            return self.expression.evaluate(prc) >= self.expression2.evaluate(prc)
        raise ValueError(f'Unknown comparator: {self.comparator}')

    @staticmethod
    def new_condition(ctx):
        return Condition(Expression.new_expression(ctx), Comparator.new_comparator(ctx), Expression.new_expression(ctx))

    def grow(self, ctx):
        if ctx.rand.choice([True, False]):
            self.expression = self.expression.grown(ctx)
        else:
            self.expression2 = self.expression2.grown(ctx)
