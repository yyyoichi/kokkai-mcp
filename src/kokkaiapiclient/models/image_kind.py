from enum import Enum

class ImageKind(str, Enum):
    会議録 = "会議録",
    目次 = "目次",
    索引 = "索引",
    附録 = "附録",
    追録 = "追録",

