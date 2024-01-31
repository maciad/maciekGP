import copy


class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self.indent = 0

    @property
    def get_children(self):
        return self.children

    def update_indent(self):
        if self.children:
            for n in self.children:
                n.indent = self.indent + 1

    def update_parents(self):
        if self.children:
            for n in self.children:
                if n is not None:
                    n.parent = self
                    n.update_parents()

    def get_nested_nodes(self):
        x = [self]
        if self.children:
            for n in self.children:
                x.extend(n.get_nested_nodes())
        return x

    # def get_nested_nodes(self):
    #     x = [self] if self is not None else []
    #     if self.children:
    #         # Dodano warunek, aby sprawdzić, czy element jest obiektem typu Node
    #         x.extend(n.get_nested_nodes() for n in self.children if isinstance(n, Node))
    #     return x

    # def get_depth(self):
    #     if self.children and len(self.children) > 0:
    #         return max(n.get_depth() for n in self.children) + 1
    #     return 1

    def get_depth(self):
        if self.children:
            # Dodano warunek, aby sprawdzić, czy element jest obiektem typu Node
            children_depths = [n.get_depth() for n in self.children if isinstance(n, Node)]
            return max(children_depths, default=0) + 1
        return 1

    def clone(self):
        new_node = self.__class__()
        new_node.__dict__ = self.__dict__.copy()  # shallow copy
        new_node.children = [n.clone() for n in self.children] if self.children else None
        new_node.update_parents()
        return new_node

    def deep_clone(self):
        return copy.deepcopy(self)

    @staticmethod
    def cross_nodes(n1, n2):
        # this checks inheritance, so we can't cross nodes of different types
        if type(n1) != type(n2):
            return  # can't cross different types
        # get parent nodes
        p1 = n1.parent
        p2 = n2.parent
        # get index of self in parents
        i1 = p1.children.index(n1)
        i2 = p2.children.index(n2)
        # swap children
        p1.children[i1] = n2
        p2.children[i2] = n1
        # fix parents
        n1.parent, n2.parent = p2, p1
