# 2024.06.28
# Benchmark: Total time in twotone matrix
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Twotone Total Time
nurion_n1 = [
    194.061681,
    90.547553,
    46.907755,
    28.909206,
    20.021185,
    16.393102,
    16.801963,
]
nurion_best = [
    194.061681,
    75.136955,
    35.107221,
    19.768211,
    13.339013,
    10.673334,
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

plt.ylabel("Wall-clock time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.01)
plt.show()
