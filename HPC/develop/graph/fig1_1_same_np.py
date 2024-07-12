# 2024.07.03.(Wed)
# Benchmark: Total time in torso1 matrix with same np 
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
np64_core1 = [
    17.896147,
    18.202787,
    16.649028,
    16.956162,
    18.687322,
    19.228931,
    20.469057,
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

np64_core4 = [
    16.211849,
    16.066551,
    15.999596,
    15.870264,
    16.315582,
    22.729153,
    18.5925,
]

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
fig, ax = plt.subplots()

y_values = {
            "np=64:node=1":np64_core1,
            "np=64:node=2":np64_core2,
            "np=64:node=4":np64_core4,
           }

for key in y_values.keys():
    ax.plot(
        r_64,
        y_values[key],
        "^--",
        label=key,
        markeredgecolor="black",
    )
    np64_min = np.argmin(y_values[key])
    plt.plot(r_64[np64_min], y_values[key][np64_min], "r*", markersize=12)

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**6)
# plt.ylim(1.5 * 10**1, 2.0 * 10**1)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(r_128)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.title("Test: 64np with [1-4] node (torso1)")
plt.ylabel("Wall-clock time (sec)")
plt.xlabel("r")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.01)
plt.show()
