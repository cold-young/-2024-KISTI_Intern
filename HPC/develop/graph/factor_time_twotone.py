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

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
fig, ax = plt.subplots()

x_ref = [1, 2, 4, 8, 16]
x = [1, 2, 4, 8, 16, 32, 64]
x_best = [1, 2, 4, 8, 16, 32]

ax.plot(
    x_ref,
    Ref,
    "o-",
    color="gold",
    label="Table 4",
)
ax.plot(
    x,
    nurion_n1,
    "^--",
    color="blue",
    label="Nurion (N*1)",
)

ax.plot(
    x_best,
    nurion_best,
    "s-",
    color="firebrick",
    label="Nurion (Best)",
    markeredgecolor="black",
)

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**7)
plt.ylim(10**0, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.ylabel("Factorization time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.01)
plt.show()
