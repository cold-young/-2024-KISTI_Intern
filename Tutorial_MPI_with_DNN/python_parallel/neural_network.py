import numpy as np
from mpi4py import MPI
import math
import pickle

MNIST_IMAGE_WIDTH = 28
MNIST_IMAGE_HEIGHT = 28
MNIST_IMAGE_SIZE = MNIST_IMAGE_WIDTH * MNIST_IMAGE_HEIGHT
MNIST_LABELS = 10


class NN:
    def __init__(self):
        self.b = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W = np.zeros((MNIST_LABELS, MNIST_IMAGE_SIZE), dtype=np.float32)

    def neural_network_random_weights(self):
        self.b = np.random.rand(MNIST_LABELS).astype(np.float32)
        self.W = np.random.rand(MNIST_LABELS, MNIST_IMAGE_SIZE).astype(np.float32)


class NN_Grad:
    def __init__(self):
        self.b_grad = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W_grad = np.zeros((MNIST_LABELS, MNIST_IMAGE_SIZE), dtype=np.float32)


# Calculate the softmax vector from the activations. This uses a more
# numerically stable algorithm that normalises the activations to prevent large exponents.
def neural_network_softmax(activations):
    e_activations = np.exp(activations - np.max(activations))
    return e_activations / np.sum(e_activations)


def neural_network_hypothesis(image, network):
    activations = np.dot(network.W, image) + network.b
    return neural_network_softmax(activations)


def neural_network_gradient_update(image, network: NN, gradient: NN_Grad, label):
    activations = neural_network_hypothesis(image, network)
    for i in range(MNIST_LABELS):
        b_grad = activations[i] - (1 if i == label else 0)
        gradient.b_grad[i] += b_grad
        gradient.W_grad[i] += b_grad * image
    return -math.log(activations[label])


def neural_network_training_step(
    dataset: dict,
    network: NN,
    learning_rate: float,
    ista: int,
    iend: int,
    total_size: int,
):
    local_loss = np.array(0.0, dtype=np.float32)
    total_loss = np.array(0.0, dtype=np.float32)

    # Initialize gradient
    gradient = NN_Grad()

    # Calculate the gradient and the loss by looping through the training set
    for i in range(ista, iend + 1):
        local_loss += neural_network_gradient_update(
            dataset["images"][i], network, gradient, dataset["labels"][i]
        )

    comm = MPI.COMM_WORLD
    comm.Allreduce([local_loss, MPI.FLOAT], [total_loss, MPI.FLOAT], op=MPI.SUM)
    comm.Allreduce(MPI.IN_PLACE, gradient.W_grad, op=MPI.SUM)
    comm.Allreduce(MPI.IN_PLACE, gradient.b_grad, op=MPI.SUM)

    # Apply gradient descent to the network
    for i in range(MNIST_LABELS):
        network.b[i] -= learning_rate * gradient.b_grad[i] / float(total_size)
        network.W[i] -= learning_rate * gradient.W_grad[i] / float(total_size)
    return total_loss


def save_network(network: NN, filename: str):
    with open(filename, "wb") as f:
        pickle.dump(network, f)
