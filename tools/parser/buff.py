from tools.classes.buff import Buff


def parse_buff(buff_id):
    buff = Buff(buff_id)
    buff_data = buff.to_asset()
    for buff_level in range(int(buff.max_level)):
        buff, buff.buff_level = Buff(buff_id), buff_level + 1
        for k, v in buff.to_asset().items():
            if k not in buff_data:
                buff_data[k] = [type(v)()] * buff_level
            buff_data[k].append(v)
    return buff_data
