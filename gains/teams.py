from base.expression import Variable


def get_damage():
    equip_score, buff_key = Variable("equip_score"), Variable("buff_20854_1")
    damage_base = equip_score * 0.0080170644 - 1388.323959
    # damage_base = max(damage_base, 1300)
    # buff_key = max(buff_key, 1)
    return damage_base * buff_key * 1.25 * 1.3 * 1.15 * 0.5

GAINS: dict[int, dict] = {
    545: dict(buffs={673: {}}),
    567: dict(buffs={20938: {}}),
    30850: dict(buffs={23573: dict(name="泠风解怀")}),
    404: dict(buffs={362: {}}),
    6806: dict(buffs={6363: dict(levels=[1])}),
    401: dict(buffs={661: dict(on_target=1)}),
    18872: dict(buffs={12717: dict(on_target=1)}),
    2603: dict(buffs={3465: dict(on_target=1)}),
    15115: dict(buffs={23107: {}}),
    246: dict(buffs={566: dict(on_target=1)}),
    5939: dict(buffs={6214: {}}),
    31208: dict(buffs={29294: {}}),
    32381: dict(buffs={24350: {}}),
    362: dict(buffs={378: dict(levels=[7])}),
    359: dict(buffs={375: dict(levels=[5])}),
    29093: dict(buffs={29354: dict(levels=[1])}),
    2234: dict(buffs={24742: {}}),
    3980: dict(buffs={4058: dict(levels=[1], on_target=1)}),
    3985: dict(buffs={4246: dict(levels=[1])}),
    14678: dict(buffs={4246: dict(levels=[2])}),
    13050: dict(buffs={8248: dict(levels=[1], on_target=1)}),
    44566: dict(buffs={8248: dict(levels=[2], on_target=1)}),
    13422: dict(buffs={8504: {}}),
    15072: dict(buffs={10031: {}}),
    18819: dict(buffs={23543: {}}),  # 16911
    28678: dict(buffs={20854: {}}, skills={29532: dict(levels=[1], custom_damage_base=get_damage())}),

    # mobile
    100460: dict(buffs={70684: {}}),
    100424: dict(buffs={70021: {1: dict(comment="《龙吟·悟》奇卷"), 2: dict(comment="战锋·悟")}}),
    100431: dict(buffs={70160: {}}),
    102319: dict(buffs={70167: {2: dict(comment="无往不利·悟")}}),
    101766: dict(buffs={71070: {}}),
    101759: dict(buffs={71417: {}}),
    100120: dict(buffs={71435: {}}),
    100687: dict(buffs={71436: {}}),
    100935: dict(buffs={71433: {}}),
    100874: dict(buffs={71433: {}}),
    101339: dict(buffs={70489: {}}),
    101344: dict(buffs={70501: {}}),
    101144: dict(buffs={71437: {}}),
    101401: dict(buffs={71439: {}}),
    101413: dict(buffs={71438: {}})
}
