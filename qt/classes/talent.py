from assets.raw.belongs import BELONGS


class Talent:
    name: str

    attributes: dict[str, int] = {}
    recipes: list[str] = []
    belong_key: str = ""

    def __init__(self, talent_id: int, **kwargs):
        self.talent_id = talent_id
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return dict(
            talent_id=self.talent_id,
            name=self.name
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        return cls(
            talent_id=json["talent_id"],
            **BELONGS[kungfu_id][json["talent_id"]]
        )


class Talents:
    talent_pool: list[Talent] = []

    def __init__(self, talents: dict[int, Talent] = None):
        if not talents:
            self.talents = {}
        else:
            self.talents = talents

    def __setitem__(self, key, value):
        self.talents[key] = value

    def __getitem__(self, key):
        return self.talents[key]

    def __iter__(self):
        for talent in self.talents.values():
            yield talent
        for talent in self.talent_pool:
            yield talent

    def get(self, key):
        if key not in self.talents:
            return None
        return self.talents[key]

    def pop(self, key):
        if key not in self.talents:
            return None
        return self.talents.pop(key)

    @property
    def content(self):
        attributes, recipes, talents = {}, [], {}
        for talent in self:
            for k, v in talent.attributes.items():
                if k not in attributes:
                    attributes[k] = 0
                attributes[k] += v
            recipes += talent.recipes
            talents[talent.name] = talent.belong_key
        return attributes, recipes, talents

    def to_dict(self):
        ret: dict = {index: talent.to_dict() for index, talent in self.talents.items()}
        ret["talent_pool"] = [talent.to_dict() for talent in self.talent_pool]
        return ret

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        talent_pool = [Talent.from_dict(kungfu_id, talent) for talent in json.pop("talent_pool")]
        instance = cls({
            int(index): Talent.from_dict(kungfu_id, talent) for index, talent in json.items()
        })
        instance.talent_pool = talent_pool
        return instance
