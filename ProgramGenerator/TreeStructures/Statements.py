import random
from .Node2 import Node
from .Interfaces import *
from .Expressions import Constant, Variable, Expression
from .Comparator import Condition


class Statement(Node):

    def invoke(self, prc):
        pass

    @staticmethod
    def new_statement(ctx):
        from .NodeFactory import NodeFactory
        return NodeFactory.get_new_statement(ctx.config, ctx)

    def full_grow(self, ctx, target_depth):
        pass


class BlockStatement(Statement, IMutable, IGrowable):
    def __init__(self, children=None):
        super().__init__()
        self.children = children if children else []

    @property
    def statements(self):
        return [c for c in self.children if isinstance(c, Statement)]

    @property
    def growables(self):
        return [c for c in self.children if isinstance(c, Statement) and isinstance(c, IGrowable)]

    def add(self, statement):
        self.children.append(statement)
        # statement.parent = self
        # statement.update_parents()

    def invoke(self, prc):
        prc.increment_execution_time()
        for a in self.statements:
            a.invoke(prc)

    def __str__(self):
        self.update_indent()
        s = '{\n'
        for statement in self.statements:
            s += str(statement) + '\n'
        s += '}'
        return s

    def grow(self, ctx):
        self.add(Statement.new_statement(ctx))

    def grow_self_or_children(self, ctx):
        growables = self.growables
        if not growables:
            self.add(random.choice([Assignment.new_assignment(ctx), Print.new_print(ctx)])) # troche oszukane xdd
            self.update_parents()
            return
        for _ in range(10):
            # TODO: update methods ?
            t = ctx.config.type_to_grow()
            growables_ = [x for x in growables if isinstance(x, t)]
            if growables_:
                growables_[ctx.rand.randint(0, len(growables_) - 1)].grow(ctx)
                self.update_parents()
                return
        if growables:
            growables[ctx.rand.randint(0, len(growables) - 1)].grow(ctx)
        self.update_parents()

    def full_grow(self, ctx, target_depth):
        while self.get_depth() < target_depth:
            self.grow_self_or_children(ctx)
        for statement in self.statements:
            statement.full_grow(ctx, target_depth - 1)

    def mutate(self, ctx):
        if not self.children:
            return
        exp_type = random.random()
        if exp_type < ctx.config.mutation_remove_chance:
            if self.statements:
                # self.statements.pop(ctx.rand.choice(len(self.statements)))
                self.statements.pop(ctx.rand.randint(0, len(self.statements) - 1))
        else:
            # n = self.children.pop(ctx.rand.choice(len(self.children)))
            # self.children.insert(ctx.rand.choice(len(self.children)), n)
            n = self.children.pop(ctx.rand.randint(0, len(self.children) - 1))
            if not self.children:
                self.children.append(n)
            else:
                self.children.insert(ctx.rand.randint(0, len(self.children) - 1), n)


class LoopStatement(Statement):
    def __init__(self, constant_or_variable, block):
        super().__init__()
        self.children = [constant_or_variable, block]

    @staticmethod
    def new_loop(ctx):
        if ctx.rand.choice([True, False]):
            return LoopStatement(Constant.new_constant(ctx), BlockStatement())
        if ctx.variable_counter == 0:
            return LoopStatement(Constant.new_constant(ctx), BlockStatement())
        return LoopStatement(Variable.random_variable(ctx), BlockStatement())

    # def invoke(self, prc):
    #     prc.increment_execution_time()
    #     for _ in range(self.children[0].evaluate(prc)):
    #         self.children[1].invoke(prc)

    def invoke(self, prc):
        prc.increment_execution_time()
        if isinstance(self.children[0], Constant):
            repeat_times = self.children[0].value
        else:
            repeat_times = prc.variables.get(self.children[0].name)
        # print(repeat_times, "SDFASDFASDF")
        for _ in range(repeat_times):
            self.children[1].invoke(prc)

    def full_grow(self, ctx, target_depth):
        self.children[1].full_grow(ctx, target_depth)

    def __str__(self):
        self.update_indent()
        return "loop " + str(self.children[0]) + "\n" + str(self.children[1])


class Assignment(Statement, IGrowable):
    def __init__(self, variable, expression):
        super().__init__()
        self.children = [variable, expression]

    @staticmethod
    def new_assignment(ctx):
        expression = Expression.new_expression(ctx)
        return Assignment(Variable.random_or_new(ctx), expression)

    def invoke(self, prc):
        prc.increment_execution_time()
        # print(self.children[0].name, self.children[1].evaluate(prc))
        prc.variables[self.children[0].name] = self.children[1].evaluate(prc)

    def grow(self, ctx):
        self.children[1] = self.children[1].grown(ctx)

    def full_grow(self, ctx, target_depth):
        while self.children[1].get_depth() < target_depth:
            self.grow(ctx)

    def __str__(self):
        # self.update_indent()
        return str(self.children[0]) + ' = ' + str(self.children[1])


class Print(Statement, IGrowable):
    def __init__(self, expression):
        super().__init__()
        self.children = [expression]

    @staticmethod
    def new_print(ctx):
        return Print(Expression.new_expression(ctx))

    def invoke(self, prc):
        prc.increment_execution_time()
        # print(self.children[0].evaluate(prc))
        prc.push(self.children[0].evaluate(prc))
        # print(prc.output)

    def __str__(self):
        return 'print(' + str(self.children[0]) + ')'

    def grow(self, ctx):
        self.children[0] = self.children[0].grown(ctx)

    def full_grow(self, ctx, target_depth):
        while self.children[0].get_depth() < target_depth:
            self.grow(ctx)


class IfStatement(Statement):
    def __init__(self, condition, block, else_block=None):
        super().__init__()
        if not else_block:
            self.children = [condition, block]
        else:
            self.children = [condition, block, else_block]

    @staticmethod
    def new_if_statement(ctx):
        if ctx.rand.choice([True, False]):  # Randomly decide whether to include else block
            return IfStatement(Condition.new_condition(ctx), BlockStatement(), BlockStatement())
        else:
            return IfStatement(Condition.new_condition(ctx), BlockStatement())

    def __str__(self):
        self.update_indent()
        s = 'if ' + str(self.children[0]) + '\n'
        s += str(self.children[1])
        if len(self.children) == 3:
            s += 'else\n'
            s += str(self.children[2])
        return s

    def invoke(self, prc):
        prc.increment_execution_time()
        if self.children[0].evaluate(prc):
            self.children[1].invoke(prc)
        elif len(self.children) == 3:
            self.children[2].invoke(prc)

    def full_grow(self, ctx, target_depth):
        self.children[1].full_grow(ctx, target_depth)
        if len(self.children) == 3:
            self.children[2].full_grow(ctx, target_depth)
