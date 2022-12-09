from secrets import choice
import numpy as np
import pyclip

np.random.seed(0)


def trans(w):
    v_a = ["i", "y", "ï", "ü", "u", "ë", "ö", "o", "e", "ä", "a"]
    c_a = [
        "m",
        "n",
        "p",
        "b",
        "t",
        "d",
        "k",
        "g",
        "c",
        "ǵ",
        "s",
        "z",
        "ś",
        "j",
        "f",
        "v",
        "þ",
        "ð",
        "ç",
        "x",
        "r",
        "ŕ",
        "l",
        "h",
    ]

    for i, x in enumerate(v_a):
        w = w.replace(v[i], x)

    for i, x in enumerate(c_a):
        w = w.replace(c[i], x)

    # for x in t:
    #     w = w.replace(x, "")

    return w


v = ["i", "y", "ɨ", "ʉ", "u", "e", "ø", "o", "ɛ", "ɔ", "ɑ"]
c = [
    "m",
    "n",
    "p",
    "b",
    "t̪",
    "d̪",
    "k",
    "g",
    "t̠ʃ",
    "d̠ʒ",
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
    "ɾ",
    "r",
    "l̪",
    "ɧ",
]

s = np.array(np.meshgrid(c, v)).T.reshape(-1, 2)

s1 = list(map(lambda a: "".join(["".join(x) for x in a]), s))

np.random.shuffle(s1)

# s2 = np.array(np.meshgrid(s1, s1)).T.reshape(-1, 2)
# s2 = list(map(lambda a: "".join(["".join(x) for x in a]), s2))

# np.random.shuffle(s2)

r = ""
#examples = list(map(trans, s1[0:100]))
#print(len(s1), examples)

#pyclip.copy(" ".join(examples))

for i, x in enumerate(s1):
    r += f"{trans(x)}\n"

with open("output.txt", "w") as file:
    file.write(r)

# print(r)
# pyclip.copy(r)

"""
"""
