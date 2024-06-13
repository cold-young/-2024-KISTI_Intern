import numpy as np

MNIST_IMAGE_WIDTH = 28
MNIST_IMAGE_HEIGHT = 28
MNIST_IMAGE_SIZE = MNIST_IMAGE_WIDTH * MNIST_IMAGE_HEIGHT
MNIST_LABELS = 10
HIDDEN_SIZE = 128


class NN:
    def __init__(self):
        self.b1 = np.zeros(HIDDEN_SIZE, dtype=np.float32)
        self.W1 = np.zeros((HIDDEN_SIZE, MNIST_IMAGE_SIZE), dtype=np.float32)
        self.b2 = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W2 = np.zeros((MNIST_LABELS, HIDDEN_SIZE), dtype=np.float32)

    def neural_network_random_weights(self):
        self.b1 = 0.01 * np.random.rand(HIDDEN_SIZE).astype(np.float32)
        self.W1 = 0.01 * np.random.rand(HIDDEN_SIZE, MNIST_IMAGE_SIZE).astype(
            np.float32
        )
        self.b2 = 0.01 * np.random.rand(MNIST_LABELS).astype(np.float32)
        self.W2 = 0.01 * np.random.rand(MNIST_LABELS, HIDDEN_SIZE).astype(np.float32)

    def neural_network_hypothesis(self, image):
        hidden_activations = np.maximum(
            0, np.dot(self.W1, image) + self.b1
        )  # ReLU activation for hidden layer
        output_activations = np.dot(self.W2, hidden_activations) + self.b2

        # Softmax activation for output layer
        e_activations = np.exp(output_activations - np.max(output_activations))
        return e_activations / e_activations.sum()


class NN_Grad:
    def __init__(self):
        self.b1_grad = np.zeros(HIDDEN_SIZE, dtype=np.float32)
        self.W1_grad = np.zeros((HIDDEN_SIZE, MNIST_IMAGE_SIZE), dtype=np.float32)
        self.b2_grad = np.zeros(MNIST_LABELS, dtype=np.float32)
        self.W2_grad = np.zeros((MNIST_LABELS, HIDDEN_SIZE), dtype=np.float32)

    def initialize(self):
        self.b1_grad.fill(0)
        self.W1_grad.fill(0)
        self.b2_grad.fill(0)
        self.W2_grad.fill(0)


def neural_network_gradient_update(image, network: NN, gradient: NN_Grad, label):
    # Forward pass
    hidden_activations = np.maximum(0, np.dot(network.W1, image) + network.b1)
    output_activations = np.dot(network.W2, hidden_activations) + network.b2

    # Softmax activation for output layer
    e_activations = np.exp(output_activations - np.max(output_activations))
    softmax_output = e_activations / e_activations.sum()

    # Comute gradient
    dL_dsoftmax = np.copy(softmax_output)
    dL_dsoftmax[label] -= 1

    dL_dW2 = np.outer(dL_dsoftmax, hidden_activations)
    dL_db2 = dL_dsoftmax

    dL_dhidden = np.dot(network.W2.T, dL_dsoftmax)
    dL_dhidden[hidden_activations <= 0] = 0  # Gradient of ReLU activation

    dL_dW1 = np.outer(dL_dhidden, image)
    dL_db1 = dL_dhidden

    # Accumulate gradients
    gradient.W2_grad += dL_dW2
    gradient.b2_grad += dL_db2
    gradient.W1_grad += dL_dW1
    gradient.b1_grad += dL_db1

    # Calculate loss
    loss = -np.log(softmax_output[label])
    return loss


def neural_network_training_step(
    dataset: dict, network: NN, gradient: NN_Grad, learning_rate: float
):
    total_loss = 0.0

    # Initialize gradient
    gradient.initialize()

    # Calculate the gradient and the loss by looping through the training set
    for i in range(dataset["size"]):
        tmp = neural_network_gradient_update(
            dataset["images"][i], network, gradient, dataset["labels"][i]
        )
        total_loss += tmp

    for i in range(HIDDEN_SIZE):
        network.b1[i] -= learning_rate * gradient.b1_grad[i] / dataset["size"]
        for j in range(MNIST_IMAGE_SIZE):
            network.W1[i][j] -= learning_rate * gradient.W1_grad[i][j] / dataset["size"]

    for i in range(MNIST_LABELS):
        network.b2[i] -= learning_rate * gradient.b2_grad[i] / dataset["size"]
        for j in range(HIDDEN_SIZE):
            network.W2[i][j] -= learning_rate * gradient.W2_grad[i][j] / dataset["size"]

    return total_loss
