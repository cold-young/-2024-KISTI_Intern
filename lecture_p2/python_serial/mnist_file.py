import numpy as np
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def mnist_get_dataset(images_path, labels_path):
    """
    Description: get dataset from files
    INPUT: dataset paths 
    OUTPUT: 
        dataset: dict
            dataset.size
            dataset.label
            dataset.image
    """
    dataset = {}

    with open(os.path.join(current_directory, images_path), "rb") as mnist_file:
        dataset["images"] = np.frombuffer(
            mnist_file.read(), np.uint8, offset=16
        ).reshape(-1, 28 * 28)

    # Normalizate the data(images)
    dataset["images"] = dataset["images"] / 255.0

    with open(os.path.join(current_directory, labels_path), "rb") as mnist_file:
        dataset["labels"] = np.frombuffer(mnist_file.read(), np.uint8, offset=8)

    # (maybe) need one-hot encoding
    if len(dataset["images"]) != len(dataset["labels"]):
        print("Number of images does not match number of labels")
    else:
        dataset["size"] = len(dataset["images"])

    return dataset


# Fills the batch dataset with a subset of the parent dataset
def mnist_batch(dataset, size, number):
    batch = {}

    start_offset = int(size * number)
    if start_offset >= dataset["size"]:
        return 0

    batch["images"] = dataset["images"][start_offset : start_offset + size]
    batch["labels"] = dataset["labels"][start_offset : start_offset + size]
    batch["size"] = size

    if start_offset + batch["size"] > dataset["size"]:
        batch["size"] = dataset["size"] - start_offset
        print("batch_size:", batch["size"])

    return batch
