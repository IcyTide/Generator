import json
import os
import re

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

BASE_DIR = "../jx3_hd_src"


def read_tab(*files):
    df = None
    for file in files:
        file_path = os.path.join(BASE_DIR, file)
        if df is None:
            df = pd.read_csv(file_path, sep="\t", low_memory=False, encoding="utf-8", on_bad_lines="skip")
        else:
            df = pd.concat([df, pd.read_csv(file_path, sep="\t", low_memory=False, encoding="utf-8", on_bad_lines="skip")])
    df = df.where(pd.notna(df), 0)
    return df


def save_code(prefix, data):
    code = json.dumps(data, indent=4, ensure_ascii=False)
    code = f"{prefix.upper()} = " + re.sub(r'"(-?\d+)":', r'\1:', code) + "\n"
    with open(os.path.join("assets", f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)