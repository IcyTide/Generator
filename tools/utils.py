import json
import os
import re
import string
from pathlib import Path

import pandas as pd

from .lua.enums import ATTRIBUTE_TYPE

formatter = string.Formatter()


def camel_to_snake(s):
    s1 = re.sub(r'^[a-z0-9]+', '', s)
    s2 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s1)
    s3 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s2)
    return s3.lower()


def camel_to_capital(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.upper()


def path_to_function(s):
    if not s:
        return ""
    s = Path(s).stem
    s1 = re.sub(r'\W', '', s)
    if not s1.isidentifier():
        s1 = '_' + s1
    return s1


def get_variable(prefix: str = "_", *keys):
    ret = prefix
    for key in keys:
        ret += f"_{key}"
    return ret


def process_attr_param(attr, param_1, param_2):
    param_1 = 0 if not param_1 else int(param_1)
    param_2 = 0 if not param_2 else int(param_2)
    if attr == ATTRIBUTE_TYPE.ADD_DAMAGE_BY_DST_MOVE_STATE:
        if param_1 & 386:
            return param_2
        else:
            return 0
    if attr.startswith("call_"):
        return param_1, param_2
    if attr == ATTRIBUTE_TYPE.SET_TALENT_RECIPE or attr == ATTRIBUTE_TYPE.SET_EQUIPMENT_RECIPE:
        return param_1, param_2
    return param_1 or param_2


def set_patches(instance, patch_map, key, sub_key):
    levels = []
    sub_patch_map = {}
    for k, v in patch_map.get(key, {}).items():
        if isinstance(k, int):
            if k <= 0:
                k += instance.max_level
            sub_patch_map[k] = v
            levels.append(k)
            continue
        elif isinstance(k, float):
            k = int(instance.max_level * k)
            sub_patch_map[k] = v
            levels.append(k)
            continue
        if isinstance(v, (list, str)):
            instance[k] += v
        else:
            instance[k] = v
    for k, v in sub_patch_map.get(sub_key, {}).items():
        if isinstance(v, (list, str)):
            instance[k] += v
        else:
            instance[k] = v
    if "{" in instance.comment and "}" in instance.comment:
        levels = range(1, instance.max_level + 1)
        if instance.comment == "{}":
            instance.comment = ""
        args = {}
        for _, field, _, _ in formatter.parse(instance.comment):
            if not field:
                continue
            args[field] = eval(field, dict(level=sub_key))
        if args:
            instance.comment = instance.comment.format(**args)
        else:
            instance.comment = instance.comment.format(sub_key)
    if not levels:
        levels = [instance.max_level]
    instance.levels = levels


BASE_DIR = "../jx3-package"
SAVE_DIR = "assets/raw"
JSON_DIR = "assets/json"


def fill_na(series):
    if pd.to_numeric(series.dropna(), errors="coerce").notna().all():
        return pd.to_numeric(series.fillna("0"), errors="coerce").astype(object)
    else:
        return series.fillna("")


def read_tab(*files):
    df = None
    for file in files:
        file_path = os.path.join(BASE_DIR, file)
        if df is None:
            df = pd.read_csv(file_path, sep="\t", low_memory=False, encoding="gbk", dtype=str, on_bad_lines="skip")
        else:
            df = pd.concat([
                df,
                pd.read_csv(file_path, sep="\t", low_memory=False, encoding="gbk", dtype=str, on_bad_lines="skip")
            ])
    df = df.apply(fill_na)
    return df


def save_code(prefix, data):
    print(f"Saving {prefix} asset code")
    code = json.dumps(
        data, indent=4, ensure_ascii=False, default=lambda x: {k: v for k, v in x.to_dict().items() if v}
    )
    code = f"{prefix.upper()} = " + re.sub(r'"(-?\d+)":', r'\1:', code) + "\n"
    with open(os.path.join(SAVE_DIR, f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)


def save_json(prefix, data):
    print(f"Saving {prefix} asset json")
    with open(os.path.join(JSON_DIR, f"{prefix.lower()}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False, default=lambda x: {k: v for k, v in x.to_dict().items() if v})
