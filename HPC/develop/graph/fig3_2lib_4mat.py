# 2024.07.12(Fri)
# Benchmark: Suerplu vs Strumpack in 4 matrix
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Total = True
file_name = "fig3_2lib_4mat_total.png"
size = 7
#######################################################################
if Total:
    # Total Time 
    # # Factor time /w best r-c case (dim / ratio / speedup)
    
    # mc2depi
    superlu_mc2depi = [
    139.55687,
    132.635868,
    128.807417,
    125.734265,
    124.065961,
    ]
    strumpack_mc2depi = [
    35.244902,
    24.15424,
    19.045848,
    15.720414,
    15.102277,
    14.0546,
    13.709388,
    ]
    
    # 256^3 TDM
    superlu_tdm = [
    423.107,
    393.473891,
    382.856642,
    369.06915,
    350.5179,
    348.092226,
    ]
    strumpack_tdm = [
    1318.470459,
    815.123642,
    564.132293,
    437.01672,
    371.396246,
    337.743508,
    ]
    
    # ML_Laplace
    superlu_ml_laplace = [
    119.559997,
    79.806011,
    57.335642,
    45.890487,
    39.046724,
    35.440983,
    ]
    
    strumpack_ml_laplace = [
    97.271677,
    58.295956,
    40.99883,
    31.570772,
    29.305834,
    25.142719,
    24.301913,
    23.317861,
    22.7536,
    22.69958,
    ]
    
    # g7jac200
    superlu_g7jac200 = [
    123.866808,
    59.784501,
    32.113525,
    20.725833,
    14.526157,
    12.25377,
    ]

    strumpack_g7jac200 = [
    117.958532,
    117.385963,
    143.597923,
    132.503456,
    143.141473,
    132.754464,
    ]
else:
    ######################################################################
    # Factor time /w best r-c case (dim / ratio / speedup)
    pass

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
    x_superlu_mc2depi = [1, 2, 4, 8, 16]
    x_strumpack_mc2depi = [1, 2, 4, 8, 16, 32, 64]
    x_superlu_tdm = [4, 8, 16, 32, 64, 128]
    x_strumpack_tdm = [1, 2, 4, 8, 16, 32]
    x_superlu_ml_laplace = [1, 2, 4, 8, 16, 32]
    x_strumpack_ml_laplace = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    x_superlu_g7jac200 = [1, 2, 4, 8, 16, 32]
    x_strumpack_g7jac200 = [1, 2, 4, 8, 16, 32]
    x = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    
else:
    pass
    # Factor Time


x_values = {
     "superlu_mc2depi" : x_superlu_mc2depi,
     "strumpack_mc2depi" : x_strumpack_mc2depi,
     "superlu_tdm" : x_superlu_tdm,
     "strumpack_tdm" : x_strumpack_tdm,
     "superlu_ml_laplace" : x_superlu_ml_laplace,
     "strumpack_ml_laplace" : x_strumpack_ml_laplace,
     "superlu_g7jac200" : x_superlu_g7jac200,
     "strumpack_g7jac200" : x_strumpack_g7jac200,
}

y_values = {
     "superlu_mc2depi" : superlu_mc2depi,
     "strumpack_mc2depi" : strumpack_mc2depi,
     "superlu_tdm" : superlu_tdm,
     "strumpack_tdm" : strumpack_tdm,
     "superlu_ml_laplace" : superlu_ml_laplace,
     "strumpack_ml_laplace" : strumpack_ml_laplace,
     "superlu_g7jac200" : superlu_g7jac200,
     "strumpack_g7jac200" : strumpack_g7jac200,
}

## Dim & nnz
strum_labels ={
    #  "strumpack_mc2depi" :    "mc2depi(strumpack)",
     "strumpack_tdm" :        r"256^3 TDM (strumpack); nnz=1.79E-07",
    #  "strumpack_ml_laplace" : "ML_Laplace(strumpack)",
     "strumpack_g7jac200" :   "g7jac200 (strumpack); nnz=2.04E-04",
 }

superlu_labels ={
    #  "superlu_mc2depi" :    "mc2depi(superlu)",
     "superlu_tdm" :        r"256^3 TDM (superlu); nnz=1.79E-07",
    #  "superlu_ml_laplace" : "ML_Laplace(superlu)",
     "superlu_g7jac200" :   "g7jac200 (suplerlu); nnz=2.04E-04",
 }

colors = ['blue', 'skyblue', 'lightcoral', 'red', 
          'firebrick', 'firebrick', 'firebrick']
markers = ['o', 'v', '^', 's', 'p', '*']
# linestyles = ['-', ':', '--']
linestyles = ['-', '--', '--', '--', ':', '-', '--']

# superlu
for i, (key, st_key) in enumerate(zip(superlu_labels.keys(), strum_labels.keys())):
    ax.plot(
        x_values[key],
        y_values[key],
        marker=markers[i],
        linestyle=linestyles[i],
        color="blue",
        # markeredgecolor="black",
        label=superlu_labels[key],
    )
    
    ax.plot(
        x_values[st_key],
        y_values[st_key],
        marker=markers[i],
        linestyle=linestyles[i],
        color="firebrick",
        # markeredgecolor="black",
        label=strum_labels[st_key],
    )


plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

################################################
# Triangle shape
tri_x = [1, 2, 1, 1]
tri_y = [1000, 500, 500, 1000]
ax.plot(tri_x, tri_y, 'k-', linewidth=1.5)
ax.fill(tri_x, tri_y, 'grey', alpha=0.1)

ax.text(1.4, 480, '2', ha='center', va='top', fontsize=12, color='black')

if Total:
    # total
    ax.text(0.7, 700, '500', ha='left', va='center', fontsize=12, color='black')
    plt.ylabel("Total time (sec)")

else:
    # factor
    ax.text(0.7, 700, '500', ha='left', va='center', fontsize=12, color='black')
    plt.ylabel("Factorization time (sec)")

################################################

# plt.xlim(2**-1, 2**10)
plt.xlim(2**-1, 2**8)
# plt.ylim(10**0, 10**3)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, 
           labelspacing=0.17)

plt.savefig(file_name, format='png')
plt.show()
