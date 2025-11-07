from env.skill import Skill


class BuffInSetting:
    buff_id: int
    buff_level: int
    buff_name: str

    max_stack: int
    max_tick: int
    interval: int
    min_interval: int
    max_interval: int

    script_file: str

    begin_attributes: list[tuple[str, int | str]]
    active_attributes: list[tuple[str, int | str]]
    end_attributes: list[tuple[str, int | str]]



class BuffInScript:
    index: int

    source_id: int
    source_skill: Skill

    current_tick: int
    left_tick: int
    current_interval: int
    left_interval: int
    current_stack: int

    custom_value: int
