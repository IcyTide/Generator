from collections import defaultdict
from functools import cache
from typing import List

import matplotlib.pyplot as plt

from base.constant import BINARY_SCALE, FRAME_PER_SECOND
from tools.reader import DataFrameReader
from tools.settings import skill_settings


def parse(content):
    index = 0
    result = {}
    key_flag = False
    code_flags = []
    str_flag = False
    key = ""
    string = ""
    ret = {}
    num = ""
    i = 0
    while i < len(content):
        c = content[i]

        if c == "{":
            code_flags.append(i + 1)
        elif c == "}" and code_flags:
            start = code_flags.pop()
            if not code_flags:
                ret = parse(content[start: i])
        elif code_flags:
            pass
        elif c == '"':
            str_flag = not str_flag
        elif str_flag:
            string += c
        elif c == "]":
            key_flag = False
        elif key_flag:
            key += c
        elif c == "[":
            key_flag = True
        elif c == "=":
            index = int(key) - 1
            key = ""
        elif c == "," and not str_flag:
            if ret:
                result[index] = ret
                ret = {}
            elif num:
                if num == "true":
                    result[index] = True
                elif num == "false":
                    result[index] = False
                else:
                    result[index] = int(num)
                num = ""
            else:
                result[index] = string
                string = ""
            index += 1
        else:
            num += c
        i += 1
    if ret:
        result[index] = ret
    elif num:
        if num == "true":
            result[index] = True
        elif num == "false":
            result[index] = False
        else:
            result[index] = int(num)
    elif string:
        result[index] = string
    return result


def parse_lua(lua_data):
    return parse(lua_data.strip()[1:-1])


CJK_FONTS = ["Microsoft YaHei", "SimHei", "SimSun", "PingFang SC", "Noto Sans CJK SC"]


def setup_font():
    """player_name 是中文名，matplotlib 默认字体（DejaVu Sans）无中文字形会渲染成方框。"""
    current = list(plt.rcParams["font.sans-serif"])
    plt.rcParams["font.sans-serif"] = [f for f in CJK_FONTS if f not in current] + current
    plt.rcParams["axes.unicode_minus"] = False


class Calculator:
    def __init__(self, event_id: int, interval: int, ):
        self.players = {}
        self.records = defaultdict(lambda: defaultdict(int))
        self.reader = DataFrameReader()
        event_row = self.reader.query("event_settings", dict(ID=event_id))[-1]
        self.prob = event_row["Odds"] / BINARY_SCALE
        self.interval = interval * FRAME_PER_SECOND
        self.mask_1, self.mask_2 = event_row["EventMask1"], event_row["EventMask2"]

    @cache
    def check_trigger(self, skill_id):
        row = skill_settings[skill_settings["SkillID"] == skill_id].iloc[-1]
        return row["SkillEventMask1"] & self.mask_1 or row["SkillEventMask2"] & self.mask_2

    def parse_skill(self, row):
        current_frame = int(row[1])
        detail = parse_lua(row[-1])

        react = detail[2]
        if react:
            return

        caster_id = detail[0]

        skill_id = detail[4]

        if self.check_trigger(skill_id):
            self.records[caster_id][current_frame] += 1

    def get_start_frame(self, caster_id) -> int:
        frames = self.records[caster_id]
        return min(frames) if frames else 0

    def get_c_list(self, caster_id) -> List[int]:
        frames = self.records[caster_id]
        if not frames:
            return []
        return [frames[t] for t in range(self.get_start_frame(caster_id), max(frames) + 1)]

    @staticmethod
    def calculate_probs(prob: float, interval: int, c_list: List[int]) -> List[float]:
        probs = [0.0] * len(c_list)

        for t, c in enumerate(c_list):
            if not c:
                continue
            probs[t] = 1 - (1 - prob) ** c
            suppress_prob = sum(probs[max(0, t - interval + 1):t])
            probs[t] *= (1 - suppress_prob)

        return probs

    def calculate(self, caster_id) -> List[float]:
        return self.calculate_probs(self.prob, self.interval, self.get_c_list(caster_id))

    def get_name(self, caster_id) -> str:
        return self.players.get(caster_id, str(caster_id))

    def plot(self, save_path: str = None):
        setup_font()
        for caster_id in self.records:
            probs = self.calculate(caster_id)
            plt.plot(range(len(probs)), probs, label=self.get_name(caster_id))

        plt.title("触发概率")
        plt.xlabel("帧")
        plt.ylabel("概率")
        plt.grid()
        plt.legend()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
        else:
            plt.show()

    def parse_player(self, row):
        detail = parse_lua(row[-1])
        player_id, player_name, kungfu_id = detail[0], detail[1], detail[3]
        self.players[player_id] = player_name

    def read_file(self, file_name: str):
        try:
            lines = open(file_name, encoding="gbk").readlines()
        except UnicodeDecodeError:
            lines = open(file_name, encoding="utf-8").readlines()

        for line in lines:
            row = line.split("\t")
            if row[4] == "21":
                self.parse_skill(row)
            elif row[4] == "4":
                self.parse_player(row)
            else:
                continue


if __name__ == '__main__':
    EVENT_ID = 3293  # 雷·灭气：装备命中后触发，Odds=51 -> prob≈0.0498
    INTERVAL = 60  # 冷却窗口，单位秒（__init__ 内乘 FRAME_PER_SECOND 换算为帧）
    JCL_FILE = "2026-11-13-11-35-46-长安(15)-极境试炼木桩(24538).jcl"

    calculator = Calculator(EVENT_ID, INTERVAL)
    calculator.read_file(JCL_FILE)

    print(f"prob={calculator.prob:.4f}, interval={calculator.interval} frames")
    for caster_id in calculator.records:
        c_list = calculator.get_c_list(caster_id)
        probs = calculator.calculate(caster_id)
        print(f"{calculator.get_name(caster_id)}: "
              f"{len(c_list)} frames, {sum(c_list)} triggers, "
              f"{sum(1 for e in probs if e > 0)} non-zero, max={max(probs):.4f}")

    calculator.plot()
