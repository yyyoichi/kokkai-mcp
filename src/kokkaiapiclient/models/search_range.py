from enum import Enum

class SearchRange(str, Enum):
    冒頭 = "冒頭",
    本文 = "本文",
    冒頭・本文 = "冒頭・本文",

