from .Node2 import Node
from .Interfaces import *
from .Operator import Operator


class Expression(Node):
    probability = 0.1

    def evaluate(self, program_run_context):
        pass

    @staticmethod
    def new_expression(ctx):
        from .NodeFactory import NodeFactory
        return NodeFactory.get_new_expression(ctx.config, ctx)

    def grown(self, ctx):
        if ctx.rand.choice([True, False]):
            return NestedExpression(self.new_expression(ctx), Operator.new_operator(ctx), self)
        return NestedExpression(self, Operator.new_operator(ctx), self.new_expression(ctx))


class NestedExpression(Expression, IGrowable):
    def __init__(self, expression, operator, expression2):
        super().__init__()
        self.children = [expression, operator, expression2]

    @property
    def expression(self):
        return self.children[0]

    @expression.setter
    def expression(self, value):
        self.children[0] = value

    @property
    def operator(self):
        return self.children[1]

    @property
    def expression2(self):
        return self.children[2]

    @expression2.setter
    def expression2(self, value):
        self.children[2] = value

    def evaluate(self, prc):
        return self.operator.evaluate(self.expression.evaluate(prc), self.expression2.evaluate(prc))

    def __str__(self):
        return f'({self.expression} {self.operator} {self.expression2})'

    def grow(self, ctx):
        if ctx.rand.choice([True, False]):
            self.expression = self.expression.grown(ctx)
        else:
            self.expression2 = self.expression2.grown(ctx)


class Constant(Expression, IMutable):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def evaluate(self, prc):
        return self.value

    def mutate(self, ctx):
        # TODO: change values after adding configuration file
        self.value = ctx.rand.randint(0, 10)

    def __str__(self):
        return str(self.value)

    @staticmethod
    def new_constant(ctx):
        return Constant(ctx.rand.randint(0, 10))


class Read(Expression):
    def evaluate(self, prc):
        return prc.pop()
        # return int(input())

    def __str__(self):
        return 'read()'

    @staticmethod
    def new_read(ctx):
        return Read()


class Variable(Expression, IMutable):
    def __init__(self, index):
        super().__init__()
        self.name = f'x_{index}'

    def evaluate(self, prc):
        # print('evaluated', prc.variables)
        return prc.variables.get(self.name)

    def __str__(self):
        return self.name

    def mutate(self, ctx):
        idx = ctx.rand.randint(0, len(ctx.variables))
        self.name = f'x_{idx}'

    # @staticmethod
    # def random(ctx):
    #     # count = ctx.variable_count
    #     count = len(ctx.variables)
    #     if count == 0:
    #         return None
    #     idx = ctx.rand.randint(0, ctx.variable_count - 1)
    #     return Variable(idx)
    #
    # @staticmethod
    # def random_or_new(ctx):
    #     # count = ctx.variable_count
    #     count = len(ctx.variables)
    #     idx = ctx.rand.randint(-1, count)
    #     return Variable(idx) if idx >= 0 else Variable(count)

    @staticmethod
    def random_or_new(ctx):
        if ctx.variable_counter == 0:
            ctx.variable_counter += 1
            return Variable(0)
        if ctx.rand.choice([True, False]):
            # new variable
            var = Variable(ctx.variable_counter)
            ctx.variable_counter += 1
            return var
        # random variable
        idx = ctx.rand.randint(0, ctx.variable_counter - 1)
        return Variable(idx)
