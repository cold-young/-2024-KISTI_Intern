import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

import scipy.stats
from tqdm import tqdm

# Step 1: mtx loader
parser = argparse.ArgumentParser("Get Correlation factor & Visulaize")
parser.add_argument("--name", type=str, default="twotone", help="name of .mtx file")
parser.add_argument("--vis", type=str, default="True", help="False or True")
current_directory = os.path.dirname(os.path.abspath(__file__))
absolute_path = "/home/chanyoung/Intern/Conf_poster/baseline_matrix/mtx"
args_cli = parser.parse_args()


def get_nnz_mn(file_path):
    m_size = int
    n_size = int
    nnz = int
    reading_data = False
    m = []
    n = []

    with open(file_path, "r") as file:
        for line in tqdm(file, desc="load mtx file"):
            if line.startswith("%"):
                continue

            if not reading_data:
                parts = line.split()
                m_size = int(parts[0])
                n_size = int(parts[1])
                nnz = int(parts[2])
                print(f"\n Matrix {args_cli.name}: {m_size} * {n_size}, nnz = {nnz}")
                reading_data = True
            else:
                parts = line.split()
                m.append(int(parts[0]))
                n.append(int(parts[1]))

    m = np.array(m)
    n = np.array(n)

    if len(m) != nnz:
        raise ValueError(f"Mismatch expected {nnz}, but get {len(m)}")
    print("done")
    return m, n


# Step 2: Visualize
def visualize_matrix(m, n):
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 5)

    c = np.ones(len(m))
    scatter = ax.scatter(m, n, c, marker="s")
    ax.set_xlabel("Column Index")
    ax.set_ylabel("Row Index")
    plt.title(f"Matrix {args_cli.name} Visualization")
    plt.gca().invert_yaxis()  # 행렬 시각화에서는 y축을 반전시키는 것이 일반적입니다.
    plt.savefig(args_cli.name + ".png", format="png")
    plt.show()


# Step 3: Correlation factor: pearson correlation factor
file_path = os.path.join(absolute_path, args_cli.name + ".mtx")
m, n = get_nnz_mn(file_path)
if args_cli.vis == "True":
    visualize_matrix(m, n)

result = scipy.stats.pearsonr(m, n)
print(f"matrix {args_cli.name}'s correlation factor: {result}")
