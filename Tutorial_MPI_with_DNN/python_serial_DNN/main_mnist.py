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
    MNIST_LABELS,
    neural_network_hypothesis,
    save_network,
)

STEPS = 500
BATCH_SIZE = 400

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
        activations, _ = neural_network_hypothesis(dataset["images"][i], network)
        predict = np.argmax(activations)
        if predict == dataset["labels"][i]:
            correct += 1

    return correct / dataset["size"]


def main():
    np.random.seed(0)

    network = NN()
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

    for i in range(STEPS):
        # Initialize a new batch
        batch = mnist_batch(train_dataset, BATCH_SIZE, i % batches)

        # Run one step of gradient descent and calculate the loss
        loss = neural_network_training_step(batch, network, 0.05)
        accuracy = calculate_accuracy(test_dataset, network)
        size = batch["size"]
        result = "Step: {0:3}  Average Loss: {1:2.3f} \t Accuracy: {2:3.3f}".format(
            i, loss / size, accuracy
        )
        print(result)
    save_network(network, "./serial_DNN_model.pkl")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback

        traceback.print_exc()
