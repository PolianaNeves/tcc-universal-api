from enum import Enum


class BranchName(str, Enum):
    florida = "florida"
    japan = "japan"
    singapore = "singapore"


class LabelName(str, Enum):
    positive = "pos"
    negative = "neg"
