from dist.maciekGPVisitor import maciekGPVisitor
from grammar.dist.maciekGPParser import maciekGPParser
from sympy import sympify

OPERATIONS_LIMIT = 15_000


class MyVisitor(maciekGPVisitor):
    # def visitProgram(self, ctx: maciekGPParser.ProgramContext):
    #     return self.visitChildren(ctx)

    def __init__(self):
        self.variables = {}
        self.operations = 0

    def update_operations(self):
        self.operations += 1
        if self.operations > OPERATIONS_LIMIT:
            raise Exception("Operations limit exceeded")

    def visitPrint(self, ctx: maciekGPParser.PrintContext):
        # self.update_operations()

        expression_text = ctx.expression().getText()
        try:
            result = sympify(expression_text, locals=self.variables)
            print(result)
        except Exception as e:
            print(f"Error evaluating expression: {e}")

        return self.visitChildren(ctx)

    def visitRead(self, ctx: maciekGPParser.ReadContext):
        self.update_operations()

        value = int(input())
        return value

    def visitAssignment(self, ctx: maciekGPParser.AssignmentContext):
        self.update_operations()

        variable = ctx.variable().getText()
        value = self.visitExpression(ctx.expression())
        self.variables[variable] = value
        return value

    def visitExpression(self, ctx: maciekGPParser.ExpressionContext):
        # self.update_operations()

        if ctx.constant():
            return int(ctx.constant().getText())
        elif ctx.variable():
            return self.variables[ctx.variable().getText()]
        elif ctx.read():
            return self.visitRead(ctx.read())
        elif ctx.nestedExpression():
            return self.visitNestedExpression(ctx.nestedExpression())

    def visitNestedExpression(self, ctx: maciekGPParser.NestedExpressionContext):
        self.update_operations()

        left = self.visitExpression(ctx.expression(0))
        right = self.visitExpression(ctx.expression(1))
        operator = ctx.operator().getText()

        if operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        elif operator == "%":
            return left % right
        elif operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        else:
            raise Exception("Unknown operator")

    def visitIfStatement(self, ctx: maciekGPParser.IfStatementContext):
        # self.update_operations()

        condition = self.visitCondition(ctx.condition())
        if condition:
            self.visitBlockStatement(ctx.blockStatement(0))
        elif ctx.else_():
            self.visitBlockStatement(ctx.blockStatement(1))

    def visitBlockStatement(self, ctx: maciekGPParser.BlockStatementContext):
        # self.update_operations()

        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitCondition(self, ctx: maciekGPParser.ConditionContext):
        self.update_operations()

        left = self.visitExpression(ctx.expression(0))
        right = self.visitExpression(ctx.expression(1))
        comparator = ctx.comparator().getText()

        if comparator == "<":
            return left < right
        elif comparator == "<=":
            return left <= right
        elif comparator == ">":
            return left > right
        elif comparator == ">=":
            return left >= right
        elif comparator == "==":
            return left == right
        elif comparator == "!=":
            return left != right
        else:
            raise Exception("Unknown comparator")

    def visitLoopStatement(self, ctx: maciekGPParser.LoopStatementContext):
        # self.update_operations()

        if ctx.constant():
            iterations = int(ctx.constant().getText())
        elif ctx.variable():
            iterations = self.variables[ctx.variable().getText()]
        else:
            raise Exception("Unknown loop iterations")

        for i in range(iterations):
            self.visitBlockStatement(ctx.blockStatement())
