import pandas as pd

from tools.utils import read_tab

buff_settings = read_tab("settings/skill/buff.tab", "settings/skill_mobile/buff.tab")
skill_settings = read_tab("settings/skill/skills.tab")
skill_mobile_settings = read_tab("settings/skill_mobile/skills.tab")
skill_settings["Path"], skill_mobile_settings["Path"] = "skill", "skill_mobile"
skill_settings = pd.concat([skill_settings, skill_mobile_settings])
recipe_settings = read_tab("settings/skill/recipeskill.tab")
recipe_mobile_settings = read_tab("settings/skill_mobile/recipeskill.tab")
recipe_settings["Path"], recipe_mobile_settings["Path"] = "skill", "skill_mobile"
recipe_settings = pd.concat([recipe_settings, recipe_mobile_settings])

# weapon_settings = read_tab("settings/item/Custom_Weapon.tab")
# armor_settings = read_tab("settings/item/Custom_Armor.tab")
# trinket_settings = read_tab("settings/item/Custom_Trinket.tab")
# enchant_settings = read_tab("settings/item/Enchant.tab")
# attrib_settings = read_tab("settings/item/Attrib.tab")
# set_settings = read_tab("settings/item/Set.tab")
# item_settings = read_tab("ui/scheme/case/Item.txt")

skill_event_settings = read_tab("settings/skill/skillevent.tab")

buff_recipe_settings = read_tab("settings/skill/buffrecipe.tab")

skill_txts = read_tab("ui/scheme/case/skill.txt", "ui/scheme/case_mobile/skill.txt")
recipe_txts = read_tab("ui/scheme/case/skillrecipetable.txt")
buff_txts = read_tab("ui/scheme/case/buff.txt", "ui/scheme/case_mobile/buff.txt")
