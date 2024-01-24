from datetime import datetime
from random import Random
from Node2 import Node
from Interfaces import *
from Actions import Action
from Expressions import Variable


class Program(Node, IMutable, IGrowable):
    TAB = ' '

    def __init__(self, seed=None, children=None, config=None):
        super().__init__()
        self.rand = Random(seed) if seed is not None else Random()
        self.config = config if config is not None else None # else TreeConfig()  TODO: TreeConfig
        self.children = children if children is not None else []

    @property
    def actions(self):
        return [child for child in self.children if isinstance(child, Action)]

    @property
    def variables(self):
        return list(set([child for child in self.children if isinstance(child, Variable)]))

    @property
    def nodes(self):
        return self.get_nested_nodes()

    def get_nodes(self):
        return self.nodes

    @property
    def growables(self):
        return [node for node in self.nodes if isinstance(node, IGrowable)]

    @property
    def mutables(self):
        return [node for node in self.nodes if isinstance(node, IMutable)]

    def add_action(self, action):
        self.children.append(action)

    def invoke(self, prc):
        start_time = datetime.now()

        try:
            for action in self.actions:
                action.invoke(prc)
        except Exception as e:
            print(e)

        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds() * 1000
        prc.execution_time = elapsed_time

    def __str__(self):
        self.update_indent()
        s = ''
        for child in self.children:
            s += str(child) + '\n'
        return s

    def grow(self, ctx=None):
        if ctx is not None:
            self.children.append(Action.new_action(ctx))
        else:
            x = self.growables
            for _ in range(10):
                t = self.config.type_to_grow()
                # growables_ = [node for node in self.growables if node.__class__ == t]
                growables_ = [node for node in self.growables if isinstance(node, t)]
                if growables_:
                    growables_[self.rand.randint(0, len(growables_) - 1)].grow(self)
                    self.update_parents()
                    return
            if x:
                x[self.rand.randint(0, len(x) - 1)].grow(self)

            self.update_parents()

    def full_grow(self):
        while self.get_depth() < self.config.max_depth:
            self.grow()
        for action in self.actions:
            action.full_grow(self.config.max_depth - 1)

    # def mutate(self, t):
    #     x = self.mutables
    #     mutables_ = [node for node in self.mutables if isinstance(node, t)]
    #     if mutables_:
    #         mutables_[self.rand.randint(0, len(mutables_) - 1)].mutate(self)
    #         return
    #     print('this should not happen', t)
    #     x[self.rand.randint(0, len(x) - 1)].mutate(self)
    #
    # def mutate(self, ctx):
    #     node = self.children[self.rand.randint(0, len(self.children) - 1)]
    #     self.children.remove(node)
    #     self.children.insert(self.rand.randint(0, len(self.children) - 1), node)
# TODO: zastanowic sie nad tym xdddd
    def mutate(self, ctx_or_t):
        if isinstance(ctx_or_t, Program):
            node = self.children[self.rand.randint(0, len(self.children) - 1)]
            self.children.remove(node)
            self.children.insert(self.rand.randint(0, len(self.children) - 1), node)
            return

        elif isinstance(ctx_or_t, type):
            x = self.mutables
            mutables_ = [node for node in self.mutables if isinstance(node, ctx_or_t)]
            if mutables_:
                mutables_[self.rand.randint(0, len(mutables_) - 1)].mutate(self)
                return
            print('this should not happen', ctx_or_t)
            x[self.rand.randint(0, len(x) - 1)].mutate(self)
        raise Exception('Invalid type')

    def has_node_of_type(self, t):
        return any([isinstance(node, t) for node in self.nodes])

    def can_be_mutated(self):
        return len(self.mutables) > 0