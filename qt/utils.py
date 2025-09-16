from kungfus import SUPPORT_KUNGFUS


def unfold_kungfus():
    result = {}
    for kungfu in SUPPORT_KUNGFUS:
        result[kungfu.kungfu_id] = kungfu
