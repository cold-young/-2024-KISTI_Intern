# Study about NVIDIA Modulus 
[![NVIDIA Modulus](https://img.shields.io/badge/NVIDIA-Modulus-nvidia.svg?logo=nvidia)](https://developer.nvidia.com/modulus)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)
[![code style](https://img.shields.io/badge/code_style-black-black.svg)](https://github.com/psf/black)

## What is Modulus?
- NVIDIA Modulus is an open-source framework for building, training, and fine-tuning Physics-ML models with a simple Python interface. 
- Modulus supports the creation of large-scale digital twin models across various physics domains, from computational fluid dynamics and structural mechanics to eletromagnetics. 

## Studies folder
- I documented what I learned while studying NVIDIA modulus in this folder.
  
## Prerequisites
### Installation
[![Modulus docs](https://img.shields.io/badge/Modulus-docs-silver.svg)](https://docs.nvidia.com/deeplearning/modulus/getting-started/index.html)

- **Caution** <br>
  Currently a lot of dependencies are not fully supported using the `pip` method, especially the tesselated geometry moduue in `Modulus Sym`

#### PyPi Install
```shell
pip install nvidia-modulus nvidia-modulus-sym
```

#### Modulus Examples
```shell
# Modulus examples
git clone https://github.com/NVIDIA/modulus.git

cd ./modulus/examples/cfd/darcy_fno/
pip install warp-lang   # Warp is not included in Modulus container
python train_fno_darcy.py

# Modulus Sym exmaples
git clone https://github.com/NVIDIA/modulus-sym.git 
```

#### Develeopment using Modulus
```shell
pip uninstall -y nvidia-modulus nvidia-modulus.sym
```

```shell
git clone https://github.com/NVIDIA/modulus.git
cd modulus/
pip install -e .

# Testing the developments
pip install -e .[dev]
```