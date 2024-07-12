# 2024.07.12(Fri)
# Benchmark: Superlu setting r-c parameter
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Total = True
file_name = "fig1_2_superlu_rm07r_total.png"
size = 8
#######################################################################
if Total:
    # Total Time 
    # RM07R;    	381,689	    2.57E-04	8
    nx1=[
    1115.904,
    676.912,
    381.581,
    236.227,
    166.327,
    151.432,
    ]

    best=[
    1032.632,
    530.897,
    282.813,
    152.422,
    89.001,
    54.784,
    40.895,
    32.433,
    30.117,
    ]

########################################################
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"
########################################################
fig, ax = plt.subplots()
fig.set_size_inches(size, size)

if Total:
    # Total Time
    x_nx1 = [2, 4, 8, 16, 32, 64]
    x_best = [2, 4, 8, 16, 32, 64, 128, 256, 1024]
    x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
else:
    # Factor Time
    x_n2_c1 = [1, 2]
    x_n2_c2 = [1, 2, 4]
    x_n2_c4 = [1, 2, 4, 8]
    x_n2_c8 = [1, 2, 4, 8, 16]
    x_n2_c16 = [1, 2, 4, 8, 16, 32]
    x_n2_c32 = [1, 2, 4, 8, 16, 32, 64]
    x_n2_c64 = [4, 8, 16, 32]
    x = [1, 2, 4, 8, 16, 32]

x_values = {
    "nx1":  x_nx1,
    "best": x_best,
    }

y_values = {
    "nx1":   nx1,
    "best":  best,

    }
## Dim & nnz
labels ={
    "nx1": r"RM07R (n$\times$1)",
    "best":"RM07R (best)",
}

# colors = ['blue', 'skyblue', 'dodgerblue', 
#           'red', 'lightcoral', 'firebrick']
# colors = ['blue', 'skyblue', 'lightcoral', 'red', 
        #   'firebrick', 'firebrick', 'firebrick']
colors = [ 'blue','firebrick','skyblue',
          'skyblue','skyblue','skyblue', 'skyblue',
          'skyblue', 'skyblue', 'skyblue', 
          ]
markers = ['o', 'v', '^', 
           's', 'p', '*', 
           'o', 'v', '^', 's',
           ]
# linestyles = ['-', ':', '--']
linestyles = ['-', '--', '-.', 
              ':', (0, (3, 5, 1, 5)), (0, (5, 1, 1, 1)), 
              (0, (5, 10)), ':', '--', '-.',
              ]

for i, key in enumerate(labels.keys()):
    ax.plot(
        x_values[key],
        y_values[key],
        # marker=markers[i],
        marker='^',
        linestyle=linestyles[i],
        color=colors[i],
        markeredgecolor="black",
        label=labels[key],
    )
    # local_min = np.argmin(y_values[key])
    # plt.plot(x_values[key][local_min], y_values[key][local_min], "r*", markersize=12)

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

################################################
# Triangle shape
# tri_x = [16, 32, 16, 16]
tri_x = [128, 256, 128, 128]
tri_y = [1000, 500, 500, 1000]
ax.plot(tri_x, tri_y, 'k-', linewidth=1.5)
ax.fill(tri_x, tri_y, 'grey', alpha=0.1)

ax.text(180, 480, '2', ha='center', va='top', fontsize=12, color='black')

if Total:
    # total
    ax.text(85, 700, '500', ha='left', va='center', fontsize=12, color='black')
    plt.ylabel("Total time (sec)")

################################################

# plt.xlim(2**-1, 2**10)
plt.xlim(2**-1, 2**11)
# plt.ylim(0.7* 10**2, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.xlabel("r")
plt.legend(loc="upper right", fontsize="12", frameon=False, 
           labelspacing=0.12)

plt.savefig(file_name, format='png')
plt.show()
