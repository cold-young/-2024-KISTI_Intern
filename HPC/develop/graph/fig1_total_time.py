# 2024.07.02.(Tue)
# Benchmark: Total time in torso1 matrix
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

# Figure 1
# r - time 그래프에서 np=8, 16, … 일때 그래프 그리기, (best point 표기해서 보기)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# x-axis : r
# r_1 = [1]
r_2 = [1, 2]
r_4 = [1, 2, 4]
r_8 = [1, 2, 4, 8]
r_16 = [1, 2, 4, 8, 16]
r_32 = [1, 2, 4, 8, 16, 32]
r_64 = [1, 2, 4, 8, 16, 32, 64]
r_128 = [1, 2, 4, 8, 16, 32, 64, 128]

# total times
np4_core1 = [
    17.307959,
    18.081142,
    18.792604,
]

np8_core1 = [
    16.675602,
    16.906695,
    17.216772,
    17.252219,
]

np16_core1 = [
    16.667737,
    15.905342,
    16.48891,
    16.711617,
    17.031261,
]

np32_core1 = [
    16.857234,
    16.35258,
    15.676438,
    16.092027,
    17.240004,
    17.546006,
]

np64_core1 = [
    17.896147,
    18.202787,
    16.649028,
    16.956162,
    18.687322,
    19.228931,
    20.469057,
]

# core2: total times
np4_core2 = [
    18.154871,
    17.944493,
    18.995791,
]

np8_core2 = [
    16.495457,
    16.365529,
    16.887902,
    17.361329,
]

np16_core2 = [
    16.065365,
    15.792654,
    15.950113,
    16.207227,
    17.091533,
]

np32_core2 = [
    15.972149,
    15.618414,
    15.563953,
    15.818393,
    16.49021,
    17.711928,
]

np64_core2 = [
    16.025893,
    15.858274,
    15.76692,
    15.855467,
    16.20224,
    17.207698,
    18.588423,
]

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
fig, ax = plt.subplots()

# ax.plot(
#     r_4,
#     np4_core1,
#     "s-",
#     color="seagreen",
#     label="np=4:node=1",
#     markeredgecolor="black",
# )

# ax.plot(
#     r_8,
#     np8_core1,
#     "s-",
#     color="blue",
#     label="np=8:node=1",
#     markeredgecolor="black",
# )

# ax.plot(
#     r_16,
#     np16_core1,
#     "s-",
#     color="firebrick",
#     label="np=16:node=1",
#     markeredgecolor="black",
# )

# ax.plot(
#     r_32,
#     np32_core1,
#     "s-",
#     color="gold",
#     label="np=32:node=1",
#     markeredgecolor="black",
# )

################################
ax.plot(
    r_4,
    np4_core2,
    "^--",
    color="seagreen",
    label="np=4:node=2",
    markeredgecolor="black",
)
np4_core2_min = np.argmin(np4_core2)
plt.plot(r_4[np4_core2_min], np4_core2[np4_core2_min], "r*", markersize=12)

ax.plot(
    r_8,
    np8_core2,
    "^--",
    # "s-",
    color="blue",
    label="np=8:node=2",
    markeredgecolor="black",
)

np8_core2_min = np.argmin(np8_core2)
plt.plot(r_8[np8_core2_min], np8_core2[np8_core2_min], "r*", markersize=12)

ax.plot(
    r_16,
    np16_core2,
    "^--",
    color="firebrick",
    label="np=16:node=2",
    markeredgecolor="black",
)

np16_core2_min = np.argmin(np16_core2)
plt.plot(r_16[np16_core2_min], np16_core2[np16_core2_min], "r*", markersize=12)

ax.plot(
    r_32,
    np32_core2,
    "^--",
    color="gold",
    label="np=32:node=2",
    markeredgecolor="black",
)

np32_core2_min = np.argmin(np32_core2)
plt.plot(r_32[np32_core2_min], np32_core2[np32_core2_min], "r*", markersize=12)

# ax.plot(
#     r_64,
#     np64_core2,
#     "^--",
#     color="seagreen",
#     label="np=64:node=1",
#     markeredgecolor="black",
# )


plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**6)
plt.ylim(1.5 * 10**1, 2.0 * 10**1)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(r_128)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.ylabel("Wall-clock time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.01)
plt.show()
