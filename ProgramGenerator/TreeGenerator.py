from ProgramGenerator.TreeStructures.Program import Program


def generate_program_node_count(min_node_count=12):
    p = Program()
    while len(p.get_nodes()) < min_node_count:
        p.grow()
    return p


def generate_program_from_config(config, depth_percentage=100):
    p = Program(config=config)
    if int(depth_percentage) == 100:
        p.full_grow()
        return p
    while p.get_depth() < int(config.max_depth * depth_percentage / 100):
        p.grow()
    return p
