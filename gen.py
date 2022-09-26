from secrets import choice
import numpy as np
import pyclip

np.random.seed(0)


def trans(w):
    v_a = ["i", "y", "ī", "ū", "ü", "u", "e", "ø", "o", "ä", "ö", "ā", "a"]
    c_a = [
        "m",
        "n",
        "ṅ",
        "ŋ",
        "p",
        "b",
        "t",
        "d",
        "c",
        "k",
        "g",
        "q",
        "ġ",
        "t̠ʃ",
        "d̠ʒ",
        "pɸ",
        "bβ",
        "p̪f",
        "b̪v",
        "s",
        "z",
        "ʃ",
        "ʒ",
        "ɸ",
        "β",
        "f",
        "v",
        "θ",
        "ð",
        "ç",
        "x",
        "χ",
        "h",
        "ɾ",
        "r",
        "l̪",
        "ɧ",
    ]

    for i, x in enumerate(v_a):
        w = w.replace(v[i], x)

    for i, x in enumerate(c_a):
        w = w.replace(c[i], x)

    for x in t:
        w = w.replace(x, "")

    return w


v = ["i", "y", "ɨ", "ʉ", "ɯ", "u", "e", "ø", "o", "ə", "ɛ", "œ", "ʌ", "ɔ", "æ", "ɑ"]
t = ["˥", "˧", "˩"]
c = [
    "m",
    "n",
    "p",
    "b",
    "t̪",
    "d̪",
    "k",
    "g",
    "t̪s̪",
    "d̪z̪",
    "t̠ʃ",
    "d̠ʒ",
    "pɸ",
    "bβ",
    "s",
    "z",
    "ʃ",
    "ʒ",
    "ɸ",
    "β",
    "θ",
    "ð",
    "ç",
    "x",
    "χ",
    "h",
    "ɾ",
    "r",
    "l̪",
    "ɧ",
]

s = np.array(np.meshgrid(v, v, v)).T.reshape(-1, 3)

s1 = list(map(lambda a: "".join(["".join(x) for x in a]), s))

np.random.shuffle(s1)

# s2 = np.array(np.meshgrid(s1, s1)).T.reshape(-1, 2)
# s2 = list(map(lambda a: "".join(["".join(x) for x in a]), s2))

# np.random.shuffle(s2)

r = ""

print(len(s1), s1[10:20])

for i, x in enumerate(s1):
    r += f"{x}    {{}}\n"

# print(r)
pyclip.copy(r)

"""
"""
