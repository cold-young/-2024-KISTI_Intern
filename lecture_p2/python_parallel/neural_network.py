import numpy as np
from mpi4py import MPI

MNIST_IMAGE_WIDTH = 28
MNIST_IMAGE_HEIGHT = 28
MNIST_IMAGE_SIZE = MNIST_IMAGE_WIDTH * MNIST_IMAGE_HEIGHT
MNIST_LABELS = 10


class NN:
    def __init__(self):
        self.b = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W = np.zeros((MNIST_LABELS, MNIST_IMAGE_SIZE), dtype=np.float32)

    def neural_network_random_weights(self):
        np.random.seed(0)
        self.b = np.random.rand(MNIST_LABELS).astype(np.float32)
        self.W = np.random.rand(MNIST_LABELS, MNIST_IMAGE_SIZE).astype(np.float32)


class NN_Grad:
    def __init__(self):
        self.b_grad = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W_grad = np.zeros((MNIST_LABELS, MNIST_IMAGE_SIZE), dtype=np.float32)

    def initialize(self):
        self.b_grad.fill(0)
        self.W_grad.fill(0)


# Calculate the softmax vector from the activations. This uses a more
# numerically stable algorithm that normalises the activations to prevent large exponents.
def neural_network_softmax(activations):
    e_activations = np.exp(activations - np.max(activations))
    return e_activations / e_activations.sum()


def neural_network_hypothesis(image, network):
    activations = np.zeros(MNIST_LABELS, dtype=np.float32)
    for i in range(MNIST_LABELS):
        activations[i] = network.b[i]
        for j in range(MNIST_IMAGE_SIZE):
            activations[i] += network.W[i][j] * image[j]

    return neural_network_softmax(activations)


def neural_network_gradient_update(image, network: NN, gradient: NN_Grad, label):
    activations = neural_network_hypothesis(image, network)
    for i in range(MNIST_LABELS):
        # b_grad = activations[i] - 1 if i == label else activations[i]
        b_grad = activations[i] - (1 if i == label else 0)
        gradient.b_grad[i] += b_grad
        for j in range(MNIST_IMAGE_SIZE):
            # W_grad = b_grad * image[i]
            W_grad = b_grad * image[j]

            gradient.W_grad[i][j] += W_grad

    return -np.log(activations[label])


def neural_network_training_step(
    dataset: dict,
    network: NN,
    gradient: NN_Grad,
    learning_rate: float,
    ista: int,
    iend: int,
    total_size: int,
):
    local_loss = np.array(0.0, dtype=np.float32)
    total_loss = np.array(0.0, dtype=np.float32)

    # Initialize gradient
    gradient.initialize()

    # Calculate the gradient and the loss by looping through the training set
    for i in range(iend - ista + 1):
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
        for j in range(MNIST_IMAGE_SIZE):
            network.W[i][j] -= learning_rate * gradient.W_grad[i][j] / float(total_size)

    return total_loss
