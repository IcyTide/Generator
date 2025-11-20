import json

from assets.raw.equipments import EQUIPMENTS
from gains.gears import GAINS

gains = {}
for position, schools in EQUIPMENTS.items():
    for school, kinds in schools.items():
        for kind, equipments in kinds.items():
            for equipment, detail in equipments.items():
                for gain in detail['gains']:
                    _, skill_id, skill_level = gain.split("_")
                    if skill_id not in gains:
                        gains[skill_id] = {}
                    if skill_level not in gains[skill_id]:
                        gains[skill_id][skill_level] = []
                    gains[skill_id][skill_level].append(equipment)

for gain in gains:
    if int(gain) not in GAINS:
        print(gain)
json.dump(gains, open("gains.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)