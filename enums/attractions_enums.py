from enum import Enum


class BranchName(str, Enum):
    full = "full"
    florida = "florida"
    japan = "japan"
    singapore = "singapore"


class LabelName(str, Enum):
    positive = "pos"
    negative = "neg"
