# Tri-diagonal matrix generator using compressed sparse column format based on 1-index
# Ji-Hoon Kang, KISTI

# Update for saving .rua file and changing dimension
# Chanyoung Ahn (https://github.com/cold-young)
# 24.05.27

# Command Example:
# $ python generate_matrix.py --dim=20 --random=True
# TODO: Randomization A matrix

import argparse
import os
import datetime as dt

import numpy as np
import math
import random

current_directory = os.path.dirname(os.path.abspath(__file__))
default_path = os.path.join(current_directory, "matrix_data")

parser = argparse.ArgumentParser("Visualize Sparse Tridiagonal Matrix")
parser.add_argument("--dim", type=int, default=16, help="dimension of matrix")
parser.add_argument("--path", type=str, default=default_path, help="Path of .rua file")
parser.add_argument(
    "--name", type=str, default="random", help="a name of generated rua file"
)
parser.add_argument("--view", type=str, default="False", help="View matrix file")
parser.add_argument("--random", type=str, default="False", help="b matrix randomization True/False. Default is False.")
args_cli = parser.parse_args()

lines = []
size = args_cli.dim

### element of b matrix ###
rhs = np.zeros(args_cli.dim, "double")
if args_cli.random == "False":
    rhs[0] = 1
    for i in range(1, size - 1):
        rhs[i] = 0
    rhs[size - 1] = 5
else:
    for i in range(size):
        rhs[i] = random.randint(-10, 10)
###########################

## Diagonal element of A matrix ##
a_diag = 2.0
a_lower = -1.0
a_upper = -1.0
##################################

col_ptr = np.zeros(args_cli.dim + 1, "int32")
col_ptr[0] = 1
for i in range(1, size):
    col_ptr[i] = 3 * i
col_ptr[size] = col_ptr[size - 1] + 2

nnz = size * 3 - 2
row_ind = np.zeros(nnz, "int32")
val = np.zeros(nnz, "double")

row_ind[0] = 1
row_ind[1] = 2

val[0] = 2
val[1] = -1

for i in range(1, size - 1):
    row_ind[3 * i - 1] = i
    row_ind[3 * i + 0] = i + 1
    row_ind[3 * i + 1] = i + 2

    val[3 * i - 1] = -1
    val[3 * i + 0] = 2
    val[3 * i + 1] = -1

row_ind[nnz - 2] = size - 1
row_ind[nnz - 1] = size

val[nnz - 2] = -1
val[nnz - 1] = 2

# Line 1:
# TITLE, (72 characters)
# KEY, (8 characters)
Line1 = "{0:72}{1:8}".format("Tridiagonal matirx", "tdm")
lines.append(Line1)

if args_cli.view == "True":
    print(Line1)

PTRFMT_width = len(str(col_ptr[-1])) + 1
PTRFMT_count = 80 // PTRFMT_width
INDFMT_width = len(str(row_ind[-1])) + 1
INDFMT_count = 80 // INDFMT_width

VALFMT_width = 15
VALFMT_precs = 8
VALFMT_count = 5
RHSFMT_width = 15
RHSFMT_precs = 8
RHSFMT_count = 5

PTRCRD = math.ceil((size + 1) / PTRFMT_count)
INDCRD = math.ceil(nnz / INDFMT_count)
VALCRD = math.ceil(nnz / VALFMT_count)
RHSCRD = math.ceil(size / RHSFMT_count)
TOTCRD = PTRCRD + INDCRD + VALCRD + RHSCRD

# Line 2:
# TOTCRD, integer, total number of data lines, (14 characters)
# PTRCRD, integer, number of data lines for pointers, (14 characters)
# INDCRD, integer, number of data lines for row or variable indices, (14 characters)
# VALCRD, integer, number of data lines for numerical values of matrix entries, (14 characters)
# RHSCRD, integer, number of data lines for right hand side vectors, starting guesses, and solutions, (14 characters)
Line2 = "{0:14d}{1:14d}{2:14d}{3:14d}{4:14d}".format(
    TOTCRD, PTRCRD, INDCRD, VALCRD, RHSCRD
)
lines.append(Line2)

if args_cli.view == "True":
    print(Line2)

# Line 3:
# MXTYPE, matrix type (see table), (3 characters)
# blank space, (11 characters)
# NROW, integer, number of rows or variables, (14 characters)
# NCOL, integer, number of columns or elements, (14 characters)
# NNZERO, integer, number of row or variable indices. For "assembled" matrices, this is just the number of nonzero entries. (14 characters)
# NELTVL, integer, number of elemental matrix entries. For "assembled" matrices, this is 0. (14 characters)
Line3 = "{0:3s}{1:11}{2:14d}{3:14d}{4:14d}{5:14d}".format("RUA", "", size, size, nnz, 0)
lines.append(Line3)

if args_cli.view == "True":
    print(Line3)

# Line 4:
# PTRFMT, FORTRAN I/O format for pointers, (16 characters)
# INDFMT, FORTRAN I/O format for row or variable indices, (16 characters)
# VALFMT, FORTRAN I/O format for matrix entries, (20 characters)
# RHSFMT, FORTRAN I/O format for right hand sides, initial guesses, and solutions, (20 characters)
ptrfmt_str = f"({PTRFMT_count}I{PTRFMT_width})"
indfmt_str = f"({INDFMT_count}I{INDFMT_width})"
valfmt_str = f"({VALFMT_count}E{VALFMT_width}.{VALFMT_precs})"
rhsfmt_str = f"({RHSFMT_count}E{RHSFMT_width}.{RHSFMT_precs})"

Line4 = "{0:16s}{1:16s}{2:20s}{3:20s}".format(
    ptrfmt_str, indfmt_str, valfmt_str, rhsfmt_str
)
lines.append(Line4)

if args_cli.view == "True":
    print(Line4)

# Line 5:
Line5 = "{0:3s}{1:11}{2:14d}{3:14d}".format("F", "", 1, 0)
lines.append(Line5)

if args_cli.view == "True":
    print(Line5)

# 6 row
tmp = ""
for i in range(size + 1):
    tmp += "{0:{1}}".format(col_ptr[i], PTRFMT_width)
    if ((i + 1) % PTRFMT_count == 0) or (i == size):
        lines.append(tmp)
        if args_cli.view == "True":
            print(tmp)
        tmp = ""

# 7 row
tmp = ""
for i in range(nnz):
    tmp += "{0:{1}}".format(row_ind[i], INDFMT_width)
    if ((i + 1) % INDFMT_count == 0) or (i == nnz - 1):
        lines.append(tmp)
        if args_cli.view == "True":
            print(tmp)
        tmp = ""


tmp = ""
for i in range(nnz):
    tmp += "{0:15.8e}".format(val[i])
    if ((i + 1) % VALFMT_count == 0) or (i == nnz - 1):
        lines.append(tmp)
        if args_cli.view == "True":
            print(tmp)
        tmp = ""

tmp = ""
for i in range(size):
    tmp += "{0:15.8e}".format(rhs[i])
    if ((i + 1) % RHSFMT_count == 0) or (i == size - 1):
        lines.append(tmp)
        if args_cli.view == "True":
            print(tmp)
        tmp = ""

if args_cli.name == "random":
    name = f"tdm{args_cli.dim}_" + dt.datetime.now().strftime("%m%d") + ".rua"
else:
    name = args_cli.name + ".rua"

file_path = os.path.join(args_cli.path, name)

with open(f"{file_path}", "w") as f:
    for line in lines:
        f.write(line + "\n")

print("Generated Matrix!")
