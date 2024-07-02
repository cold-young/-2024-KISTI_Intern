# 2024.06.28
# Benchmark: Factor time in twotone matrix
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Twotone Factor time
Ref = [
    135.43,
    78.44000,
    46.64,
    30,
    18.49,
    # 0,
    # 0
]
nurion_n1 = [
    185.442,
    83.158,
    40.251,
    22.672,
    13.97,
    10.169,
    9.844,
]
nurion_best = [
    185.442,
    67.972,
    28.702,
    13.756,
    7.418,
    4.908,
    # 0,
]

# g7jac200 Factor time
Ref_g7jac200 = [
    283.44,
    153.18,
    83.09,
    49.20,
    31.70,
]

nurion_n1_g7jac200 = [
    62.391,
    47.326,
    30.492,
    21.523,
    16.125,
    14.647,
]

nurion_best_g7jac200 = [
    62.391,
    36.018,
    21.036,
    13.633,
    9.316,
    6.759,
    6.184,
    5.118,
    4.48,
    4.252,
]


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
fig, ax = plt.subplots()

x_8 = [1, 2, 4, 8]
x_16 = [1, 2, 4, 8, 16]
x_32 = [1, 2, 4, 8, 16, 32]
x_64 = [1, 2, 4, 8, 16, 32, 64]
x_512 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# -- Twotone
ax.plot(
    x_64,
    nurion_n1,
    "o-",
    # "^--",
    color="firebrick",
    markeredgecolor="black",
    label="Twotone (Nurion); N=120,750",
)

# -- g7jac200
ax.plot(
    x_32,
    nurion_n1_g7jac200,
    "o-",
    # "^--",
    color="blue",
    markeredgecolor="black",
    label="g7jac200 (Nurion); N=59,310",
)

# -- torso1
ax.plot(
    x_8,
    [4.193, 3.545, 2.893, 2.481],
    "o-",
    color="gold",
    markeredgecolor="black",
    label="torso1 (Nurion); N=116,158",
)

# -- stomach
ax.plot(
    x_32,
    [23.503, 16.184, 10.579, 7.474, 5.975, 5.686],
    "o-",
    color="seagreen",
    markeredgecolor="black",
    label="stomach (Nurion);N=213,360",
)


plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**7)
plt.ylim(10**0, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x_64)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.ylabel("Factorization time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.1)
plt.show()
