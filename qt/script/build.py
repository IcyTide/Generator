from base.constant import MAX_RECIPE, MAX_TALENT_IN_POOL
from qt import refresh_table
from qt.classes.kungfu import Kungfu
from qt.classes.recipe import Recipe, Recipes
from qt.classes.talent import Talent, Talents
from qt.component.build_widget.widget import BuildWidget, RecipeWidget, TalentWidget


class TalentScript:
    talents: list

    def __init__(self, talent_widget: TalentWidget, build_script: "BuildScript"):
        self.widget = talent_widget
        self.parent = build_script

        self.connect()

    def connect(self):
        for i, talent_combo in enumerate(self.widget.talent_combos):
            talent_combo.currentTextChanged.connect(self.select_talent_combo(i))
        self.widget.talent_pool.itemSelectionChanged.connect(self.select_talent_list)

    def select_talent_combo(self, index: int):
        def inner(talent: str):
            if talent not in self.parent.kungfu.belong2id:
                self.parent.talents.pop(index)
                return
            talent_id = self.parent.kungfu.belong2id[talent]
            self.parent.talents[index] = Talent(talent_id, **self.talents[index][talent])
            self.parent.update_kungfu()

        return inner

    def select_talent_list(self):
        selected_items = self.widget.talent_pool.selectedItems()
        while len(selected_items) > MAX_TALENT_IN_POOL:
            selected_items.pop().setSelected(False)
        self.parent.talents.talent_pool = []
        for i, item in enumerate(selected_items):
            talent = item.text()
            talent_id = self.parent.kungfu.belong2id[talent]
            self.parent.talents.talent_pool.append(Talent(talent_id, **self.talents[-1][talent]))
        self.parent.update_kungfu()

    def init(self, talents: list[dict[int, dict]] = None):
        self.talents = talents
        for i, talent_combo in enumerate(self.widget.talent_combos):
            talent_combo.set_items([""] + list(self.talents[i]))
            if talent := self.parent.talents.get(i):
                talent_combo.setCurrentText(str(talent.name))

        talent_pools = [str(talent.name) for talent in self.parent.talents.talent_pool]
        self.widget.talent_pool.clear()
        self.widget.talent_pool.addItems([str(talent) for talent in self.talents[-1]])
        for i in range(self.widget.talent_pool.count()):
            item = self.widget.talent_pool.item(i)
            item.setSelected(item.text() in talent_pools)


class RecipeScript:
    recipes: dict[int, list[dict]]

    def __init__(self, recipe_widget: RecipeWidget, build_script: "BuildScript"):
        self.widget = recipe_widget
        self.parent = build_script

        self.connect()

    def connect(self):
        self.widget.skill_combo.currentTextChanged.connect(self.select_skill)
        self.widget.recipe_table.itemSelectionChanged.connect(self.select_recipe)

    def select_skill(self, skill):
        if skill not in self.recipes:
            refresh_table(self.widget.recipe_table, [])
            return
        table_data = [[recipe["name"], recipe["desc"]] for recipe in self.recipes[skill]]
        select_rows = [recipe.index for recipe in self.parent.recipes.get(skill)]
        refresh_table(self.widget.recipe_table, table_data, select=False)
        for i in range(self.widget.recipe_table.rowCount()):
            select = i in select_rows
            for j in range(self.widget.recipe_table.columnCount()):
                self.widget.recipe_table.item(i, j).setSelected(select)

    def select_recipe(self):
        skill = self.widget.skill_combo.currentText()
        if skill not in self.recipes:
            return
        skill_id = self.parent.kungfu.belong2id[skill]
        selected_items = self.widget.recipe_table.selectedItems()
        selected_rows = {}
        for item in selected_items:
            row = item.row()
            if row not in selected_rows:
                selected_rows[row] = []
            selected_rows[row].append(item)
        while len(selected_rows) > MAX_RECIPE:
            pop_rows = list(selected_rows)[MAX_RECIPE:]
            for row in pop_rows:
                items = selected_rows.pop(row)
                for item in items:
                    item.setSelected(False)
        self.parent.recipes[skill] = []
        for i in selected_rows:
            self.parent.recipes[skill].append(Recipe(skill_id, i, **self.recipes[skill][i]))
        self.parent.update_kungfu()

    def init(self, recipes: dict):
        self.recipes = recipes
        self.widget.skill_combo.clear()
        self.widget.skill_combo.set_items(list(recipes))


class BuildScript:
    kungfu: Kungfu
    talents: Talents
    recipes: Recipes

    def __init__(self, build_widget: BuildWidget):
        self.widget = build_widget

        self.talent_script = TalentScript(self.widget.talent_widget, self)
        self.recipe_script = RecipeScript(self.widget.recipe_widget, self)

    def init(self, kungfu: Kungfu, talents: Talents = None, recipes: Recipes = None):
        self.kungfu = kungfu

        if not talents:
            self.talents = Talents()
        else:
            self.talents = talents
        if not recipes:
            self.recipes = Recipes()
        else:
            self.recipes = recipes

        self.talent_script.init(kungfu.talents)
        self.recipe_script.init(kungfu.recipes)

        return dict(talents=self.talents, recipes=self.recipes)

    def update_kungfu(self):
        attributes, recipes, gains = self.talents.attributes
        recipes += list(self.recipes)
        self.kungfu.build_attributes = attributes
        self.kungfu.build_recipes = recipes
        self.kungfu.build_gains = gains
        self.kungfu.select_talents = [talent.name for talent in self.talents]

