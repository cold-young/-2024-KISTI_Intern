# Visualize .rua matrix
# Chanyoung Ahn (https://github.com/cold-young)
# 24.05.23

# Command Example:
# $ python matrix_visualizer.py --name=tdm16_example.rua --number=True

import argparse
import os

import numpy as np
import matplotlib.pyplot as plt

current_directory = os.path.dirname(os.path.abspath(__file__))
default_path = os.path.join(current_directory, "matrix_data")

parser = argparse.ArgumentParser("Visualize Sparse Tridiagonal Matrix")
parser.add_argument(
    "--path", type=str, default=default_path, help="Path of folder for .rua files"
)
parser.add_argument(
    "--name", type=str, default="tdm16_example.rua", help="name of .rua file"
)
parser.add_argument("--number", type=str, default="False", help="Number ON/OFF")
args_cli = parser.parse_args()


def parse_harwell_boeing(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Strip newline characters from each line
    lines = [line.rstrip("\n") for line in lines]

    # Header information
    title = lines[0][:72].strip()
    key = lines[0][72:80].strip()

    totcrd = int(lines[1][0:14].strip())
    ptrcrd = int(lines[1][14:28].strip())
    indcrd = int(lines[1][28:42].strip())
    valcrd = int(lines[1][42:56].strip())
    rhscrd = int(lines[1][56:70].strip())

    mxtype = lines[2][0:3].strip()
    nrow = int(lines[2][14:28].strip())
    ncol = int(lines[2][28:42].strip())
    nnzero = int(lines[2][42:56].strip())
    neltvl = int(lines[2][56:70].strip())

    ptrfmt = lines[3][0:16].strip()
    indfmt = lines[3][16:32].strip()
    valfmt = lines[3][32:52].strip()
    rhsfmt = lines[3][52:72].strip()

    rhstyp = None
    nrhs = 0
    nrhsix = 0
    if rhscrd > 0:
        rhstyp = lines[4][0:3].strip()
        nrhs = int(lines[4][14:28].strip())
        nrhsix = int(lines[4][28:42].strip())

    # Parse pointers
    pointers = []
    pointer_lines = lines[5 : 5 + ptrcrd]
    for line in pointer_lines:
        pointers.extend([int(val.strip()) for val in line.split() if val.strip()])

    # Parse indices
    indices = []
    index_lines = lines[5 + ptrcrd : 5 + ptrcrd + indcrd]
    for line in index_lines:
        indices.extend([int(val.strip()) for val in line.split() if val.strip()])

    # Parse values
    values = []
    value_lines = lines[5 + ptrcrd + indcrd : 5 + ptrcrd + indcrd + valcrd]
    # Fixed format: 5E15.8 means each value has a width of 15 characters
    value_width = 15
    for line in value_lines:
        for i in range(0, len(line), value_width):
            segment = line[i : i + value_width].strip()
            if segment:  # Ensure no empty strings are processed
                values.append(float(segment))

    return nrow, ncol, pointers, indices, values


def create_matrix(nrow, ncol, pointers, indices, values):
    A = np.zeros((nrow, ncol))
    for j in range(ncol):
        for idx in range(pointers[j] - 1, pointers[j + 1] - 1):
            i = indices[idx] - 1
            A[i, j] = values[idx]
    return A


def visualize_matrix(A):
    fig, ax = plt.subplots()
    cax = ax.matshow(A, cmap="viridis")
    if args_cli.number == "True":
        for (i, j), val in np.ndenumerate(A):
            if A[i, j] != 0:
                ax.text(
                    j,
                    i,
                    f"{val:.1f}",
                    ha="center",
                    va="center",
                    color="red",
                    size=6,
                    weight="bold",
                )

    plt.colorbar(cax)
    plt.title(f"Matrix Visualization: {args_cli.name}")
    plt.show()


##
file_path = os.path.join(args_cli.path, args_cli.name)
nrow, ncol, pointers, indices, values = parse_harwell_boeing(file_path)
A = create_matrix(nrow, ncol, pointers, indices, values)
visualize_matrix(A)
