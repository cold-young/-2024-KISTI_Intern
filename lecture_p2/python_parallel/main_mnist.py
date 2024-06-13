# MNIST Classification
# Chanyoung Ahn (https://github.com/cold-young)
# 24.06.10

# Command Example:
# $ python

import numpy as np
import matplotlib.pyplot as plt
from mnist_file import mnist_get_dataset, mnist_batch
from neural_network import (
    NN,
    NN_Grad,
    neural_network_training_step,
    neural_network_hypothesis,
)
from mpi4py import MPI

STEPS = 1000
BATCH_SIZE = 400
TEST_BATCH_SIZE = 100

# Dataset
# Downloaded from: http://yann.lecun.com/exdb/mnist/
data_sources = {
    "train_images": "data/train-images-idx3-ubyte",
    "train_labels": "data/train-labels-idx1-ubyte",
    "test_images": "data/t10k-images-idx3-ubyte",
    "test_labels": "data/t10k-labels-idx1-ubyte",
}


def calculate_accuracy(dataset: dict, network: NN, ista: int, iend: int):
    correct = np.array(0.0, dtype=np.float32)
    total_correct = np.array(0.0, dtype=np.float32)

    for i in range(iend - ista + 1):
        activations = neural_network_hypothesis(dataset["images"][i], network)

        predict = np.argmax(activations)
        if predict == dataset["labels"][i]:
            correct += 1.0

    local_correct = np.array(correct / dataset["size"], dtype=np.float32)

    comm = MPI.COMM_WORLD
    comm.Allreduce([local_correct, MPI.FLOAT], [total_correct, MPI.FLOAT], op=MPI.SUM)
    return total_correct / comm.Get_size()


def para_range(N: int, nproc: int, myrank: int):
    iwork1 = N // nproc
    iwork2 = N % nproc
    ista = myrank * iwork1 + min(myrank, iwork2)
    iend = ista + iwork1 - 1
    if iwork2 > myrank:
        iend += 1
    return ista, iend


def main():
    batch = None
    network = NN()
    gradient = NN_Grad()
    loss, accuracy = float, float

    # MPI Initialize
    comm = MPI.COMM_WORLD
    myrank = comm.Get_rank()  # current_process
    nproc = comm.Get_size()  # np

    # Read the dataset from the ./data directory
    train_dataset = mnist_get_dataset(
        data_sources["train_images"], data_sources["train_labels"]
    )
    test_dataset = mnist_get_dataset(
        data_sources["test_images"], data_sources["test_labels"]
    )

    batches = train_dataset["size"] / BATCH_SIZE
    test_batches = test_dataset["size"] / TEST_BATCH_SIZE

    ista1, iend1 = para_range(BATCH_SIZE, nproc, myrank)
    ista2, iend2 = para_range(TEST_BATCH_SIZE, nproc, myrank)

    np.random.seed(0)
    network.neural_network_random_weights()

    for i in range(STEPS):
        # Initialize a new batch
        batch = mnist_batch(train_dataset, BATCH_SIZE, iend1 - ista1 + 1, i % batches)
        test_batch = mnist_batch(
            test_dataset, TEST_BATCH_SIZE, iend2 - ista2 + 1, i % test_batches
        )

        loss = neural_network_training_step(
            batch, network, gradient, 0.05, ista1, iend1, BATCH_SIZE
        )
        accuracy = calculate_accuracy(test_batch, network, ista2, iend2)

        if myrank == 0:
            result = "Step: {0:3}  Average Loss: {1:2.3f} \t Accuracy: {2:3.3f}".format(
                i, loss / BATCH_SIZE, accuracy
            )
            print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback

        traceback.print_exc()
