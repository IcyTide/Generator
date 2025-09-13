from tools.classes.buff import Buff


def parse_buff(buff: Buff) -> dict[int, Buff]:
    result = {}
    for buff_level in buff.levels:
        buff = Buff(buff.buff_id, buff_level)
        result[buff_level] = buff
    return result
