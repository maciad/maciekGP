from ProgramGenerator.TreeStructures.Program import Program
from grammar.dist.maciekGPParser import maciekGPParser
from grammar.dist.maciekGPLexer import maciekGPLexer


def generate_program_node_count(min_node_count=12, seed=-1):
    p = Program()
    if seed != -1:
        p = Program(seed=seed)
    while len(p.get_nodes()) < min_node_count:
        p.grow()

    print(p)
    return p


def generate_program_from_config(config, depth_percentage=100):
    p = Program(config=config)
    if int(depth_percentage) == 100:
        p.full_grow()
        return p
    while p.get_depth() < int(config.max_depth * depth_percentage / 100):
        p.grow()
    return p
