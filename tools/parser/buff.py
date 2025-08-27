from tools.classes.buff import Buff


def parse_buff(buff: Buff) -> dict[int, Buff]:
    result = {}
    for buff_level in range(1, int(buff.max_level) + 1):
        buff = Buff(buff.buff_id, buff_level)
        result[buff_level] = buff
    return result
