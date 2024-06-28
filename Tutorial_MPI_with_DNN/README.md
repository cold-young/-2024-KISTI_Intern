# Parallelizing Neural Networks for MNIST Classification 
**Date**: 2024.06.12 (Wed) <br>
**Writer**: Chanyoung Ahn ([cold-young](https://github.com/cold-young))
___

## Getting Started 

1. Clone this repository:
    ```sh
    git clone https://github.com/cold-young/2024_KISTI_Intern.git
    ```

2. Navigate to this directory & Install the dependencies:
    ```sh
    cd ~/2024_KISTI_Intern/lecture_p2
    ```
3. Install conda dependencies: 
   - Install Minconda: [link](https://docs.anaconda.com/free/miniconda/)
    ```sh
    conda env create -f requirements.yaml
    conda activate p2env    
    ```
4. Test Examples:
   ```sh
    # python_serial
    cd ~/python_serial
    python main_mnist.py

    # python_parallel (MPI parallel version)
    cd ~/python_parallel
    mpirun -np 4 python main_mnist.py 
   ```
    - Test your traied model at `test_model.ipynb` using *jupyter_notebook*.

## Directory Layout
```text
    leacture_p2
    ├── environment.yaml
    ├── python_parallel
    │   ├── data
    │   ├── main_mnist.py
    │   ├── mnist_file.py
    │   └── neural_network.py
    ├── python_serial
    │   ├── data
    │   ├── main_mnist.py
    │   ├── mnist_file.py
    │   ├── neural_network.py
    │   └── test_dataset.ipynb
    ├── python_serial_2 
    │   ├── data
    │   ├── main_mnist.py
    │   ├── mnist_file.py
    │   ├── neural_network.py
    └── README.md
```
- `python_parallel`: Classification NN w/ MPI 
- `python_serial`: Classification NN w/o MPI 
- `python_serial_DNN`: Classficiation NN w/o MPI + hidden layer .. 
- `python_parallel_DNN`: Classficiation NN w/ MPI + hidden layer .. 
