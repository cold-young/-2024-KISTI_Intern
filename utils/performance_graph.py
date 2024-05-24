# 2024.05.09
# Graph Visualization w/ matplotlib
# Contributor: Chanyoung Ahn (https://github.com/cold-young)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Vectorization vs. no vectorization
noavx_64 = 0.140931818
avx512_64 = 0.095923639
cube64 = [noavx_64, avx512_64]

noavx_512 = 55.887011304
avx512_512 = 32.598592745
cube512 = [noavx_512, avx512_512]

# MPI and OpenMP parallelization
omp512grids = [
    32.606779005,
    21.247073577,
    11.020524112,
    5.955112894,
    3.332149252,
    2.050469994,
    1.497179431,
]
omp64grids = [
    0.094362608,
    0.068243630,
    0.054914403,
    0.048423795,
    0.044562038,
    0.044795658,
    0.046022719,
]
mpi512grids = [
    33.058616927,
    16.421466076,
    9.883300797,
    5.234337983,
    2.639241374,
    1.414837710,
    1.041474111,
]
mpi64grids = [
    0.093972747,
    0.046887890,
    0.032996763,
    0.02490968,
    0.021638118,
    0.019794921,
    0.029807235,
]

# MPI+OpenMP hyprid parallelization
omp_num = [1, 2, 4, 8, 16, 32, 64]
hybrid = [
    0.028580677,
    0.018765798,
    0.020100651,
    0.039248790,
    0.020439823,
    0.022812935,
    0.043820841,
]

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 15

plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Times New Roman"

########################################################
# Fig 1: Vectorization vs/ no vec.
# bar_width = 0.5
# index = np.arange(2)

# # Subplot 1
# ax1 = plt.subplot(121)
# b1 = plt.bar(index, cube64, bar_width, color=['royalblue', 'firebrick'],
#              edgecolor='black', linewidth=1.)

# ax1.annotate('(a)', xy=(0.5, 0), xycoords='axes fraction', fontsize=18,
#                 xytext=(0, -80), textcoords='offset points',
#                 ha='center', va='bottom')

# plt.ylabel('Wall-clock time (sec)')
# plt.xlabel('$64^3$ grids')

# plt.xticks(index, ('AVX \n Disabled', 'AVX \n Enabled'), fontsize=12)
# plt.ylim((0, 0.16))
# plt.xlim(-0.6, 1.6)
# plt.tick_params(axis='x', direction='in', length=4)
# plt.tick_params(axis='y', direction='in', length=4)

# # Subplot 2
# ax2 = plt.subplot(122)
# b2 = plt.bar(index, cube512, bar_width, color=['royalblue', 'firebrick'],
#              edgecolor='black', linewidth=1.)

# ax2.annotate('(b)', xy=(0.5, 0), xycoords='axes fraction', fontsize=18,
#                 xytext=(0, -80), textcoords='offset points',
#                 ha='center', va='bottom')

# # plt.xlabel('AVX')
# plt.xticks(index, ('AVX \n Disabled', 'AVX \n Enabled'), fontsize=12)
# plt.ylim((0, 65))
# plt.xlim(-0.6, 1.6)

# plt.ylabel('Wall-clock time (sec)')
# plt.xlabel('$512^3$ grids')
# plt.tick_params(axis='x', direction='in', length=4)

# plt.tight_layout()
# plt.show()
########################################################


########################################################
# # Fig 2: MPI and OpenMP parallelization
fig, ax = plt.subplots()

# plt.rcParams['legend.loc'] = 'upper right'
# marker_style = dict(color='black', linestyle=':', marker='s',
# markersize=5, markerfacecoloralt='firebrick')

x = [1, 2, 4, 8, 16, 32, 64]

# ax.plot(x, omp512grids, 's:', fillstyle="right", **marker_style)
ax.plot(
    x,
    omp512grids,
    "s--",
    color="blue",
    label="OpenMP w/ $512^3$ grids",
)
ax.plot(
    x,
    omp64grids,
    "^--",
    color="blue",
    label="OpenMP w/ $64^3$ grids",
)

ax.plot(
    x,
    mpi512grids,
    "s-",
    color="firebrick",
    label="MPI w/ $512^3$ grids",
    markeredgecolor="black",
)
ax.plot(
    x,
    mpi64grids,
    "^-",
    color="firebrick",
    label="MPI w/ $64^3$ grids",
    markeredgecolor="black",
)

plt.tick_params(axis="y", direction="in", which="both")
plt.tick_params(axis="x", direction="in", which="both")
plt.tick_params(axis="x", which="minor", length=0)

plt.xlim(2**-1, 2**7)
plt.ylim(10**-2, 10**2)

plt.yscale("log")
ax.set_xscale("log")
ax.set_xticks(x)
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
# ax.legend()

plt.ylabel("Wall-clock time (sec)")
plt.xlabel("Number of cores")
plt.legend(loc="upper right", fontsize="12", frameon=False, labelspacing=0.01)
# plt.tight_layout()
plt.show()


########################################################
# # Fig 3: MPI+OpenMP hyprid parallelization
# fig, ax = plt.subplots()

# x = [1, 2, 4, 8, 16, 32, 64]

# ax.plot(x, hybrid, 'o-', color="royalblue",
#         label="Total number of cores = 64",
#         markeredgecolor='b')

# plt.tick_params(axis='y', direction='in', which='both')
# plt.tick_params(axis='x', direction='in', which='both')
# plt.tick_params(axis='x', which='minor', length=0)

# plt.xlim(2**-1, 2**7)
# plt.ylim(0.015, 0.048)

# # plt.yscale('log')
# ax.set_xscale('log')
# ax.set_xticks(x)
# ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
# # ax.legend()

# plt.ylabel('Wall-clock time (sec)')
# plt.xlabel('Number of threads')
# plt.legend(loc="upper right", fontsize="14", frameon=False, labelspacing=0.01)
# # plt.tight_layout()
# plt.show()
