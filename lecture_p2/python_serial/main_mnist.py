# MNIST Classification
# Chanyoung Ahn (https://github.com/cold-young)
# 24.06.13

# Command Example:
# $ python main_mnist.py


import numpy as np
import matplotlib.pyplot as plt
from mnist_file import mnist_get_dataset, mnist_batch
from neural_network import (
    NN,
    NN_Grad,
    neural_network_training_step,
    neural_network_hypothesis,
    MNIST_LABELS,
)

STEPS = 500
BATCH_SIZE = 100

# Dataset
# Downloaded from: http://yann.lecun.com/exdb/mnist/
data_sources = {
    "train_images": "data/train-images-idx3-ubyte",
    "train_labels": "data/train-labels-idx1-ubyte",
    "test_images": "data/t10k-images-idx3-ubyte",
    "test_labels": "data/t10k-labels-idx1-ubyte",
}


def calculate_accuracy(dataset: dict, network: NN):
    correct = 0

    for i in range(dataset["size"]):
        activations = neural_network_hypothesis(dataset["images"][i], network)
        predict = np.argmax(activations)
        if predict == dataset["labels"][i]:
            correct += 1

    return correct / dataset["size"]


def main():
    batch = None
    network = NN()
    gradient = NN_Grad()
    loss, accuracy = float, float

    # # Read the dataset from the ./data directory
    train_dataset = mnist_get_dataset(
        data_sources["train_images"], data_sources["train_labels"]
    )
    test_dataset = mnist_get_dataset(
        data_sources["test_images"], data_sources["test_labels"]
    )

    np.random.seed(0)

    network.neural_network_random_weights()
    batches = train_dataset["size"] / BATCH_SIZE
    test_batches = test_dataset["size"] / 50

    for i in range(STEPS):
        # Initialize a new batch
        batch = mnist_batch(train_dataset, BATCH_SIZE, i % batches)
        test_batch = mnist_batch(test_dataset, 50, i % test_batches)

        # Run one step of gradient descent and calculate the loss
        loss = neural_network_training_step(batch, network, gradient, 0.05)
        accuracy = calculate_accuracy(test_batch, network)
        size = batch["size"]
        # print(f"Step {i} \t Average Loss: {loss / size} \t Accuracy: {accuracy}")
        result = "Step: {0:3}  Average Loss: {1:10} \t Accuracy: {2:3}".format(
            i, loss / size, accuracy
        )
        print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback

        traceback.print_exc()
