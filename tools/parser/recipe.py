from tools.classes.recipe import Recipe


def parse_recipe(recipe_id, recipes):
    recipe = Recipe(recipe_id)
    recipe_data = recipe.to_asset()
    for recipe_level in recipes[recipe_id]:
        recipe, recipe.recipe_level = Recipe(recipe_id), recipe_level
        for k, v in recipe.to_asset().items():
            if k not in recipe_data:
                recipe_data[k] = [type(v)()] * recipe_level
            recipe_data[k].append(v)
    return recipe_data
