# 2024.07.11.(Thur)
# Benchmark: 256^3 Total/Factorization time in three baselines 
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

################################################
# Total Time
# tdm_superlu=[
# 423.107,
# 393.473891,
# 382.856642,
# 369.06915,
# 350.5179,
# 348.092226,
# ]

# tdm_strumpack=[
# 1318.470459,
# 815.123642,
# 564.132293,
# 437.01672,
# 371.396246,
# 337.743508,
# ]

# tdm_ptdma=[
# 1.134767,
# 0.745245,
# 0.384509,
# 0.209275,
# 0.116161,
# 0.07306,
# 0.056541,
# 0.034142,
# ]

################################################
# Factor Time
tdm_superlu=[
63.259,
57.332,
45.183,
]

tdm_strumpack=[
621.352,
309.894,
155.549,
77.96,
38.91,
19.619,
10.059,
9.152,
4.672,
2.73,
1.491,
1.144,
]

tdm_ptdma=[

0.673,
0.343,
0.183,
0.098,
0.057,
0.038,
0.02,
]
################################################

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

################################################
fig, ax = plt.subplots()
fig.set_size_inches(8,8)

################################################
# Total Time
# x_tdm_superlu = [4, 8, 16, 32, 64, 128]
# x_tdm_strumpack = [1, 2, 4, 8, 16, 32]
# x_tdm_ptdma = [1, 2, 4, 8, 16, 32, 64, 128]
# x = [1, 2, 4, 8, 16, 32, 64, 128]

################################################
# Factor Time
x_tdm_superlu = [4, 8, 16]
x_tdm_strumpack = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
x_tdm_ptdma = [2, 4, 8, 16, 32, 64, 128]
x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
################################################

x_values = {
            "tdm_superlu": x_tdm_superlu, 
            "tdm_strumpack": x_tdm_strumpack, 
            "tdm_ptdma": x_tdm_ptdma, 
           }

y_values = {
            "tdm_superlu": tdm_superlu, 
            "tdm_strumpack": tdm_strumpack, 
            "tdm_ptdma": tdm_ptdma, 
            }

labels = {
        "tdm_superlu":      f"SuperLU-DIST; speed rate={round(tdm_superlu[0]/tdm_superlu[-1],1)}", 
        "tdm_strumpack":    f"Strumpack; speed rate={round(tdm_strumpack[0]/tdm_strumpack[5],1)}", 
        "tdm_ptdma":        f"PaScaL_TDMA; speed rate={round(tdm_ptdma[0]/tdm_ptdma[5],1)}", 
        }

colors = {
        "tdm_superlu":   "blue",
        "tdm_strumpack": "seagreen",
        "tdm_ptdma":     "firebrick",
        }

for key in x_values.keys():
    ax.plot(
        x_values[key],
        y_values[key],
        "o-",
        # markeredgecolor="black",
        color=colors[key],
        label=labels[key],
    )

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

################################################
# Triangle shape
tri_x = [1, 2, 1, 1]
tri_y = [100, 10, 10, 100]
ax.plot(tri_x, tri_y, 'k-', linewidth=1.5)
ax.fill(tri_x, tri_y, 'grey', alpha=0.1)

ax.text(1.4, 9, '2', ha='center', va='top', fontsize=12, color='black')

# total
# ax.text(0.8, 30, '10', ha='left', va='center', fontsize=12, color='black')
# factor
ax.text(0.7, 30, '10', ha='left', va='center', fontsize=12, color='black')

# ax.annotate('', xy=(0.92, 100), xytext=(0.92, 10),
#             arrowprops=dict(arrowstyle='<->', color='black', lw=1))
# ax.annotate('', xy=(1, 8.5), xytext=(2, 8.5),
#             arrowprops=dict(arrowstyle='<->', color='black', lw=1))
################################################


# plt.xlim(2**-1, 2**8) # total
plt.xlim(2**-1, 2**12) # factor
# plt.ylim(10**0, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

# plt.ylabel("Total time (sec)")
plt.ylabel("Factorization time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.12)
# plt.savefig('fig4_3lib_total.png', format='png')
plt.savefig('fig4_3lib_factor.png', format='png')
plt.show()
