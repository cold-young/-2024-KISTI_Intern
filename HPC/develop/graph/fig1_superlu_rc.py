# 2024.07.03(Wed)
# Benchmark: Superlu setting r-c parameter
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Total = True
file_name = "fig1_superlu_rm07r_total_all.png"
size = 8
#######################################################################
if Total:
    # Total Time 
    # RM07R;    	381,689	    2.57E-04	8
    n2_c1=[
    1179.999078,
    1262.877602,
    ]

    n2_c2=[
    650.788596,
    673.399728,
    796.003836,
    ]

    n2_c4=[
    393.709046,
    387.612994,
    422.721988,
    487.414104,
    ]

    n2_c8=[
    275.636466,
    249.04793,
    262.433064,
    286.370386,
    335.302916,
    ]
    
    n2_c16=[
    234.789796,
    183.598676,
    181.677728,
    190.856144,
    214.600789,
    263.056303,
    ]

    n2_c32=[
    209.78144,
    168.976562,
    146.246118,
    147.354061,
    160.157736,
    198.652169,
    249.78427,
    ]

    #128
    # n4_c32=[
    # 186.144919,
    # 159.222374,
    # 141.028728,
    # 124.193645,
    # 131.322799,
    # 158.568947,
    # 179.551543,
    # 271.165883,
    # ]
    n2_c64=[
    156.033638,
    144.449602,
    150.633741,
    177.644953,
    ]
    
    #256
    n4_c64=[
    170.789623,
    167.590574,
    140.895539,
    136.329263,
    149.857779,
    167.316219,
    228.79283,
    ]

    #512
    n8_c64=[
    173.940374,
    149.278645,
    150.801411,
    132.569818,
    138.628339,
    151.178472,
    195.081139,
    298.354493,
    ]

    #1024
    n16_c64=[
    214.388836,
    151.193243,
    140.326943,
    143.43336,
    143.564657,
    151.379407,
    185.157928,
    259.148654,
    483.112132,
    ]


else:
    # RM07R;    	381,689	    2.57E-04	8
    n2_c1=[
    1032.632,
    1115.904,
    ]

    n2_c2=[
    530.897,
    553.267,
    676.912,
    ]

    n2_c4=[
    288.801,
    282.813,
    318.349,
    381.581,
    ]

    n2_c8=[
    177.571,
    152.422,
    165.263,
    188.665,
    236.227,
    ]
    
    n2_c16=[
    139.568,
    90.196,
    89.001,
    97.523,
    120.691,
    166.327,
    ]

    n2_c32=[
    112.411,
    75.556,
    54.784,
    55.15,
    67.8,
    105.446,
    151.432,
    ]

    n2_c64=[
    51.81,
    40.895,
    46.744,
    73.605,
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
    x_n2_c1 = [1, 2]
    x_n2_c2 = [1, 2, 4]
    x_n2_c4 = [1, 2, 4, 8]
    x_n2_c8 = [1, 2, 4, 8, 16]
    x_n2_c16 = [1, 2, 4, 8, 16, 32]
    x_n2_c32 = [1, 2, 4, 8, 16, 32, 64]
    x_n2_c64 = [4, 8, 16, 32]
    # x_n4_c32 = [1, 2, 4, 8, 16, 32, 64, 128]
    x_n4_c64 = [2, 4, 8, 16, 32, 64, 128]
    x_n8_c64 = [2, 4, 8, 16, 32, 64, 128, 256]
    x_n16_c64 = [2, 4, 8, 16, 32, 64, 128, 256, 512]
    x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
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
    "n2_c1": x_n2_c1,
    "n2_c2": x_n2_c2,
    "n2_c4": x_n2_c4,
    "n2_c8": x_n2_c8,
    "n2_c16": x_n2_c16,
    "n2_c32": x_n2_c32,
    "n2_c64": x_n2_c64,
    # "n4_c32" : x_n4_c32, 
    "n4_c64" : x_n4_c64, 
    "n8_c64" : x_n8_c64, 
    "n16_c64" : x_n16_c64, 
    }

y_values = {
    "n2_c1":  n2_c1,
    "n2_c2":  n2_c2,
    "n2_c4":  n2_c4,
    "n2_c8":  n2_c8,
    "n2_c16": n2_c16,
    "n2_c32": n2_c32,
    "n2_c64": n2_c64,
    # "n4_c32" :  n4_c32, 
    "n4_c64" :  n4_c64, 
    "n8_c64" :  n8_c64, 
    "n16_c64" : n16_c64, 
    }
## Dim & nnz
labels ={
    "n2_c1":  "np 2",
    "n2_c2":  "np 4",
    "n2_c4":  "np 8",
    "n2_c8":  "np 16",
    "n2_c16": "np 32",
    "n2_c32": "np 64",
    "n2_c64": "np 128",
    # "n4_c32": "np 128",
    "n4_c64": "np 256",
    "n8_c64": "np 512",
    # "n16_c64": "np 1024",
    
}

# colors = ['blue', 'skyblue', 'dodgerblue', 
#           'red', 'lightcoral', 'firebrick']
# colors = ['blue', 'skyblue', 'lightcoral', 'red', 
        #   'firebrick', 'firebrick', 'firebrick']
colors = [ 'skyblue','skyblue','skyblue',
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
    local_min = np.argmin(y_values[key])
    plt.plot(x_values[key][local_min], y_values[key][local_min], "r*", markersize=12)

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

################################################
# Triangle shape
# tri_x = [16, 32, 16, 16]
tri_x = [64, 128, 64, 64]
tri_y = [1000, 500, 500, 1000]
ax.plot(tri_x, tri_y, 'k-', linewidth=1.5)
ax.fill(tri_x, tri_y, 'grey', alpha=0.1)

ax.text(90, 480, '2', ha='center', va='top', fontsize=12, color='black')

if Total:
    # total
    ax.text(45, 700, '500', ha='left', va='center', fontsize=12, color='black')
    plt.ylabel("Total time (sec)")

else:
    # factor
    ax.text(45, 700, '500', ha='left', va='center', fontsize=12, color='black')
    plt.ylabel("Factorization time (sec)")

################################################

# plt.xlim(2**-1, 2**10)
plt.xlim(2**-1, 2**7)
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
