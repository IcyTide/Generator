from assets.raw.recipes import RECIPES


class Recipe:
    name: str

    recipe_key: str

    def __init__(self, skill_id: int, index: int, **kwargs):
        self.skill_id = skill_id
        self.index = index
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return dict(
            skill_id=self.skill_id,
            index=self.index,
            name=self.name
        )

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        return cls(
            json["skill_id"],
            json["index"],
            **RECIPES[kungfu_id][json["skill_id"]][json["index"]]
        )


class Recipes:
    def __init__(self, recipes: dict[int, list[Recipe]] = None):
        if not recipes:
            self.recipes = {}
        else:
            self.recipes = recipes

    def __setitem__(self, key, value):
        self.recipes[key] = value

    def __getitem__(self, key):
        return self.recipes[key]

    def get(self, key):
        if key not in self.recipes:
            return []
        return self.recipes[key]

    def __iter__(self):
        for skill, recipes in self.recipes.items():
            for recipe in recipes:
                yield recipe.recipe_key

    def to_dict(self):
        return {
            skill: [recipe.to_dict() for recipe in recipes] for skill, recipes in self.recipes.items()
        }

    @classmethod
    def from_dict(cls, kungfu_id: int, json: dict):
        return cls({
            skill: [Recipe.from_dict(kungfu_id, recipe) for recipe in recipes]
            for skill, recipes in json.items()
        })
