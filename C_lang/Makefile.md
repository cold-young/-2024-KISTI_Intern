# C/C++ & Makefile
**Date**: 2024.05.24 (Fri) <br>
**Writer**: Chanyoung Ahn ([cold-young](https://github.com/cold-young))
___

## TBD ...

- *Makefile*
```make
CC = mpiicc

INC = -I/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/include/
LIB = -L/apps/common/xccels_lib/mic-knl/superlu_dist/8.1.2/lib64 -lsuperlu_dist

SRCS  = dreadhb.c dcreate_matrix.c dcreate_matrix_perturbed.c test.c
CFLAGS = -O3 
TARGET = test.out

all :
    $(CC) $(INC) $(LIB) $(SRCS) $(CFLAGS) -o $(TARGET)
```