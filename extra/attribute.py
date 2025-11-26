import json

from base.attribute import BaseAttribute
from kungfus import SUPPORT_KUNGFUS

BELONGS = json.load(open("assets/json/belongs.json", encoding="utf-8"))
SCHOOL_KIND_KUNGFUS = {(kungfu.school, kungfu.kind): kungfu for kungfu in SUPPORT_KUNGFUS}


class Attribute(BaseAttribute):
    kungfu_name: str = ""

    def __init__(self, school: str, kind: str):
        kungfu = SCHOOL_KIND_KUNGFUS.get((school, kind))
        if not kungfu:
            return
        kungfu_id = str(kungfu.kungfu_id)
        kungfu_info = BELONGS[kungfu_id][kungfu_id]
        super().__init__(kungfu.major, kungfu_info['damage_type'], kungfu_info['critical_type'])
        for attr, value in kungfu_info['attributes'].items():
            self[attr] += value
        self.kungfu_name = kungfu_info['name']

    def __bool__(self):
        return bool(self.kungfu_name)
