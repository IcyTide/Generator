import json
import os
import re
from pathlib import Path

import pandas as pd


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


def set_comment(instance):
    max_level, comments = instance.max_level, instance.comments
    if comments is None:
        instance.levels = [max_level]
        comments = {}
    elif comments:
        instance.levels = list(comments)
    else:
        instance.levels = list(range(1, max_level + 1))
    comment = instance.comment
    instance.comment = comments.get(instance.level, "") if not comment else comment


def set_patches(instance, patch_map, key, sub_key):
    for k, v in patch_map.get(key, {}).items():
        if isinstance(k, int):
            continue
        instance[k] = v
    for k, v in patch_map.get(key, {}).get(sub_key, {}).items():
        instance[k] = v
    set_comment(instance)


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
    print(f"Saving {prefix} asset")
    code = json.dumps(data, indent=4, ensure_ascii=False, default=lambda x: x.to_dict())
    with open(os.path.join(JSON_DIR, f"{prefix.lower()}.json"), "w", encoding="utf-8") as f:
        f.write(code)
    code = f"{prefix.upper()} = " + re.sub(r'"(-?\d+)":', r'\1:', code) + "\n"
    with open(os.path.join(SAVE_DIR, f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)
