import numpy as np

np.random.seed(0)

v = ["i", "y", "u", "e", "o", "ɑ"]
t = ["˥", "˦", "˧", "˨", "˩"]
a = ["", "́", "̀", "̇"]
m = ["", "̄"]
c = [
    "m",
    "n",
    "ɲ",
    "p",
    "b",
    "t̪",
    "d̪",
    "k",
    "g",
    "q",
    "t̪s̪",
    "d̪z̪",
    "t̠ʃ",
    "d̠ʒ",
    "pɸ",
    "bβ",
    "t̪θ",
    "d̪ð",
    "s",
    "z",
    "ʃ",
    "ʒ",
    "ɸ",
    "β",
    "θ",
    "ð",
    "ɾ",
    "r",
    "l̪",
    "ɧ",
]

t_p = ["", "", "", "", ""]
c_p = [
    "m",
    "n",
    "ṅ",
    "p",
    "b",
    "t",
    "d",
    "c",
    "g",
    "q",
    "ṡ",
    "ż",
    "c̄",
    "j̄",
    "ḟ",
    "v̇",
    "þ̇",
    "ð̇",
    "s",
    "z",
    "s̄",
    "j",
    "f",
    "v",
    "þ",
    "ð",
    "r",
    "ṙ",
    "l",
    "h",
]

s = np.array(np.meshgrid(c, v, m, a, t)).T.reshape(-1, 5)

s1 = list(map(lambda a: "".join(["".join(x) for x in a]), s))

np.random.shuffle(s1)

# s2 = np.array(np.meshgrid(s1, s1)).T.reshape(-1, 2)
# s2 = list(map(lambda a: "".join(["".join(x) for x in a]), s2))

# np.random.shuffle(s2)

r = ""
examples = list(s1[0:100])
print(len(s1), examples)

# pyclip.copy(" ".join(examples))

for i, x in enumerate(s1):
    r += f"{x}\n"

with open("output.txt", "w") as file:
    file.write(r)

# print(r)
# pyclip.copy(r)

"""
"""
