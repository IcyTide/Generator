from assets.raw.belongs import BELONGS
from gains.formations import FORMATIONS as RAW_FORMATIONS

FORMATIONS = {
    BELONGS[0][k]["name"]: v for k, v in RAW_FORMATIONS.items()
}

ATTRIBUTE_FUNCS = {
}
