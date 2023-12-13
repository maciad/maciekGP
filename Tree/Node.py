from typing import Optional, List


class Node:
    count = 0

    def __init__(self):
        self.parent = None
        self.children = []
        self.indent = 0
        self.value = self.count
        Node.count += 1

    def update_indent(self):
        if self.children:
            for child in self.children:
                child.indent = self.indent + 1

    def update_parents(self):
        if self.children:
            for child in self.children:
                child.parent = self
                child.update_parents()

    def get_depth(self):
        if self.children:
            return max([child.get_depth() for child in self.children]) + 1
        else:
            return 1

    def get_nested_nodes(self):
        nested_nodes = [self]
        if self.children:
            for child in self.children:
                nested_nodes.extend(child.get_nested_nodes())
        return nested_nodes

    def clone(self):
        new_node = Node()
        new_node.parent = self.parent
        new_node.indent = self.indent
        if self.children:
            new_node.children = [child.clone() for child in self.children]
            new_node.update_parents()
        return new_node

    def __str__(self):
        return f'(parent={self.parent}, indent={self.indent} value={self.value})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def cross_nodes(node1, node2):
        if not isinstance(node1, Node) or not isinstance(node2, Node):
            raise TypeError('Both node1 and node2 must be Node objects')
        if node1.parent is None or node2.parent is None:
            raise ValueError('Both node1 and node2 must have parents')

        parent1 = node1.parent
        parent2 = node2.parent

        index1 = parent1.children.index(node1)
        index2 = parent2.children.index(node2)

        parent1.children[index1] = node2
        parent2.children[index2] = node1

        node1.parent = parent2
        node2.parent = parent1


