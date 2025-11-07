class SkillInSetting:
    skill_id: int
    skill_level: int
    skill_name: str

    script_file: str

    skill_event_mask_1: int
    skill_event_mask_2: int

    recipe_type: int

    cast_mask: int


class SkillInScript:
    index: int

    self_rollback_attributes: list[tuple[str, int | str]]
    dest_rollback_attributes: list[tuple[str, int | str]]
    self_attributes: list[tuple[str, int | str]]
    dest_attributes: list[tuple[str, int | str]]

    prepare_frames: int
    min_prepare_frames: int
    channel_interval: int
    min_channel_interval: int
    channel_frame: int
    min_channel_frame: int

    instant_channel: bool
    ignore_prepare_state: bool
