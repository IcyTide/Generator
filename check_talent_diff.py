from kungfus import SUPPORT_KUNGFUS
from tools.utils import read_tab

kungfu_info = read_tab("settings/skill/mainkungfuinfo.tab")
talent_tab = read_tab("settings/skill/tenextrapoint.tab")


def main():
    for kungfu in SUPPORT_KUNGFUS:
        if kungfu.kungfu_id > 100000:
            continue
        kungfu_id = kungfu_info[kungfu_info.KungfuID == kungfu.kungfu_id].iloc[0].KungfuIndex
        talent_rows = talent_tab[talent_tab.KungFuID == kungfu_id]
        all_talents = []
        for row in talent_rows.itertuples():
            all_talents.append(talents := [])
            for i in range(12):
                skill_id = getattr(row, f"SkillID{i + 1}")
                if not skill_id:
                    break
                talents.append(skill_id)
        for i in range(len(kungfu.talents)):
            for x, y in zip(all_talents[i], kungfu.talents[i]):
                if x != y:
                    print(f"Wrong Talent: {y}; Should be {x}")


if __name__ == '__main__':
    main()