from tools.classes.dot import Dot


def parse_dot(dot_id):
    dot = Dot(dot_id)
    dot_data = dot.to_asset()
    for buff_level in range(int(dot.max_level)):
        dot, dot.buff_level = Dot(dot_id), buff_level + 1
        for k, v in dot.to_asset().items():
            if k not in dot_data:
                dot_data[k] = [type(v)()] * buff_level
            dot_data[k].append(v)
    return dot_data
